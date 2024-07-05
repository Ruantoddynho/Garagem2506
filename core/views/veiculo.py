from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    query = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    