from decimal import Decimal

from salary_calculator.local_taxes import (
    calculate_lombardy_regional_tax,
    calculate_milan_municipal_tax,
)


def test_lombardy_tax_is_progressive():
    assert calculate_lombardy_regional_tax(Decimal("35000")) == Decimal("510.30")


def test_milan_exemption_is_not_a_franchise():
    assert calculate_milan_municipal_tax(Decimal("23000")) == Decimal("0")
    assert calculate_milan_municipal_tax(Decimal("23000.01")) == Decimal("184.00")
