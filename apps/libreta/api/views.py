from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import PersonaSerializer, DireccionSerializer
from ..models import Persona, Direccion



from rest_framework.response import Response


class PersonaViewSet(viewsets.ModelViewSet):
    model = Persona
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True).data
        return Response(data)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
        
    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Persona no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=False, methods=['post'])
    def eliminar_todo(self, request):
        user_ids = request.data.get('user_ids')
        data = Persona.objects.filter(id__in=user_ids)
        data.delete()
        return Response({'message':'Personas eliminada correctamente!'}, status=status.HTTP_200_OK) 
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Persona registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Persona actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Persona eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Persona no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)



class DireccionViewSet(viewsets.ModelViewSet):
    model = Direccion
    serializer_class = DireccionSerializer
    queryset = Direccion.objects.all()

    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True).data
        return Response(data)
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
        
    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Direccion no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Direccion registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Direccion actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Direccion eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Direccion no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)