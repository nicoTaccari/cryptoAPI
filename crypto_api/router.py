from core.viewsets import CoinViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('coin', CoinViewset)
