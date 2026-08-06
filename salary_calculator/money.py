from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
ZERO = Decimal("0")


def money(value: Decimal) -> Decimal:
    """Round a monetary value to euro cents using commercial rounding."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def clamp_non_negative(value: Decimal) -> Decimal:
    return max(value, ZERO)
