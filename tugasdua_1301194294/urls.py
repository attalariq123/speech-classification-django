from django.urls import path
from . import views

app_name = 'tugasdua'

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course, name='course')
]