from rest_framework import routers
from authentication.viewsets import InstagramUserViewSet, SelectedImageViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r'InstagramUser', InstagramUserViewSet)
router.register(r'SelectedImage', SelectedImageViewSet)
router.register(r'Image', ImageViewSet)