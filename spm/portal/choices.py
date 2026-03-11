from django.db import models
from django.utils.translation import gettext_lazy as _


class ApprovalModel(models.TextChoices):
    COMPANY = "company", _("Company")
    

class ApprovalStatus(models.TextChoices):
    PENDING = "pending", _("Pending")
    APPROVED = "approved", _("Approved")
    REJECTED = "rejected", _("Rejected")