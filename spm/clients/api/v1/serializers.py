from rest_framework import serializers

from spm.clients.models import Client
from spm.portal.choices import ApprovalModel
from spm.utils.api.serializers import ApprovalSerializerMixin, CompanyObjectSerializer
from spm.utils.functions import create_approval_object


class ClientModifySerializer(ApprovalSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        obj = super().create(validated_data)
        create_approval_object(ApprovalModel.CLIENT, obj.id)
        return obj


class ClientDetailSerializer(ApprovalSerializerMixin, serializers.ModelSerializer):
    company = CompanyObjectSerializer(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"