from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from spm.portal.api.v1.serializers import ApprovalDetailSerializer
from spm.portal.mixins.v1.views import ApprovalFlowMixin
from spm.portal.models import Approval


class ApprovalViewSet(mixins.ListModelMixin, ApprovalFlowMixin, viewsets.GenericViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalDetailSerializer
    permission_classes = [IsAdminUser]
