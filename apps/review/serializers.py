from rest_framework import serializers

from .models import (
    ReviewItem
)


class ReviewItemSerializer(
    serializers.ModelSerializer
):
    """
    Review Serializer

    Includes:
    - Review fields
    - Nested normalized record data
    """

    # -----------------------------------------
    # Normalized Record Fields
    # -----------------------------------------

    activity_type = serializers.CharField(
        source=(
            "normalized_record.activity_type"
        ),
        read_only=True
    )

    quantity = serializers.DecimalField(
        source=(
            "normalized_record.quantity"
        ),
        max_digits=18,
        decimal_places=4,
        read_only=True
    )

    normalized_unit = serializers.CharField(
        source=(
            "normalized_record.normalized_unit"
        ),
        read_only=True
    )

    scope = serializers.CharField(
        source=(
            "normalized_record.scope"
        ),
        read_only=True
    )

    class Meta:

        model = ReviewItem

        fields = [

            # Review Fields
            "id",
            "status",
            "analyst_notes",
            "reviewed_by",
            "reviewed_at",
            "created_at",
            "updated_at",

            # FK
            "normalized_record",

            # Nested Normalized Data
            "activity_type",
            "quantity",
            "normalized_unit",
            "scope",
        ]