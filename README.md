<div align="center">

# RAL to Net Calculator

### A transparent Italian gross-to-net salary estimator for tax year 2026

[Open the live calculator](https://ral-to-net-calculator.onrender.com/) · [Calculation model](docs/calculation-model.md) · [Official sources](docs/sources.md)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white)
![Tests](https://img.shields.io/badge/tests-18%20passing-2E7D32)
![License](https://img.shields.io/badge/license-MIT-blue)

</div>

## Overview

RAL to Net Calculator is a web prototype built for the **Jet HR Product Builder task**.

It estimates how an employee's gross annual salary is divided between net income, social-security contributions and taxes. Unlike calculators that return only a final number, this project exposes the main calculation steps, assumptions and fiscal rules used by the model.

> **Live application:** https://ral-to-net-calculator.onrender.com/

## What it calculates

Given a gross annual salary (`RAL`) and the number of salary payments, the application returns:

- estimated annual net income;
- average net amount across 12, 13 or 14 payments;
- employee social-security contributions;
- taxable employment income;
- gross and net IRPEF;
- employee tax deductions and tax-wedge relief;
- Lombardy regional surtax;
- Milan municipal surtax;
- total taxes and total amount withheld;
- effective take-home percentage.

The detailed breakdown can be expanded directly from the result page.

## Supported scenario

The MVP deliberately models a narrow, explainable case:

| Parameter | Assumption |
| --- | --- |
| Tax year | 2026 |
| Employment | Permanent private-sector employee |
| Employment period | Full calendar year |
| Tax residence | Milan, Lombardy |
| Other income | None |
| Dependants | None |
| Special deductions or regimes | None |
| Supported RAL | €5,000–€120,000 |

This scope is intentional. It keeps the result testable and avoids presenting incomplete fiscal logic as precise payroll advice.

More detail is available in [docs/assumptions.md](docs/assumptions.md).

## Product decisions

### Transparent calculations

Every major deduction is shown separately, so the user can understand how the estimate was produced.

### Fiscal logic separated from the interface

The calculation functions do not depend on Flask or HTML. They can be tested and reused independently.

### Explicit assumptions over false precision

The application supports one well-documented standard case rather than pretending to cover every Italian contract, municipality and personal tax situation.

### Money handled with `Decimal`

All monetary calculations use Python's `Decimal` type and commercial rounding to euro cents instead of binary floating-point arithmetic.

## Architecture

```text
Browser form
    │
    ▼
Flask route ─────────────── app.py
    │
    ▼
Input validation ────────── validation.py
    │
    ▼
Calculation orchestrator ── calculator.py
    │
    ├── social contributions
    ├── IRPEF and employee deductions
    ├── regional surtax
    └── municipal surtax
    │
    ▼
SalaryCalculationResult ─── immutable dataclass
    │
    ▼
Jinja template ──────────── result page
```

## Tech stack

| Area | Technology |
| --- | --- |
| Backend | Python 3.13, Flask |
| Interface | Jinja, semantic HTML, responsive CSS |
| Production server | Gunicorn |
| Testing | Pytest |
| Deployment | Render |
| Continuous integration | GitHub Actions |

No database or JavaScript framework is required because the calculator is a deterministic operation with no persistent user data.

## Repository structure

```text
.
├── app.py
├── salary_calculator/
│   ├── calculator.py
│   ├── contributions.py
│   ├── irpef.py
│   ├── local_taxes.py
│   ├── models.py
│   ├── money.py
│   └── validation.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tests/
├── docs/
│   ├── assumptions.md
│   ├── calculation-model.md
│   ├── future-improvements.md
│   └── sources.md
├── render.yaml
└── requirements.txt
```

## Run locally

```bash
uv venv --python 3.13 .venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt
flask --app app run --debug
```

Open `http://127.0.0.1:5000`.

## Run the tests

```bash
python -m pytest
```

The test suite covers:

- contribution rates and thresholds;
- progressive IRPEF brackets;
- employee deductions and tax-wedge relief;
- regional and municipal surtaxes;
- common Italian and international number formats;
- supported salary and payment inputs;
- end-to-end result reconciliation.

## Deployment

The application is deployed on Render using Gunicorn:

```bash
gunicorn app:app
```

The repository keeps `render.yaml` as infrastructure-as-code. It documents the production build, start command and health check, and allows the deployment to be recreated consistently.

## Documentation

- [Calculation assumptions](docs/assumptions.md)
- [Calculation model](docs/calculation-model.md)
- [Official and institutional sources](docs/sources.md)
- [Possible future improvements](docs/future-improvements.md)

## Limitations

This project is an indicative prototype, not payroll software or professional tax advice. Actual payslips may differ because of contract-specific contributions, payroll timing, bonuses, personal deductions, local rules and year-end adjustments.

## AI-assisted workflow

AI tools were used to accelerate research, implementation and review. The final behaviour does not depend on an AI service: fiscal rules are written explicitly, connected to documented sources and covered by automated tests.

## License

Distributed under the [MIT License](LICENSE).
