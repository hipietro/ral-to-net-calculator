from decimal import Decimal, ROUND_HALF_UP


ORDINARY_EMPLOYEE_RATE = Decimal("0.0919")
ADDITIONAL_EMPLOYEE_RATE = Decimal("0.01")
ADDITIONAL_CONTRIBUTION_THRESHOLD_2026 = Decimal("56224")
CENT = Decimal("0.01")


def calculate_employee_contributions(
    gross_salary: Decimal,
) -> Decimal:
    if gross_salary < 0:
        raise ValueError("Gross salary cannot be negative.")

    ordinary_contributions = gross_salary * ORDINARY_EMPLOYEE_RATE

    salary_above_threshold = max(
        gross_salary - ADDITIONAL_CONTRIBUTION_THRESHOLD_2026,
        Decimal("0"),
    )

    additional_contributions = (
        salary_above_threshold * ADDITIONAL_EMPLOYEE_RATE
    )

    total_contributions = (
        ordinary_contributions + additional_contributions
    )

    return total_contributions.quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )
