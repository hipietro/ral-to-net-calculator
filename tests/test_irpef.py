from decimal import Decimal

from salary_calculator.irpef import (
    calculate_employee_deduction,
    calculate_gross_irpef,
    calculate_tax_wedge_relief,
)


def test_irpef_at_first_threshold():
    assert calculate_gross_irpef(Decimal("28000")) == Decimal("6440.00")


def test_irpef_at_second_threshold():
    assert calculate_gross_irpef(Decimal("50000")) == Decimal("13700.00")


def test_irpef_above_second_threshold():
    assert calculate_gross_irpef(Decimal("60000")) == Decimal("18000.00")


def test_employee_deduction_low_income():
    assert calculate_employee_deduction(Decimal("15000")) == Decimal("1955.00")


def test_employee_deduction_includes_65_euro_increase():
    assert calculate_employee_deduction(Decimal("30000")) == Decimal("1801.36")


def test_tax_wedge_relief_up_to_20k():
    assert calculate_tax_wedge_relief(Decimal("20000")) == (
        Decimal("960.00"),
        Decimal("0"),
    )


def test_additional_deduction_tapers_to_zero():
    assert calculate_tax_wedge_relief(Decimal("36000")) == (
        Decimal("0"),
        Decimal("500.00"),
    )
