from django.urls import path
from .views import PassportAPIView

urlpatterns = [
    path('', PassportAPIView.as_view(), name='index'),
]


# from django.urls import path
# from mrz_app import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]