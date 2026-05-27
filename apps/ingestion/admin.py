from django.contrib import admin

from .models import (
    DataSource,
    ImportJob,
    RawRecord
)


admin.site.register(DataSource)
admin.site.register(ImportJob)
admin.site.register(RawRecord)