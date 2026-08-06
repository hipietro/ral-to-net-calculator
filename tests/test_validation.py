from decimal import Decimal

import pytest

from salary_calculator.validation import parse_gross_salary, parse_payments


def test_parses_italian_number_format():
    assert parse_gross_salary("35.000,50") == Decimal("35000.50")


def test_rejects_out_of_scope_salary():
    with pytest.raises(ValueError, match="up to €120,000"):
        parse_gross_salary("150000")


def test_validates_payments():
    assert parse_payments("14") == 14
    with pytest.raises(ValueError):
        parse_payments("15")
