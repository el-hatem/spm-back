from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from spm.companies.models import Company
from spm.portal.choices import ApprovalModel, ApprovalStatus
from spm.portal.models import Approval


class ApprovalSerializerMixin(serializers.ModelSerializer):
    approval_status = serializers.SerializerMethodField()

    @extend_schema_field(serializers.ChoiceField(choices=ApprovalStatus.choices))
    def get_approval_status(self, obj):
        approval = Approval.objects.filter(object_id=obj.id).first()
        if approval:
            return approval.status
        return None


class CompanyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


CONTENT_OBJECT_SERIALIZERS = {
    ApprovalModel.COMPANY: CompanyObjectSerializer,
}
