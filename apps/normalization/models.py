import uuid

from django.db import models

from apps.organizations.models import Organization
from apps.ingestion.models import (
    DataSource,
    ImportJob,
    RawRecord
)

from core.choices import (
    ScopeCategory
)


class NormalizedRecord(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="normalized_records"
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    import_job = models.ForeignKey(
        ImportJob,
        on_delete=models.CASCADE
    )

    raw_record = models.OneToOneField(
        RawRecord,
        on_delete=models.CASCADE
    )

    activity_type = models.CharField(
        max_length=100
    )

    scope = models.CharField(
        max_length=20,
        choices=ScopeCategory.choices
    )

    quantity = models.DecimalField(
        max_digits=18,
        decimal_places=4
    )

    normalized_unit = models.CharField(
        max_length=50
    )

    billing_period_start = models.DateField(
        null=True,
        blank=True
    )

    billing_period_end = models.DateField(
        null=True,
        blank=True
    )

    source_reference = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    is_flagged = models.BooleanField(
        default=False
    )

    flag_reason = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "normalized_records"

    def __str__(self):
        return f"{self.activity_type} - {self.quantity}"