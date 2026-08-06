# Calculation Model

## Flow

1. Validate gross annual salary and number of payments.
2. Estimate employee social-security contributions.
3. Subtract contributions to obtain taxable income.
4. Apply progressive national IRPEF brackets.
5. Apply the ordinary employee deduction.
6. Apply the 2025 structural tax-wedge measure still in force in 2026:
   - tax-free employee sum up to €20,000;
   - additional deduction from €20,000 to €40,000.
7. Apply Lombardy regional surtax.
8. Apply Milan municipal surtax.
9. Add any modelled treatment integrativo.
10. Divide annual net by the selected number of payments.

## Formula summary

```text
Taxable income = RAL - employee contributions

Net IRPEF = max(
    gross IRPEF
    - employee deduction
    - additional employee deduction,
    0
)

Annual net = RAL
    - employee contributions
    - net IRPEF
    - regional surtax
    - municipal surtax
    + tax-free employee sum
    + treatment integrativo
```

All monetary outputs use `Decimal` and are rounded to euro cents with `ROUND_HALF_UP`.

## Known modelling choices

- The prototype uses taxable employment income as the reference income for deductions and tax-wedge thresholds.
- The ordinary 9.19% employee contribution rate is a simplified standard-case assumption; exact rates can vary by employer sector and contribution profile.
- The 1% additional contribution is applied above the 2026 annual threshold of €56,224.
- Milan's €23,000 municipal exemption is treated as a threshold, not as a franchise.
- The treatment integrativo is modelled only for the standard full-year case up to €15,000 and excludes the more complex €15,000–€28,000 eligibility path involving other deductions.
