from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    DataSourceViewSet,
    ImportJobViewSet,
    RawRecordViewSet,
    CSVUploadView,
)

router = DefaultRouter()

router.register(
    r"data-sources",
    DataSourceViewSet,
    basename="data-sources"
)

router.register(
    r"imports",
    ImportJobViewSet,
    basename="imports"
)

router.register(
    r"raw-records",
    RawRecordViewSet,
    basename="raw-records"
)

urlpatterns = router.urls + [
    path(
        "upload/",
        CSVUploadView.as_view(),
        name="csv-upload"
    ),
]