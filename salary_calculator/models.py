from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class SalaryCalculationResult:
    gross_salary: Decimal
    payments: int
    employee_contributions: Decimal
    taxable_income: Decimal
    gross_irpef: Decimal
    employee_deduction: Decimal
    additional_employee_deduction: Decimal
    net_irpef: Decimal
    regional_tax: Decimal
    municipal_tax: Decimal
    tax_free_employee_sum: Decimal
    treatment_integrativo: Decimal
    total_taxes: Decimal
    total_withheld: Decimal
    annual_net: Decimal
    net_per_payment: Decimal
    take_home_rate: Decimal
