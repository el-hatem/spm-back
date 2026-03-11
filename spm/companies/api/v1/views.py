from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser

from spm.companies.models import Company
from spm.companies.api.v1.serializers import CompanySerializer



class CompanyViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ("name",)
    permission_classes = [IsAdminUser]
    

    