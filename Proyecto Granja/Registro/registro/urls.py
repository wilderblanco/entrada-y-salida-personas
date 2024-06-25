from django.urls import path
from . import views

urlpatterns = [
 path('',views.Pagina_Principal, name='paginaprincipal'),
 path('crearregistro/', views.Registrarnuevapersona, name='crearregistronuevo'),
 path('guardarregistro/',views.guardarregistro, name='guardarregistro')
]
