from django.urls import path
from mensaje import views

app_name = 'mensaje'

urlpatterns = [
    path('mensaje/', views.mensaje_list, name="mensaje_list"),
    path('mensaje/create', views.mensaje_create, name="mensaje_create"),
    path('mensaje/pdf/<int:pk>', views.mensaje_pdf, name="mensaje_pdf")
]