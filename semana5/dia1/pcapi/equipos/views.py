from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Empleado,Equipo
from .serializers import EmpleadoSerializer,EquipoSerializer

@api_view(['GET'])
def index(request):
    data={'mensaje':'hola mundo json'}
    return Response(data)

@api_view(['GET'])
def empleados(request):
    listaEmpleados=Empleado.objects.all()
    print(listaEmpleados)
    #dataEmpleados=[]
    #for d in listaEmpleados:
     #   dataEmpleados.append({
      #      'nombre':d.nombre,
       #     'email':d.email
        #})

    serEmpleados=EmpleadoSerializer(listaEmpleados,many=True)

    return Response({'status':'OK','data':serEmpleados.data})

@api_view(['POST'])
def crearEmpleado(request):
    """ nuevoEmpleado=Empleado()
    nuevoEmpleado.nombre=request.data['nombre']
    nuevoEmpleado.email=request.data['email']
    nuevoEmpleado.save()

    dataNuevoEmpleado={
        'id':nuevoEmpleado.id,
        'nombre':nuevoEmpleado.nombre,
        'email':nuevoEmpleado.email
    } """
    serEmpleado=EmpleadoSerializer(data=request.data)
    serEmpleado.is_valid(raise_exception=True)

    nuevoEmpleado=serEmpleado.save()

    return Response({'status':'ok','data':EmpleadoSerializer(nuevoEmpleado).data})

@api_view(['GET','POST'])
def equipos(request):
    if request.method=='GET':
        #retornar los equipos
        dataEquipos=Equipo.objects.all()
        serEquipos=EquipoSerializer(dataEquipos,many=True)
        return Response(serEquipos.data)
    elif request.method=='POST':
        serEquipo = EquipoSerializer(data=request.data)
        if serEquipo.is_valid():
            serEquipo.save()
            return Response(serEquipo.data)
        else:
            return Response(serEquipo.errors)
