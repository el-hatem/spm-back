from django.contrib import admin

from spm.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "company_type", "created"]
    search_fields = ["name"]
    list_filter = ["company_type", "created"]