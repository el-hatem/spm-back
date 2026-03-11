from rest_framework import serializers

from spm.companies.models import Company
from spm.portal.choices import ApprovalModel
from spm.utils.api.serializers import ApprovalSerializerMixin
from spm.utils.functions import create_approval_object


class CompanySerializer(ApprovalSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

    def create(self, validated_data):
        obj = super().create(validated_data)
        create_approval_object(ApprovalModel.COMPANY, obj.id)
        return obj
