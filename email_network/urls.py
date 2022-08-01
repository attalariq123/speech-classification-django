from django.urls import path

from . import views

app_name = 'email_network'

urlpatterns = [
    path('', views.index, name='index'),
]
