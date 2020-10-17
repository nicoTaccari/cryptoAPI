from rest_framework import viewsets
from . import models
from . import serializers


class CoinViewset(viewsets.ModelViewSet):
    queryset = models.Coin.objects.all()
    serializer_class = serializers.CoinSerializer
