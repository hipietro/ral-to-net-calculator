from decimal import Decimal

from .money import ZERO, money

ORDINARY_EMPLOYEE_RATE = Decimal("0.0919")
ADDITIONAL_EMPLOYEE_RATE = Decimal("0.01")
ADDITIONAL_CONTRIBUTION_THRESHOLD_2026 = Decimal("56224")


def calculate_employee_contributions(gross_salary: Decimal) -> Decimal:
    """Estimate employee-side social-security contributions for the model."""
    if gross_salary < ZERO:
        raise ValueError("Gross salary cannot be negative.")

    ordinary = gross_salary * ORDINARY_EMPLOYEE_RATE
    excess = max(gross_salary - ADDITIONAL_CONTRIBUTION_THRESHOLD_2026, ZERO)
    additional = excess * ADDITIONAL_EMPLOYEE_RATE
    return money(ordinary + additional)
