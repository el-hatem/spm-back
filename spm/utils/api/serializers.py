from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from spm.clients.models import Client
from spm.companies.models import Company
from spm.portal.choices import ApprovalModel, ApprovalStatus
from spm.portal.models import Approval


class ApprovalSerializerMixin(serializers.ModelSerializer):
    approval_status = serializers.SerializerMethodField()

    @extend_schema_field(serializers.ChoiceField(choices=ApprovalStatus.choices))
    def get_approval_status(self, obj):
        approval = Approval.objects.filter(object_id=obj.id, content_type__model=obj._meta.model_name).first()
        if approval:
            return approval.status
        return None


class CompanyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ClientObjectSerializer(serializers.ModelSerializer):
    company = CompanyObjectSerializer()

    class Meta:
        model = Client
        fields = "__all__"


CONTENT_OBJECT_SERIALIZERS = {
    ApprovalModel.COMPANY: CompanyObjectSerializer,
    ApprovalModel.CLIENT: ClientObjectSerializer,
}
