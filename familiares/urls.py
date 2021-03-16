from django.urls import path
from . import views
from .views import FamiliaresList, FamiliaresDetails

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('editar/<id>', views.editar, name='editar'),
    path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('crear/', views.crear, name='crear'),
    path('api/list', FamiliaresList.as_view(), name='list'),
    path('api/list/<pk>', FamiliaresDetails.as_view(), name='details'),

    ]

