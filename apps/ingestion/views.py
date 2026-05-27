from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.organizations.models import (
    Organization
)

from apps.ingestion.services.import_service import (
    ImportService
)

from core.pagination import (
    DefaultPagination
)

from .models import (
    DataSource,
    ImportJob,
    RawRecord
)

from .serializers import (
    DataSourceSerializer,
    ImportJobSerializer,
    RawRecordSerializer
)


class DataSourceViewSet(
    viewsets.ModelViewSet
):

    queryset = DataSource.objects.all()

    serializer_class = (
        DataSourceSerializer
    )

    pagination_class = (
        DefaultPagination
    )

    filter_backends = [
        SearchFilter
    ]

    search_fields = [
        "name",
        "source_type"
    ]


class ImportJobViewSet(
    viewsets.ModelViewSet
):

    queryset = ImportJob.objects.all()

    serializer_class = (
        ImportJobSerializer
    )

    pagination_class = (
        DefaultPagination
    )


class RawRecordViewSet(
    viewsets.ReadOnlyModelViewSet
):

    queryset = RawRecord.objects.all()

    serializer_class = (
        RawRecordSerializer
    )

    pagination_class = (
        DefaultPagination
    )


class CSVUploadView(APIView):

    def post(self, request):

        organization_id = request.data.get(
            "organization_id"
        )

        source_id = request.data.get(
            "source_id"
        )

        uploaded_file = request.FILES.get(
            "file"
        )

        uploaded_by = request.data.get(
            "uploaded_by",
            "System"
        )

        if not organization_id:
            return Response(
                {
                    "message":
                    "organization_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not source_id:
            return Response(
                {
                    "message":
                    "source_id is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not uploaded_file:
            return Response(
                {
                    "message":
                    "CSV file is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            organization = (
                Organization.objects.get(
                    id=organization_id
                )
            )

            source = (
                DataSource.objects.get(
                    id=source_id
                )
            )

            job = (
                ImportService.process_csv(
                    organization=organization,
                    source=source,
                    uploaded_file=uploaded_file,
                    uploaded_by=uploaded_by
                )
            )

            return Response(
                {
                    "message":
                    "File processed successfully",
                    "import_job_id":
                    str(job.id),
                    "status":
                    job.status
                },
                status=status.HTTP_201_CREATED
            )

        except Organization.DoesNotExist:

            return Response(
                {
                    "message":
                    "Organization not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except DataSource.DoesNotExist:

            return Response(
                {
                    "message":
                    "Data source not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:

            return Response(
                {
                    "message":
                    str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )