from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "entity_type",
        "action",
        "performed_by",
        "performed_at"
    )

    search_fields = (
        "entity_type",
        "performed_by"
    )

    list_filter = (
        "action",
    )