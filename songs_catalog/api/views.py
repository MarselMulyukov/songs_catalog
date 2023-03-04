from .models import Album, MusicPerformer
from .serializers import (
    AllAlbumsSerializer,
    AllPerformersSerializer,
    AlbumSerializer,
    PerformerSerializer
)
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class AlbumViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AllAlbumsSerializer
        if self.action == 'retrieve':
            return AlbumSerializer


class MusicPerformerViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = MusicPerformer.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AllPerformersSerializer
        if self.action == 'retrieve':
            return PerformerSerializer
