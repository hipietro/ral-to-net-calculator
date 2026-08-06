from decimal import Decimal

from .money import ZERO, money

MILAN_MUNICIPAL_EXEMPTION = Decimal("23000")
MILAN_MUNICIPAL_RATE = Decimal("0.008")


def calculate_lombardy_regional_tax(taxable_income: Decimal) -> Decimal:
    """2026 Lombardy regional surtax, applied progressively."""
    if taxable_income <= ZERO:
        return ZERO

    brackets = (
        (Decimal("15000"), Decimal("0.0123")),
        (Decimal("28000"), Decimal("0.0158")),
        (Decimal("50000"), Decimal("0.0172")),
        (None, Decimal("0.0173")),
    )

    tax = ZERO
    lower = ZERO
    for upper, rate in brackets:
        if upper is None:
            amount = max(taxable_income - lower, ZERO)
        else:
            amount = min(max(taxable_income - lower, ZERO), upper - lower)
        tax += amount * rate
        if upper is None or taxable_income <= upper:
            break
        lower = upper

    return money(tax)


def calculate_milan_municipal_tax(taxable_income: Decimal) -> Decimal:
    """Milan 0.8% surtax; the €23k exemption is not a tax-free allowance."""
    if taxable_income <= MILAN_MUNICIPAL_EXEMPTION:
        return ZERO
    return money(taxable_income * MILAN_MUNICIPAL_RATE)
