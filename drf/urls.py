from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/', include('send_email.urls')),
]



