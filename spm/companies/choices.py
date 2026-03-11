from django.db import models
from django.utils.translation import gettext_lazy as _


class CompanyType(models.TextChoices):
    SMALL_BUSINESS = "small_business", _("Small Business")
    STARTUP = "startup", _("Startup")
    CORPORATION = "corporation", _("Corporation")
