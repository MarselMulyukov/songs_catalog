from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import AlbumViewSet, MusicPerformerViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Songs_catalog API",
        default_version='v1',
        description="Документация для приложения каталог песен",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'
    ),
    re_path(
        r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path("", include(router.urls)),
]
