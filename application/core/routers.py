from rest_framework import routers
from database.viewsets import InstagramUserViewSet, SelectedImageViewSet, ImageViewSet
from incoming.viewsets import IncomingViewSet, LocationQueryViewSet

router = routers.DefaultRouter()
router.register(r'InstagramUser', InstagramUserViewSet)
router.register(r'SelectedImage', SelectedImageViewSet)
router.register(r'Image', ImageViewSet)
router.register(r'Incoming', IncomingViewSet, base_name="Incoming")
router.register(r'LocationQuery', LocationQueryViewSet,
                base_name="LocationQuery")
