from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('2023/', special_case_2023),
    path('<int:year>/', year_archive),
    path('<int:year>/<int:month>/', month_archive),
]