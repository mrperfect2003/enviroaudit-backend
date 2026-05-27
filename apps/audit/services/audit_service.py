from apps.audit.models import (
    AuditLog
)


class AuditService:
    """
    Centralized Audit Logger

    Every important business action
    should pass through this service.
    """

    @staticmethod
    def log(
        organization,
        entity_type,
        entity_id,
        action,
        performed_by,
        old_data=None,
        new_data=None,
        remarks=None
    ):

        return AuditLog.objects.create(
            organization=organization,

            entity_type=entity_type,

            entity_id=str(
                entity_id
            ),

            action=action,

            old_data=old_data,

            new_data=new_data,

            performed_by=performed_by,

            remarks=remarks
        )

    @staticmethod
    def log_import(
        organization,
        entity_id,
        performed_by,
        payload=None
    ):

        return AuditService.log(
            organization=organization,

            entity_type="RawRecord",

            entity_id=entity_id,

            action=AuditLog.ActionType.IMPORTED,

            performed_by=performed_by,

            new_data=payload
        )

    @staticmethod
    def log_approval(
        organization,
        review_id,
        performed_by,
        notes=None
    ):

        return AuditService.log(
            organization=organization,

            entity_type="ReviewItem",

            entity_id=review_id,

            action=AuditLog.ActionType.APPROVED,

            performed_by=performed_by,

            remarks=notes
        )

    @staticmethod
    def log_rejection(
        organization,
        review_id,
        performed_by,
        notes=None
    ):

        return AuditService.log(
            organization=organization,

            entity_type="ReviewItem",

            entity_id=review_id,

            action=AuditLog.ActionType.REJECTED,

            performed_by=performed_by,

            remarks=notes
        )

    @staticmethod
    def log_lock(
        organization,
        review_id,
        performed_by
    ):

        return AuditService.log(
            organization=organization,

            entity_type="ReviewItem",

            entity_id=review_id,

            action=AuditLog.ActionType.LOCKED,

            performed_by=performed_by
        )