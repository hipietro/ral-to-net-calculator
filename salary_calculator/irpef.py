from decimal import Decimal

from .money import ZERO, clamp_non_negative, money

FIRST_LIMIT = Decimal("28000")
SECOND_LIMIT = Decimal("50000")
FIRST_RATE = Decimal("0.23")
SECOND_RATE_2026 = Decimal("0.33")
THIRD_RATE = Decimal("0.43")


def calculate_gross_irpef(taxable_income: Decimal) -> Decimal:
    if taxable_income <= ZERO:
        return ZERO

    first = min(taxable_income, FIRST_LIMIT) * FIRST_RATE
    second = min(max(taxable_income - FIRST_LIMIT, ZERO), SECOND_LIMIT - FIRST_LIMIT) * SECOND_RATE_2026
    third = max(taxable_income - SECOND_LIMIT, ZERO) * THIRD_RATE
    return money(first + second + third)


def calculate_employee_deduction(taxable_income: Decimal) -> Decimal:
    """Full-year employee deduction under article 13 TUIR."""
    if taxable_income <= ZERO:
        return ZERO

    if taxable_income <= Decimal("15000"):
        deduction = Decimal("1955")
    elif taxable_income <= Decimal("28000"):
        deduction = Decimal("1910") + (
            Decimal("1190")
            * (Decimal("28000") - taxable_income)
            / Decimal("13000")
        )
    elif taxable_income <= Decimal("50000"):
        deduction = (
            Decimal("1910")
            * (Decimal("50000") - taxable_income)
            / Decimal("22000")
        )
    else:
        deduction = ZERO

    if Decimal("25000") < taxable_income <= Decimal("35000"):
        deduction += Decimal("65")

    return money(clamp_non_negative(deduction))


def calculate_tax_wedge_relief(taxable_income: Decimal) -> tuple[Decimal, Decimal]:
    """Return (tax-free employee sum, additional employee deduction)."""
    if taxable_income <= ZERO:
        return ZERO, ZERO

    if taxable_income <= Decimal("20000"):
        if taxable_income <= Decimal("8500"):
            rate = Decimal("0.071")
        elif taxable_income <= Decimal("15000"):
            rate = Decimal("0.053")
        else:
            rate = Decimal("0.048")
        return money(taxable_income * rate), ZERO

    if taxable_income <= Decimal("32000"):
        return ZERO, Decimal("1000.00")

    if taxable_income < Decimal("40000"):
        deduction = (
            Decimal("1000")
            * (Decimal("40000") - taxable_income)
            / Decimal("8000")
        )
        return ZERO, money(deduction)

    return ZERO, ZERO


def calculate_treatment_integrativo(
    taxable_income: Decimal,
    gross_irpef: Decimal,
    employee_deduction: Decimal,
) -> Decimal:
    """Model the standard full-year treatment integrativo for income up to €15k."""
    if taxable_income <= ZERO or taxable_income > Decimal("15000"):
        return ZERO

    eligibility_threshold = max(employee_deduction - Decimal("75"), ZERO)
    return Decimal("1200.00") if gross_irpef > eligibility_threshold else ZERO


def calculate_net_irpef(
    gross_irpef: Decimal,
    employee_deduction: Decimal,
    additional_employee_deduction: Decimal,
) -> Decimal:
    return money(
        clamp_non_negative(
            gross_irpef - employee_deduction - additional_employee_deduction
        )
    )
