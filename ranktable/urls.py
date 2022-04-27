from django.urls import path
from .views import rank

urlpatterns = [
    path('', rank, name='rank'),
]
