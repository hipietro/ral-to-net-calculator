from decimal import Decimal, InvalidOperation


def parse_gross_salary(raw_value: str | None) -> Decimal:
    if raw_value is None or raw_value.strip() == "":
        raise ValueError("Gross annual salary is required.")

    try:
        gross_salary = Decimal(raw_value)
    except InvalidOperation as exc:
        raise ValueError("Gross annual salary must be a valid number.") from exc

    if gross_salary <= 0:
        raise ValueError("Gross annual salary must be greater than zero.")

    return gross_salary
