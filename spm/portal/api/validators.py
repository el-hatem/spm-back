from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ApprovalValidator:
    requires_context = True
    message = _("invalid sharable object")

    def __call__(self, attr: str, serializer: serializers.ModelSerializer):
        content_type = attr.get("content_type", None)
        object_id = attr.get("object_id", None)

        content_type = ContentType.objects.get(model=content_type.model)
        Model = content_type.model_class()

        if not Model.objects.filter(pk=object_id).exists():
            raise serializers.ValidationError({"object_id": self.message})
