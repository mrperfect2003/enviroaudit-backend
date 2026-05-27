from rest_framework import (
    viewsets
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from core.pagination import (
    DefaultPagination
)

from .models import (
    AuditLog
)

from .serializers import (
    AuditLogSerializer
)


class AuditLogViewSet(
    viewsets.ReadOnlyModelViewSet
):
    """
    Audit Trail API

    Supports:

    Search
    Ordering
    Pagination
    """

    queryset = (
        AuditLog.objects.all()
    )

    serializer_class = (
        AuditLogSerializer
    )

    pagination_class = (
        DefaultPagination
    )

    filter_backends = [
        SearchFilter,
        OrderingFilter
    ]

    search_fields = [
        "entity_type",
        "performed_by",
        "action"
    ]

    ordering_fields = [
        "performed_at",
        "action"
    ]

    ordering = [
        "-performed_at"
    ]