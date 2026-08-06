from decimal import Decimal

from flask import Flask, render_template, request

from salary_calculator import SalaryCalculationResult, calculate_salary
from salary_calculator.validation import parse_gross_salary, parse_payments

app = Flask(__name__)


def format_euro(value: Decimal) -> str:
    formatted = f"{value:,.2f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


app.jinja_env.filters["euro"] = format_euro


@app.get("/health")
def health():
    return {"status": "ok"}


@app.route("/", methods=["GET", "POST"])
def home():
    result: SalaryCalculationResult | None = None
    error_message: str | None = None
    form_salary = request.form.get("gross_salary", "35000")
    form_payments = request.form.get("payments", "13")

    if request.method == "POST":
        try:
            gross_salary = parse_gross_salary(form_salary)
            payments = parse_payments(form_payments)
            result = calculate_salary(gross_salary, payments)
        except ValueError as error:
            error_message = str(error)

    return render_template(
        "index.html",
        result=result,
        error_message=error_message,
        form_salary=form_salary,
        form_payments=form_payments,
    )
