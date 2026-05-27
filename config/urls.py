from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Organizations APIs
    path(
        "api/organizations/",
        include("apps.organizations.urls")
    ),

    # Ingestion APIs
    path(
        "api/ingestion/",
        include("apps.ingestion.urls")
    ),

    # Review APIs
    path(
        "api/review/",
        include("apps.review.urls")
    ),

    # Audit APIs
    path(
        "api/audit/",
        include("apps.audit.urls")
    ),
]

# Media Files
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )