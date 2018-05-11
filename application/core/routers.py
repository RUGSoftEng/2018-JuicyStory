from rest_framework import routers
from database.viewsets import InstagramUserViewSet, SelectedImageViewSet, ImageViewSet
from incoming.viewsets import IncomingViewSet

router = routers.DefaultRouter()
router.register(r'InstagramUser', InstagramUserViewSet)
router.register(r'SelectedImage', SelectedImageViewSet)
router.register(r'Image', ImageViewSet)
router.register(r'Incoming', IncomingViewSet, base_name="Incoming")
