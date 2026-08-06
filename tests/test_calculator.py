from decimal import Decimal

from salary_calculator import calculate_salary


def test_standard_35k_salary_reconciles():
    result = calculate_salary(Decimal("35000"), 13)

    assert result.employee_contributions == Decimal("3216.50")
    assert result.taxable_income == Decimal("31783.50")
    assert result.annual_net == Decimal("26032.21")
    assert result.net_per_payment == Decimal("2002.48")

    reconciled = (
        result.gross_salary
        - result.total_withheld
        + result.tax_free_employee_sum
        + result.treatment_integrativo
    )
    assert reconciled == result.annual_net


def test_payments_change_only_average_payment():
    thirteen = calculate_salary(Decimal("35000"), 13)
    fourteen = calculate_salary(Decimal("35000"), 14)

    assert thirteen.annual_net == fourteen.annual_net
    assert thirteen.net_per_payment != fourteen.net_per_payment


def test_local_surtaxes_are_not_due_when_net_irpef_is_zero():
    result = calculate_salary(Decimal("5000"), 13)

    assert result.net_irpef == Decimal("0.00")
    assert result.regional_tax == Decimal("0")
    assert result.municipal_tax == Decimal("0")
