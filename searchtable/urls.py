from django.urls import path
from .views import *

urlpatterns = [
    path('', cor_list, name='cor_list'),
]

