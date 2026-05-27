import uuid

from django.db import models

from apps.organizations.models import (
    Organization
)


class AuditLog(models.Model):
    """
    Audit Trail

    Tracks every important action performed
    in the system.

    Examples:

    IMPORTED
    APPROVED
    REJECTED
    LOCKED
    UPDATED
    """

    class ActionType(models.TextChoices):

        CREATED = (
            "CREATED",
            "Created"
        )

        UPDATED = (
            "UPDATED",
            "Updated"
        )

        IMPORTED = (
            "IMPORTED",
            "Imported"
        )

        APPROVED = (
            "APPROVED",
            "Approved"
        )

        REJECTED = (
            "REJECTED",
            "Rejected"
        )

        LOCKED = (
            "LOCKED",
            "Locked"
        )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="audit_logs"
    )

    entity_type = models.CharField(
        max_length=100
    )

    entity_id = models.CharField(
        max_length=255
    )

    action = models.CharField(
        max_length=50,
        choices=ActionType.choices
    )

    old_data = models.JSONField(
        blank=True,
        null=True
    )

    new_data = models.JSONField(
        blank=True,
        null=True
    )

    performed_by = models.CharField(
        max_length=255
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    performed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        db_table = "audit_logs"

        ordering = [
            "-performed_at"
        ]

        indexes = [

            models.Index(
                fields=["action"]
            ),

            models.Index(
                fields=["entity_type"]
            ),

            models.Index(
                fields=["performed_by"]
            ),

            models.Index(
                fields=["performed_at"]
            )
        ]

    def __str__(self):

        return (
            f"{self.entity_type} "
            f"{self.action}"
        )