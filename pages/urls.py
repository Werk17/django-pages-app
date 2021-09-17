from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), #new
    path('', HomePageView.as_view(), name='home'),
    ]
