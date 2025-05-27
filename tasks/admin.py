from django.contrib import admin
from .models import Task
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "completed",
        "user",
        "created_at",
        "updated_at",
    )
    list_filter = ("completed", "user")
    search_fields = ("title", "description", "user__email")
    ordering = ("-created_at",)


admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)
