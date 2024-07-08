from django.shortcuts import render,redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Registro
from django.http import HttpResponseBadRequest
from datetime import datetime


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
    listarregistros= Registro.objects.all()
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
        fecha_salida = datetime.now().strftime('%Y-%m-%d')

        # Actualizar la fecha de salida
        salida.Fecha_Salida = fecha_salida
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

