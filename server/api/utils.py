from django.http import HttpResponse
import csv

def createCSV(keys, client):
  response = HttpResponse(content_type='text/csv')  
  response['Content-Disposition'] = 'attachment; filename="EquityList.csv"'  
  csvFile = csv.writer(response)
  csvFile.writerow(['Code', 'Name', 'Open', 'High', 'Low', 'Close'])

  for key in keys:
    value = client.hgetall(key)
    values = value.values()
    values = [val.decode("utf-8")  for val in values]
    csvFile.writerow(values)
  return response