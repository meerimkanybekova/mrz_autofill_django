from django.urls import path
from mrz_app import views

urlpatterns = [
    path('', views.index, name='index'),
]