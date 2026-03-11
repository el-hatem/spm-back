import logging

from django.utils import timezone
from viewflow.fsm import State

from spm.portal.choices import ApprovalStatus

logger = logging.getLogger(__name__)


class ApprovalFlow:
    status = State(ApprovalStatus.choices, default=ApprovalStatus.PENDING)

    def __init__(self, approval):
        self.approval = approval

    @status.setter()
    def _set_status(self, value):
        self.approval.status = value

    @status.getter()
    def _get_status(self):
        return self.approval.status

    @status.on_success()
    def _on_transition_success(self, descriptor, source, target, *args, **kwargs):
        self.approval.save()

    @status.transition(
        source=[ApprovalStatus.PENDING],
        target=ApprovalStatus.APPROVED,
    )
    def approve(self, reviewer=None, note=""):
        self.approval.reviewer = reviewer
        self.approval.note = note
        self.approval.reviewed_at = timezone.now()
        logger.info(f"Approve {self.approval}")

    @status.transition(
        source=[ApprovalStatus.PENDING],
        target=ApprovalStatus.REJECTED,
    )
    def reject(self, reviewer=None, note=""):
        self.approval.reviewer = reviewer
        self.approval.note = note
        self.approval.reviewed_at = timezone.now()
        logger.info(f"Reject {self.approval}")
