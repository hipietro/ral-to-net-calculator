from decimal import Decimal

import pytest

from salary_calculator.contributions import calculate_employee_contributions


def test_calculates_ordinary_contributions():
    assert calculate_employee_contributions(Decimal("35000")) == Decimal("3216.50")


def test_applies_additional_rate_above_threshold():
    assert calculate_employee_contributions(Decimal("60000")) == Decimal("5551.76")


def test_rejects_negative_salary():
    with pytest.raises(ValueError, match="Gross salary cannot be negative"):
        calculate_employee_contributions(Decimal("-1"))
