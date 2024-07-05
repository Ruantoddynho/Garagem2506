from rest_framework.viewsets import ModelViewSet

from core.models import Marca 
from core.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    query = Marca.objects.all()
    serializer_class = MarcaSerializer
    