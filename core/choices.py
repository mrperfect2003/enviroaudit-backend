from django.db import models


class SourceType(models.TextChoices):
    SAP = "SAP", "SAP"
    UTILITY = "UTILITY", "Utility"
    TRAVEL = "TRAVEL", "Travel"


class ImportStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PROCESSING = "PROCESSING", "Processing"
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"


class ScopeCategory(models.TextChoices):
    SCOPE_1 = "SCOPE_1", "Scope 1"
    SCOPE_2 = "SCOPE_2", "Scope 2"
    SCOPE_3 = "SCOPE_3", "Scope 3"


class ReviewStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    LOCKED = "LOCKED", "Locked"