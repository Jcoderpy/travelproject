from . import views
from django.urls import path

urlpatterns = [
    path('',views.care,name='care')
]