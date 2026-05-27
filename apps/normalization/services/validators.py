class ESGValidator:

    @staticmethod
    def validate(quantity, unit):

        errors = []

        if quantity <= 0:
            errors.append(
                "Invalid quantity"
            )

        if not unit:
            errors.append(
                "Missing unit"
            )

        return errors