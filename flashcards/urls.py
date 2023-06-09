from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-page'),
    path('overview/', views.overview, name='overview-page'),
]
