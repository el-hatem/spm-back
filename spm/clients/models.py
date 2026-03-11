from django.db import models
from django_extensions.db.models import TimeStampedModel


class Client(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="clients")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name
