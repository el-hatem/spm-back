from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from spm.portal.models import Approval
from spm.users.api.v1.serializers import UserDetailSerializer
from spm.portal.api.validators import ApprovalValidator
from spm.utils.api.serializers import CONTENT_OBJECT_SERIALIZERS



class CreateApprovalSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(slug_field="model", queryset=ContentType.objects.all())

    class Meta:
        model = Approval
        fields = ("content_type", "object_id")
        validators = [ApprovalValidator()]




class ApprovalDetailSerializer(serializers.ModelSerializer):
    reviewer = UserDetailSerializer(read_only=True)
    content_type = serializers.SlugRelatedField(slug_field="model", queryset=ContentType.objects.all())
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Approval
        fields = "__all__"

    @extend_schema_field(serializers.DictField)
    def get_content_object(self, obj):
        serializer_class = CONTENT_OBJECT_SERIALIZERS.get(obj.content_type.model)
        if serializer_class:
            return serializer_class(obj.content_object, context=self.context, read_only=True).data

class ApproveSerializer(serializers.Serializer):
    note = serializers.CharField(required=False, allow_blank=True)