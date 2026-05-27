from core.choices import ScopeCategory


class ScopeMapper:
    """
    Scope Mapping Service

    Responsibilities:
    1. Map activities to ESG scopes
    2. Support Scope 1, Scope 2 and Scope 3
    3. Handle SAP, Utility and Travel data
    """

    SCOPE_MAPPING = {

        # ==================================
        # Scope 1 - Direct Emissions
        # ==================================

        "fuel": ScopeCategory.SCOPE_1,
        "diesel": ScopeCategory.SCOPE_1,
        "diesel fuel": ScopeCategory.SCOPE_1,
        "petrol": ScopeCategory.SCOPE_1,
        "petrol fuel": ScopeCategory.SCOPE_1,
        "natural_gas": ScopeCategory.SCOPE_1,
        "natural gas": ScopeCategory.SCOPE_1,
        "generator diesel": ScopeCategory.SCOPE_1,
        "boiler fuel": ScopeCategory.SCOPE_1,
        "lpg": ScopeCategory.SCOPE_1,

        # ==================================
        # Scope 2 - Purchased Electricity
        # ==================================

        "electricity": ScopeCategory.SCOPE_2,
        "grid electricity": ScopeCategory.SCOPE_2,
        "power consumption": ScopeCategory.SCOPE_2,
        "utility electricity": ScopeCategory.SCOPE_2,

        # ==================================
        # Scope 3 - Indirect Emissions
        # ==================================

        # Travel
        "flight": ScopeCategory.SCOPE_3,
        "air travel": ScopeCategory.SCOPE_3,
        "hotel": ScopeCategory.SCOPE_3,
        "taxi": ScopeCategory.SCOPE_3,
        "cab": ScopeCategory.SCOPE_3,
        "ground_transport": ScopeCategory.SCOPE_3,
        "train": ScopeCategory.SCOPE_3,
        "bus": ScopeCategory.SCOPE_3,

        # Procurement
        "procurement": ScopeCategory.SCOPE_3,
        "paper": ScopeCategory.SCOPE_3,
        "office supplies": ScopeCategory.SCOPE_3,
        "laptop purchase": ScopeCategory.SCOPE_3,
        "equipment": ScopeCategory.SCOPE_3,
    }

    @staticmethod
    def get_scope(activity_type):
        """
        Determine ESG scope based on activity type.

        Examples:

        Diesel Fuel  -> Scope 1
        Electricity  -> Scope 2
        Flight       -> Scope 3
        """

        if not activity_type:
            return ScopeCategory.SCOPE_3

        activity = str(
            activity_type
        ).strip().lower()

        return ScopeMapper.SCOPE_MAPPING.get(
            activity,
            ScopeCategory.SCOPE_3
        )

    @staticmethod
    def is_known_activity(
        activity_type
    ):
        """
        Check whether activity exists
        in mapping dictionary.
        """

        if not activity_type:
            return False

        activity = str(
            activity_type
        ).strip().lower()

        return (
            activity
            in ScopeMapper.SCOPE_MAPPING
        )