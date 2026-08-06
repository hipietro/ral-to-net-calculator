from decimal import Decimal, InvalidOperation

MIN_GROSS_SALARY = Decimal("5000")
MAX_GROSS_SALARY = Decimal("120000")
SUPPORTED_PAYMENTS = {12, 13, 14}


def parse_gross_salary(raw_value: str | None) -> Decimal:
    if raw_value is None or raw_value.strip() == "":
        raise ValueError("Gross annual salary is required.")

    normalized = raw_value.strip().replace("€", "").replace(" ", "")
    if "," in normalized and "." in normalized:
        if normalized.rfind(",") > normalized.rfind("."):
            normalized = normalized.replace(".", "").replace(",", ".")
        else:
            normalized = normalized.replace(",", "")
    elif "," in normalized:
        groups = normalized.split(",")
        if len(groups) > 1 and all(len(group) == 3 for group in groups[1:]):
            normalized = "".join(groups)
        else:
            normalized = normalized.replace(",", ".")
    elif "." in normalized:
        groups = normalized.split(".")
        if len(groups) > 1 and all(len(group) == 3 for group in groups[1:]):
            normalized = "".join(groups)

    try:
        gross_salary = Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError("Gross annual salary must be a valid number.") from exc

    if gross_salary < MIN_GROSS_SALARY:
        raise ValueError("Gross annual salary must be at least €5,000.")
    if gross_salary > MAX_GROSS_SALARY:
        raise ValueError("This prototype supports salaries up to €120,000.")
    return gross_salary


def parse_payments(raw_value: str | None) -> int:
    try:
        payments = int(raw_value or "13")
    except ValueError as exc:
        raise ValueError("Payments must be 12, 13 or 14.") from exc
    if payments not in SUPPORTED_PAYMENTS:
        raise ValueError("Payments must be 12, 13 or 14.")
    return payments
