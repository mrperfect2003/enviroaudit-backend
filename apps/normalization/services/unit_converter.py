from decimal import Decimal


class UnitConverter:
    """
    Unit Conversion Service

    Responsibilities:
    1. Standardize unit names
    2. Convert quantities into a common format
    3. Support future ESG unit conversions
    """

    # Standard unit mapping
    UNIT_MAPPING = {

        # Fuel Units
        "L": "liter",
        "LTR": "liter",
        "LITER": "liter",
        "LITERS": "liter",

        # Weight Units
        "KG": "kg",
        "KGS": "kg",

        "TON": "kg",
        "TONNE": "kg",
        "TONNES": "kg",

        # Electricity
        "KWH": "kWh",
        "MWH": "kWh",

        # Volume
        "M3": "m3",

        # Distance
        "KM": "km"
    }

    @staticmethod
    def normalize_unit(unit):
        """
        Convert incoming units into a standard unit name.

        Examples:
        LTR     -> liter
        TONNE   -> kg
        KWH     -> kWh
        """

        if not unit:
            return None

        return UnitConverter.UNIT_MAPPING.get(
            str(unit).upper(),
            str(unit).lower()
        )

    @staticmethod
    def convert_quantity(
        quantity,
        unit
    ):
        """
        Convert quantity to normalized value.

        Examples:
        2 TONNE -> 2000 KG
        1 MWH   -> 1000 KWH
        """

        try:

            quantity = Decimal(
                str(quantity)
            )

            unit = str(unit).upper()

            # TONNE → KG
            if unit in [
                "TON",
                "TONNE",
                "TONNES"
            ]:
                return (
                    quantity *
                    Decimal("1000")
                )

            # MWH → KWH
            if unit == "MWH":
                return (
                    quantity *
                    Decimal("1000")
                )

            return quantity

        except Exception:

            return Decimal("0")