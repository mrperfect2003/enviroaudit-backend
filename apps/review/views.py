from django.utils import timezone

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.choices import (
    ReviewStatus
)

from apps.audit.services.audit_service import (
    AuditService
)

from .models import (
    ReviewItem
)

from .serializers import (
    ReviewItemSerializer
)


class ReviewItemViewSet(
    viewsets.ModelViewSet
):
    """
    Review Workflow

    PENDING
        ↓
    APPROVED / REJECTED
        ↓
    LOCKED
    """

    queryset = ReviewItem.objects.all()

    serializer_class = (
        ReviewItemSerializer
    )

    @action(
        detail=True,
        methods=["post"]
    )
    def approve(
        self,
        request,
        pk=None
    ):
        """
        Approve review item
        """

        review = self.get_object()

        if review.status == ReviewStatus.LOCKED:
            return Response(
                {
                    "message":
                    "Locked records cannot be modified"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        review.status = (
            ReviewStatus.APPROVED
        )

        review.reviewed_by = (
            request.data.get(
                "reviewed_by",
                "System"
            )
        )

        review.analyst_notes = (
            request.data.get(
                "analyst_notes",
                ""
            )
        )

        review.reviewed_at = (
            timezone.now()
        )

        review.save()

        # Audit Log
        AuditService.log_approval(
            organization=review.normalized_record.organization,
            review_id=review.id,
            performed_by=review.reviewed_by,
            notes=review.analyst_notes
        )

        return Response(
            {
                "message":
                "Record approved successfully",
                "status":
                review.status
            },
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def reject(
        self,
        request,
        pk=None
    ):
        """
        Reject review item
        """

        review = self.get_object()

        if review.status == ReviewStatus.LOCKED:
            return Response(
                {
                    "message":
                    "Locked records cannot be modified"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        review.status = (
            ReviewStatus.REJECTED
        )

        review.reviewed_by = (
            request.data.get(
                "reviewed_by",
                "System"
            )
        )

        review.analyst_notes = (
            request.data.get(
                "analyst_notes",
                ""
            )
        )

        review.reviewed_at = (
            timezone.now()
        )

        review.save()

        # Audit Log
        AuditService.log_rejection(
            organization=review.normalized_record.organization,
            review_id=review.id,
            performed_by=review.reviewed_by,
            notes=review.analyst_notes
        )

        return Response(
            {
                "message":
                "Record rejected successfully",
                "status":
                review.status
            },
            status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def lock(
        self,
        request,
        pk=None
    ):
        """
        Lock record for audit.
        Once locked, it cannot be modified.
        """

        review = self.get_object()

        if review.status == ReviewStatus.LOCKED:
            return Response(
                {
                    "message":
                    "Record already locked"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        review.status = (
            ReviewStatus.LOCKED
        )

        review.save()

        # Audit Log
        AuditService.log_lock(
            organization=review.normalized_record.organization,
            review_id=review.id,
            performed_by=request.data.get(
                "performed_by",
                "System"
            )
        )

        return Response(
            {
                "message":
                "Record locked successfully",
                "status":
                review.status
            },
            status=status.HTTP_200_OK
        )