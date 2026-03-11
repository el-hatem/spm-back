from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import SAFE_METHODS, IsAdminUser

from spm.clients.api.v1.serializers import ClientDetailSerializer, ClientModifySerializer
from spm.clients.models import Client


class ClientViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ClientModifySerializer
    queryset = Client.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ("name", "email")
    filterset_fields = ("company",)
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ClientDetailSerializer
        return super().get_serializer_class()
