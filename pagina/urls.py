from django.urls import path
from pagina import views as core_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.cargarInicio, name='cargarInicio'),
    path('login/', views.cargarLogin, name='cargarLogin'),
    
    path('registro/', core_views.signup, name='signup'),
]