"""Core salary calculation package."""

from .calculator import calculate_salary
from .models import SalaryCalculationResult

__all__ = ["SalaryCalculationResult", "calculate_salary"]
