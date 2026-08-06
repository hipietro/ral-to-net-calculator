from decimal import Decimal

from flask import Flask, render_template, request

from salary_calculator.contributions import (
    calculate_employee_contributions,
)
from salary_calculator.validation import parse_gross_salary

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    gross_salary: Decimal | None = None
    employee_contributions: Decimal | None = None
    error_message: str | None = None

    if request.method == "POST":
        raw_gross_salary = request.form.get("gross_salary")

        try:
            gross_salary = parse_gross_salary(raw_gross_salary)
            employee_contributions = calculate_employee_contributions(
                gross_salary,
            )
        except ValueError as error:
            error_message = str(error)

    return render_template(
        "index.html",
        gross_salary=gross_salary,
        employee_contributions=employee_contributions,
        error_message=error_message,
    )
