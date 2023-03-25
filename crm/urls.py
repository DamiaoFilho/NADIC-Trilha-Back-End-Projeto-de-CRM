from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('index/', index.as_view(), name='index'),
    path('createStock/', stockCreate.as_view(), name='stockCreate'),
    path('createCompany/', companyCreate.as_view(), name='companyCreate'),
    path('createCategory/', categoryCreate.as_view(), name='categoryCreate'),
    path('list/', stockList.as_view(), name="stockList"),
    path('update/<pk>/', stockUpdate.as_view(), name='stockUpdate'),
    path('delete/<pk>/', stockDelete.as_view(), name='stockDelete'),
    path('sell/', productSell, name='productSell')
]
