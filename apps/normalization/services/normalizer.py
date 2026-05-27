from apps.normalization.models import (
    NormalizedRecord
)

from .unit_converter import (
    UnitConverter
)

from .scope_mapper import (
    ScopeMapper
)


class Normalizer:
    """
    ESG Record Normalization Service

    Responsibilities:
    1. Normalize units
    2. Convert quantities
    3. Map Scope 1 / Scope 2 / Scope 3
    4. Detect suspicious records
    5. Create NormalizedRecord
    """

    @staticmethod
    def normalize(
        organization,
        source,
        import_job,
        raw_record,
        activity_type,
        quantity,
        unit
    ):
        """
        Normalize a raw ESG record.

        Flow:
        RawRecord
            ↓
        Normalize Unit
            ↓
        Convert Quantity
            ↓
        Map ESG Scope
            ↓
        Detect Suspicious Records
            ↓
        Save NormalizedRecord
        """

        # ----------------------------------
        # Normalize Unit
        #
        # Example:
        # liter   -> liter
        # liters  -> liter
        # kwh     -> kWh
        # tonne   -> kg
        # ----------------------------------
        normalized_unit = (
            UnitConverter.normalize_unit(
                unit
            )
        )

        # ----------------------------------
        # Convert Quantity
        #
        # Examples:
        # 2 TONNE -> 2000 KG
        # 1 MWH   -> 1000 KWH
        # ----------------------------------
        normalized_quantity = (
            UnitConverter.convert_quantity(
                quantity,
                unit
            )
        )

        # ----------------------------------
        # ESG Scope Mapping
        #
        # Diesel Fuel -> Scope 1
        # Electricity -> Scope 2
        # Flight      -> Scope 3
        # ----------------------------------
        scope = (
            ScopeMapper.get_scope(
                activity_type
            )
        )

        # ----------------------------------
        # Suspicious Record Detection
        # ----------------------------------
        is_flagged = False

        flag_reason = None

        try:

            quantity_value = float(
                normalized_quantity
            )

            # Negative or Zero Quantity
            if quantity_value <= 0:

                is_flagged = True

                flag_reason = (
                    "Quantity must be greater than zero"
                )

            # Extremely Large Quantity
            elif quantity_value > 100000:

                is_flagged = True

                flag_reason = (
                    "Unusually large quantity detected"
                )

        except (
            TypeError,
            ValueError
        ):

            is_flagged = True

            flag_reason = (
                "Invalid quantity value"
            )

        # ----------------------------------
        # Save Normalized Record
        # ----------------------------------
        return NormalizedRecord.objects.create(

            organization=organization,

            source=source,

            import_job=import_job,

            raw_record=raw_record,

            activity_type=activity_type,

            scope=scope,

            quantity=normalized_quantity,

            # IMPORTANT:
            # Must match model field name
            normalized_unit=normalized_unit,

            # IMPORTANT:
            # Must match model field name
            is_flagged=is_flagged,

            # IMPORTANT:
            # Must match model field name
            flag_reason=flag_reason
        )

    @staticmethod
    def is_suspicious(
        quantity
    ):
        """
        Utility method for future
        validation checks.
        """

        try:

            quantity = float(
                quantity
            )

            if quantity <= 0:
                return True

            if quantity > 100000:
                return True

            return False

        except (
            TypeError,
            ValueError
        ):

            return True