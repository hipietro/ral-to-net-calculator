from decimal import Decimal

from .contributions import calculate_employee_contributions
from .irpef import (
    calculate_employee_deduction,
    calculate_gross_irpef,
    calculate_net_irpef,
    calculate_tax_wedge_relief,
    calculate_treatment_integrativo,
)
from .local_taxes import (
    calculate_lombardy_regional_tax,
    calculate_milan_municipal_tax,
)
from .models import SalaryCalculationResult
from .money import money

SUPPORTED_PAYMENTS = {12, 13, 14}


def calculate_salary(gross_salary: Decimal, payments: int = 13) -> SalaryCalculationResult:
    if gross_salary <= Decimal("0"):
        raise ValueError("Gross annual salary must be greater than zero.")
    if payments not in SUPPORTED_PAYMENTS:
        raise ValueError("Payments must be 12, 13 or 14.")

    contributions = calculate_employee_contributions(gross_salary)
    taxable_income = money(gross_salary - contributions)
    gross_irpef = calculate_gross_irpef(taxable_income)
    employee_deduction = calculate_employee_deduction(taxable_income)
    tax_free_sum, additional_deduction = calculate_tax_wedge_relief(taxable_income)
    net_irpef = calculate_net_irpef(
        gross_irpef,
        employee_deduction,
        additional_deduction,
    )
    regional_tax = calculate_lombardy_regional_tax(taxable_income)
    municipal_tax = calculate_milan_municipal_tax(taxable_income)
    treatment_integrativo = calculate_treatment_integrativo(
        taxable_income,
        gross_irpef,
        employee_deduction,
    )

    total_taxes = money(net_irpef + regional_tax + municipal_tax)
    total_withheld = money(contributions + total_taxes)
    annual_net = money(
        gross_salary
        - total_withheld
        + tax_free_sum
        + treatment_integrativo
    )
    net_per_payment = money(annual_net / Decimal(payments))
    take_home_rate = money((annual_net / gross_salary) * Decimal("100"))

    return SalaryCalculationResult(
        gross_salary=money(gross_salary),
        payments=payments,
        employee_contributions=contributions,
        taxable_income=taxable_income,
        gross_irpef=gross_irpef,
        employee_deduction=employee_deduction,
        additional_employee_deduction=additional_deduction,
        net_irpef=net_irpef,
        regional_tax=regional_tax,
        municipal_tax=municipal_tax,
        tax_free_employee_sum=tax_free_sum,
        treatment_integrativo=treatment_integrativo,
        total_taxes=total_taxes,
        total_withheld=total_withheld,
        annual_net=annual_net,
        net_per_payment=net_per_payment,
        take_home_rate=take_home_rate,
    )
