from django.shortcuts import render,redirect
from .models import Registro

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
                                            Tipo_Vinculacio=Tipo_Vinculacionhtml ,
                                            Dependencia = Dependenciahtml,
                                            Tipo_Vehiculo =Tipo_Vehiculohtml,
                                            Placa_Vehiculo = Placa_Vehiculohtml,
                                            Objeto_Visita= Objeto_Visitahtml,
                                            Observacion = Observacionhtml)
    return redirect('paginaprincipal')

   