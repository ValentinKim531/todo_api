from django.contrib import admin
from .models import AstanaHubCompany


@admin.register(AstanaHubCompany)
class AstanaHubCompanyAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "date_start",
        "date_end",
        "bin",
        "status",
        "name",
    )
    search_fields = ("name",)
    ordering = ("date_start",)
