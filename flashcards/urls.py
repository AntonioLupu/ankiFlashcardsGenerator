from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-page'),
    path('overview/', views.overview, name='overview-page'),
    path('starting/', views.starting, name='starting-page'),
    path('generate-csv/', views.generate_csv, name='generate-csv')
]
