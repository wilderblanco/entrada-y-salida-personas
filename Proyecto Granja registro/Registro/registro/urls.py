from django.urls import path
from . import views

urlpatterns = [
 path('',views.Pagina_Principal, name='paginaprincipal'),
 path('crearregistro/', views.Registrarnuevapersona, name='crearregistronuevo'),
 path('guardarregistro/',views.guardarregistro, name='guardarregistro'),
 path('registroexistente/',views.registroexistente, name="existente"),
 path('irregistrarsalida/<id>', views.irregistrarsalida, name="irregistrarsalida"),
 path('registrarsalida/', views.listarregistrossalida, name='registrosalida'),
 path('actualizarregistro/', views.actualizarsalida, name="actualizar"),
 path('listado/', views.listaregistros, name="listaregistros"),
 path('logout/', views.exit , name="exit"),
 path('capture_photo/', views.capture_photo, name='capture_photo'),
 ]
