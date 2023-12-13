from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


urlpatterns = [
    path('', views.EmailCreateView.as_view(), name='create_message'),
    path(r'api/captcha/', include('rest_captcha.urls')),
]


