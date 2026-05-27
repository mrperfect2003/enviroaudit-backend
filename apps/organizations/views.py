from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from core.pagination import DefaultPagination

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = Organization.objects.all()

    serializer_class = OrganizationSerializer

    pagination_class = DefaultPagination

    filter_backends = [SearchFilter]

    search_fields = [
        "name",
        "industry",
        "country"
    ]