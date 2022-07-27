from django.urls import path

from . import views

app_name = 'message'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('save/', views.save, name='save'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]


