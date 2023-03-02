from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, MusicPerformerViewSet

router = DefaultRouter()


router.register(
    'albums',
    AlbumViewSet,
    basename='albums',
)

router.register(
    'music-performers',
    MusicPerformerViewSet,
    basename='music-performers',
)


urlpatterns = [
    path("", include(router.urls)),
]