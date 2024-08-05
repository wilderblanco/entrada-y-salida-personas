import base64
import json
from django.shortcuts import render,redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Registro
from django.http import HttpResponseBadRequest, JsonResponse
from datetime import datetime
import os

# Create your views here.
def Pagina_Principal(request):
    return render(request,'Paginaprincipal.html')

def Registrarnuevapersona(request):
    return render(request, 'Registrarnuevoingreso.html')

def guardarregistro(request):
    Tipo_Documentohtml = request.POST['tipodocumento']
    Numerohtml = request.POST['documento']   
    Nombreshtml = request.POST['nombres'] 
    Apellidoshtml = request.POST['apellidos']  
    Lugar_Procedenciahtml = request.POST['lugarprocedencia']
    Correohtml = request.POST['Correo']   
    Telefonohtml = request.POST['telefono']
    Fecha_Ingresohtml = request.POST['entrada']
    Fecha_Salidahtml = request.POST['salida']
    Tipo_Vinculacionhtml = request.POST['tipovinculacion'] 
    Dependenciahtml = request.POST['dependencia']
    Tipo_Vehiculohtml = request.POST['tipovehiculo']
    Placa_Vehiculohtml = request.POST['placa']
    Objeto_Visitahtml = request.POST['objetivovisita']
    Observacionhtml = request.POST['observacion']
    modeloregistro=Registro.objects.create(Tipo_Documento=Tipo_Documentohtml,
                                            Numero=Numerohtml,
                                            Nombres =Nombreshtml,
                                            Apellidos = Apellidoshtml , 
                                            Lugar_Procedencia =Lugar_Procedenciahtml,
                                            Correo = Correohtml,
                                            Telefono = Telefonohtml ,
                                            Fecha_Ingreso = Fecha_Ingresohtml,
                                            Fecha_Salida = Fecha_Salidahtml,
                                            Tipo_Vinculacion=Tipo_Vinculacionhtml ,
                                            Dependencia = Dependenciahtml,
                                            Tipo_Vehiculo =Tipo_Vehiculohtml,
                                            Placa_Vehiculo = Placa_Vehiculohtml,
                                            Objeto_Visita= Objeto_Visitahtml,
                                            Observacion = Observacionhtml)
    return redirect('paginaprincipal')


def registroexistente(request):
    return render(request, 'Registrarexistente.html')

def listarregistrossalida(request):
    listarregistros = Registro.objects.filter(Actualizado=False)
    return render(request, 'Registrarsalida.html', {'listarregistros': listarregistros})

def irregistrarsalida(request,id):
    salida=Registro.objects.get(id=id)
    return render(request, 'Registrarsalidactualizar.html',{'salida': salida})


def actualizarsalida(request):
    if request.method == 'POST':
        idhtml = request.POST.get('id')
        
        if not idhtml:
            return HttpResponseBadRequest("Falta el ID.")

        # Obtener el registro, si no existe, devolverá un 404
        salida = get_object_or_404(Registro, id=idhtml)

        # Obtener la fecha actual
        fecha_salida = datetime.now()

        # Actualizar la fecha de salida y el estado
        salida.Fecha_Salida = fecha_salida
        salida.Actualizado = True
        salida.save()

        return redirect('registrosalida')

    return HttpResponseBadRequest("Método no permitido.")


@login_required
def listaregistros(request):
    listarregistros= Registro.objects.all()
    return render(request, 'listaregistrosguardados.html', {'listarregistros': listarregistros})

def exit(request):
    logout(request)
    return redirect('paginaprincipal')

def capture_photo(request):
    if request.method == 'POST':
        # Recibir los datos JSON del cuerpo de la solicitud
        data = json.loads(request.body)
        image_data = data.get('image_data', None)
        
        if image_data:
            # Aquí puedes procesar la imagen recibida (guardarla, procesarla, etc.)
            # Ejemplo: Guardar la imagen en el sistema de archivos
            with open('captured_photo.png', 'wb') as f:
                f.write(base64.b64decode(image_data.split(',')[1]))  # Decodificar la imagen base64
            
            return JsonResponse({'message': 'Foto recibida y procesada correctamente.'})
        else:
            return JsonResponse({'error': 'No se recibió ninguna imagen.'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)