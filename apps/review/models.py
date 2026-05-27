import uuid

from django.db import models

from apps.normalization.models import (
    NormalizedRecord
)

from core.choices import (
    ReviewStatus
)


class ReviewItem(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    normalized_record = models.OneToOneField(
        NormalizedRecord,
        on_delete=models.CASCADE,
        related_name="review"
    )

    status = models.CharField(
        max_length=20,
        choices=ReviewStatus.choices,
        default=ReviewStatus.PENDING
    )

    analyst_notes = models.TextField(
        blank=True,
        null=True
    )

    reviewed_by = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    reviewed_at = models.DateTimeField(
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
        db_table = "review_items"

    def __str__(self):
        return f"{self.id} - {self.status}"