from rest_framework import routers
from database.viewsets import SelectedImageViewSet
from incoming.viewsets import (IncomingViewSet, LocationQueryViewSet)

''' Registering all the relevant routers to different API endpoints '''
router = routers.DefaultRouter()
router.register(r'SelectedImage', SelectedImageViewSet, base_name="SelectedImage")
router.register(r'Incoming', IncomingViewSet, base_name="Incoming")
router.register(r'LocationQuery', LocationQueryViewSet, base_name="LocationQuery")