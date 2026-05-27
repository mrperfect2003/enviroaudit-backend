import uuid

from django.db import models

from apps.organizations.models import Organization
from core.choices import (
    SourceType,
    ImportStatus
)


class DataSource(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="data_sources"
    )

    name = models.CharField(
        max_length=255
    )

    source_type = models.CharField(
        max_length=20,
        choices=SourceType.choices
    )

    description = models.TextField(
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
        db_table = "data_sources"

    def __str__(self):
        return self.name


class ImportJob(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="import_jobs"
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        related_name="imports"
    )

    file_name = models.CharField(
        max_length=255
    )

    uploaded_file = models.FileField(
        upload_to="imports/"
    )

    status = models.CharField(
        max_length=20,
        choices=ImportStatus.choices,
        default=ImportStatus.PENDING
    )

    total_rows = models.IntegerField(
        default=0
    )

    success_rows = models.IntegerField(
        default=0
    )

    failed_rows = models.IntegerField(
        default=0
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "import_jobs"
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.file_name


class RawRecord(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    import_job = models.ForeignKey(
        ImportJob,
        on_delete=models.CASCADE,
        related_name="raw_records"
    )

    row_number = models.IntegerField()

    raw_payload = models.JSONField()

    is_valid = models.BooleanField(
        default=True
    )

    validation_errors = models.JSONField(
        default=list,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "raw_records"

    def __str__(self):
        return f"{self.import_job.file_name} - {self.row_number}"
    
    status = models.CharField(
    max_length=50,
    default="PENDING"
)

error_message = models.TextField(
    null=True,
    blank=True
)