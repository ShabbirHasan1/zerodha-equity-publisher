from django.urls import path
from . import views

urlpatterns = [
  path('equities', views.fetchAll, name='FetchAllEquities'),
  path('equities/<str:name>', views.fetchByName, name='FetchEquitiesByName'),
  path('equities/export', views.exportCSV, name='ExportAsCsv'),
  path('equities/export/<str:name>', views.exportCSV, name='ExportAllAsCSV'),
  path('clean', views.flushDB, name='CleanAllEquities'),
]