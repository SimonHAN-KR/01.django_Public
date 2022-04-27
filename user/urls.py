from django.urls import path, include

from .views import *

urlpatterns = [
    path('login/', login),  # login
    path('register/', register),
    path('logout/', logout),
    # path('social/', include('allauth.urls')),
]
