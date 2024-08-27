from django.urls import path
from .views import createUnitMeasurement,createCompany

urlpatterns = [
    path('createUnitMeasurement/',createUnitMeasurement,name='createUnitMeasurement'),
    path('createCompany/',createCompany,name='createCompany')
]