from django.urls import path, include
from django.views.generic import edit

from .views import *

urlpatterns = [
    path('', index),
    path('add/', add),
    path('edit/<int:article_id>', edit),
    path('delete/<int:article_id>', delete),
]