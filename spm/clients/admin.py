from django.contrib import admin

from spm.clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "company", "created"]
    search_fields = ["name"]
    list_filter = ["company", "created"]