from django.urls import path
from . import views

app_name = 'galeria'
urlpatterns = [
    path('', views.galeria_list, name='index'),
    path('<int:pk>/', views.model_form_upload, name='detail'),
    path('galeria/<int:pk>/delete', views.delete_galeria, name='delete_galeria'),
    path('photo/<int:pk>/delete', views.delete_photo, name='delete_foto')
]