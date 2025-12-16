from rest_framework import viewsets
from medicos.models import Medico
from .serializers import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset= Medico.objects.all()
    serializer_class = MedicoSerializer
    
    
    
