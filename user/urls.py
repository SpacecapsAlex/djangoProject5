from django.urls import path
from .views import home, method


urlpatterns = [
    path('', home, name='home'),
    path('method/', method, name='method'),
]