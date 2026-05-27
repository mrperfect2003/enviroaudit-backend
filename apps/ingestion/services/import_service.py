import pandas as pd

from apps.ingestion.models import (
    ImportJob,
    RawRecord,
)

from apps.normalization.services.normalizer import (
    Normalizer,
)

from apps.review.models import (
    ReviewItem,
)

from apps.audit.services.audit_service import (
    AuditService,
)


class ImportService:
    """
    Handles complete ingestion workflow:

    CSV Upload
        ↓
    Import Job
        ↓
    Raw Records
        ↓
    Normalization
        ↓
    Review Queue
        ↓
    Audit Trail
    """

    @staticmethod
    def save_raw_records(
        import_job,
        records
    ):
        """
        Bulk save raw records for better performance.
        """

        objects = []

        for index, row in enumerate(
            records,
            start=1
        ):

            objects.append(
                RawRecord(
                    import_job=import_job,
                    row_number=index,
                    raw_payload=row
                )
            )

        RawRecord.objects.bulk_create(
            objects
        )

        return len(objects)

    @staticmethod
    def process_csv(
        organization,
        source,
        uploaded_file,
        uploaded_by="System"
    ):
        """
        Complete ingestion pipeline.

        CSV
            ↓
        ImportJob
            ↓
        RawRecord
            ↓
        NormalizedRecord
            ↓
        ReviewItem
            ↓
        AuditLog
        """

        job = ImportJob.objects.create(
            organization=organization,
            source=source,
            status="PROCESSING"
        )

        try:

            # ----------------------------------
            # Read CSV
            # ----------------------------------

            dataframe = pd.read_csv(
                uploaded_file
            )

            records = (
                dataframe.to_dict(
                    orient="records"
                )
            )

            # ----------------------------------
            # Save Raw Records
            # ----------------------------------

            ImportService.save_raw_records(
                import_job=job,
                records=records
            )

            raw_records = (
                RawRecord.objects.filter(
                    import_job=job
                ).order_by(
                    "row_number"
                )
            )

            # ----------------------------------
            # Normalize Records
            # ----------------------------------

            for raw_record in raw_records:

                payload = (
                    raw_record.raw_payload
                )

                normalized_record = (
                    Normalizer.normalize(
                        organization=organization,
                        source=source,
                        import_job=job,
                        raw_record=raw_record,
                        activity_type=payload.get(
                            "activity_type",
                            ""
                        ),
                        quantity=payload.get(
                            "quantity",
                            0
                        ),
                        unit=payload.get(
                            "unit",
                            ""
                        )
                    )
                )

                # ----------------------------------
                # Create Review Item
                # ----------------------------------

                ReviewItem.objects.create(
                    normalized_record=
                    normalized_record
                )

                # ----------------------------------
                # Audit Log
                # ----------------------------------

                AuditService.log_import(
                    organization=organization,
                    entity_id=raw_record.id,
                    performed_by=uploaded_by,
                    payload=payload
                )

            # ----------------------------------
            # Mark Job Completed
            # ----------------------------------

            job.status = "COMPLETED"
            job.save()

            return job

        except Exception as e:

            # ----------------------------------
            # Mark Job Failed
            # ----------------------------------

            job.status = "FAILED"
            job.error_message = str(e)
            job.save()

            raise e