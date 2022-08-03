from django.urls import path

from . import views

app_name = 'email_network'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]
