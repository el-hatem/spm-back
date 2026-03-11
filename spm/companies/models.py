from django.db import models
from django_extensions.db.models import TimeStampedModel

from spm.companies.choices import CompanyType


class Company(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    company_type = models.CharField(max_length=50, choices=CompanyType.choices)
    data = models.JSONField(blank=True, default=dict)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
