from django.contrib import admin
from django.urls import path, include
from searchtable.views import *
from ranktable.views import *


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('searchtable/', include('searchtable.urls')),
    path('rank/', include('ranktable.urls')),
    path('user/', include('user.urls')),
    path('detail/', include('data.urls')),
]
