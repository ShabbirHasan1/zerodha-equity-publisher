from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches
from .utils import createCSV
import json

redis_cache = caches['default']
redis_client = redis_cache.client.get_client()

def flushDB(request):
  try:
    redis_client.flushdb()
    return HttpResponse(json.dumps({"message": "DB Cleaned Successfully"}), content_type="text/json")
  except Exception as e:
    return HttpResponse(json.dumps({'Error': str(e)}), content_type="text/json")

# Create your views here.
def fetchAll(request):
  try:
    keys = redis_client.keys('*')
    equities = []
    for key in keys:
      value = redis_client.hgetall(key)
      keys_values = value.items()
      new_d = {k.decode("utf-8") : v.decode("utf-8")  for k, v in keys_values}
      equities.append(new_d)
    lastUpdated = redis_client.hgetall('lastUpdated')
    lastUpdated = lastUpdated[b'lastUpdated']
    lastUpdated = lastUpdated.decode("utf-8")
    return HttpResponse(json.dumps({'equities': equities, 'lastUpdated': lastUpdated}), content_type="text/json")
  except Exception as e:
    return HttpResponse(json.dumps({'Error': str(e)}), content_type="text/json")

def fetchByName(request, name):
  try:
    keys = redis_client.keys('*' + name.upper() + '*')
    equities = []
    for key in keys:
      value = redis_client.hgetall(key)
      keys_values = value.items()
      new_d = {k.decode("utf-8") : v.decode("utf-8")  for k, v in keys_values}
      equities.append(new_d)
    return HttpResponse(json.dumps(equities), content_type="text/json")
  except Exception as e:
    return HttpResponse(json.dumps({'Error': str(e)}), content_type="text/json")

def exportCSV(request, name = None):
  try:
    keys = []
    if name is not None:
      keys = redis_client.keys('*' + name.upper() + '*')
    else:
      keys = redis_client.keys('*')
    return createCSV(keys, client = redis_client)
  except Exception as e:
    return HttpResponse(json.dumps({'Error': str(e)}), content_type="text/json")