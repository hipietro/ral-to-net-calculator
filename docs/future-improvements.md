# Future Improvements

These extensions were considered during product design and intentionally excluded from the MVP to keep the model explainable and testable.

## Location coverage

- Add a city selector backed by versioned regional and municipal rules.
- Import official data for all Italian municipalities.
- Handle local exemptions, progressive rates and missing annual resolutions.

The MVP supports Milan only because municipal 2026 data is not uniformly available for every city, and a partially correct nationwide selector would create false precision.

## Employment profiles

- Fixed-term, apprenticeship, part-time and public-sector profiles.
- CCNL and employment level.
- Sector-specific contribution rates.
- Partial-year employment and multiple employers.

## Personal circumstances

- Dependant spouse, children and other family members.
- Personal deductions such as medical expenses, mortgage interest and donations.
- Inbound-worker and returning-researcher regimes.
- Disability-related benefits and other exemptions.

## Compensation components

- Bonuses, overtime, commissions and productivity awards.
- Fringe benefits, meal vouchers and company welfare.
- Supplementary pension contributions.
- TFR accrual and employer-side cost.

## Product features

- Compare a current RAL with a job offer.
- Generate a PDF report.
- Share calculations through a link.
- Italian/English language switch.
- Full monthly payslip simulation rather than an annual average.
- Versioned calculations across tax years.

## Data operations

- Automated retrieval of official tax data.
- Change detection and human review before publishing new rules.
- Regression tests for every threshold and annual rule update.

Any extension should be added only when its rules can be explained, sourced, isolated from the interface and covered by tests.
