import logging

from spm.portal.api.v1.serializers import CreateApprovalSerializer

logger = logging.getLogger(__name__)


def create_approval_object(model, object_id):
    try:
        serializer = CreateApprovalSerializer(data={"content_type": model, "object_id": object_id})
        serializer.is_valid(raise_exception=True)
        approval = serializer.save()
        return approval
    except Exception as e:
        # Log the error or handle it as needed
        logger.error(f"Error creating approval object: {e}")
        raise
