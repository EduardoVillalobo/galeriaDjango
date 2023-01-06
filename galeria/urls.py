from django.urls import path
from . import views

""" Namespace """
app_name = 'galeria'

""" URLpatterns """
urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('', views.galeria_list, name='galeria_list'),
    path('galeria/list', views.galeria_list, name='galeria_list'),
    path('galeria/<int:pk>/', views.galeria_detail, name='galeria_detail'),
    path('galeria/<int:pk>/delete', views.galeria_delete, name='galeria_delete'),
    path('photo/<int:pk>/delete', views.photo_delete, name='photo_delete'),    
]