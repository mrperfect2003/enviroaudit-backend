from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "industry",
        "country",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "industry",
        "country",
    )

    list_filter = (
        "country",
        "is_active",
    )