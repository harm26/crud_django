from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('editar/<id>', views.editar, name='editar'),
    path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('crear/', views.crear, name='crear'),

]