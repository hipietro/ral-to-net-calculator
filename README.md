# RAL to Net Calculator

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/hipietro/ral-to-net-calculator)

A transparent Italian gross-to-net salary calculator built for the Jet HR Product Builder task.

The application takes a gross annual salary (`RAL`) and estimates:

- annual net income;
- average net amount across 12, 13 or 14 payments;
- employee social-security contributions;
- national IRPEF;
- Lombardy regional surtax;
- Milan municipal surtax;
- employee deductions and tax-wedge benefits.

## Product goal

Most gross-to-net calculators return a number without showing how it was obtained. This prototype exposes every major step, states its assumptions and keeps fiscal logic separate from the web interface.

## Supported scenario

- Tax year: **2026**
- Permanent private-sector employee
- Full-year employment
- Tax residence: **Milan, Lombardy**
- No dependants, personal deductions or special regimes
- RAL between €5,000 and €120,000

See [calculation assumptions](docs/assumptions.md) and [calculation model](docs/calculation-model.md).

## Tech stack

- Python 3.13
- Flask
- Jinja templates
- HTML and CSS
- Pytest
- Gunicorn
- Render deployment configuration
- GitHub Actions CI

## Architecture

```text
Browser form
    ↓
Flask route (app.py)
    ↓
Input validation
    ↓
Salary calculation orchestrator
    ├── contributions
    ├── national IRPEF and deductions
    ├── regional surtax
    └── municipal surtax
    ↓
Typed result dataclass
    ↓
Jinja template
```

Fiscal functions do not depend on Flask and can be tested independently.

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
├── templates/index.html
├── static/style.css
├── tests/
├── docs/
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

## Tests

```bash
python -m pytest
```

Tests cover contribution rules, IRPEF thresholds, employee deductions, local surtaxes, validation and end-to-end reconciliation.

## Deploy on Render

The repository includes a `render.yaml` Blueprint.

1. Create a new Render Blueprint.
2. Connect this GitHub repository.
3. Render detects `render.yaml` and creates the Flask web service.

The production start command is:

```bash
gunicorn app:app
```

## Sources and limitations

- [Official sources](docs/sources.md)
- [Known assumptions](docs/assumptions.md)
- [Future improvements](docs/future-improvements.md)

This is an indicative prototype, not payroll or tax advice.

## AI-assisted workflow

AI tools were used to accelerate research, implementation and review. Rules are kept explicit, linked to institutional sources and covered by automated tests so the final behaviour can be inspected and explained without relying on the AI that helped build it.
