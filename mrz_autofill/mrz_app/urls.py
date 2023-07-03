from django.urls import path
from mrz_app import views

urlpatterns = [
    # Other URL patterns
    path('', views.index, name='index'),
]