from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches
import json
import csv

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
    # print(equities)
    lastUpdated = redis_client.hgetall('lastUpdated')
    lastUpdated = lastUpdated[b'lastUpdated']
    lastUpdated = lastUpdated.decode("utf-8")
    print(lastUpdated)
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
    # print(equities)
    return HttpResponse(json.dumps(equities), content_type="text/json")
  except Exception as e:
    return HttpResponse(json.dumps({'Error': str(e)}), content_type="text/json")

def exportCSV(request, name=None):
  try:
    keys = []
    if name is not None:
      keys = redis_client.keys('*' + name.upper() + '*')
    else:
      keys = redis_client.keys('*')
    
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="EquityList.csv"'  
    csvFile = csv.writer(response)
    csvFile.writerow(['Code', 'Name', 'Open', 'High', 'Low', 'Close'])

    for key in keys:
      value = redis_client.hgetall(key)
      values = value.values()
      values = [val.decode("utf-8")  for val in values]
      csvFile.writerow(values)  

    return response
  except Exception as e:
    return HttpResponse(json.dumps({'Error': str(e)}), content_type="text/json")