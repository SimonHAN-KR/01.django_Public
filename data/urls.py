from django.urls import path
from .views import *

app_name = 'data'

urlpatterns = [
    path('<corp_code>/', corporation_detail, name='corporation_detail'),

]

