from rest_framework.viewsets import ModelViewSet

from core.models import Cor
from core.serializers import CorSerializer

class CorViewSet(ModelViewSet):
    query = Cor.objects.all()
    serializer_class = CorSerializer
    