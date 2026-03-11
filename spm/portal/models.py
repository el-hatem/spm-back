from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.models import TimeStampedModel

from spm.portal.choices import ApprovalStatus


class Approval(TimeStampedModel):
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="approvals", null=True, blank=True
    )
    note = models.TextField(default="")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    status = models.CharField(max_length=20, choices=ApprovalStatus.choices, default=ApprovalStatus.PENDING)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ["-created"]