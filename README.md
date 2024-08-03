  <h1 align="center">TEMPORIS</h1>
</p>
<p align="center">
    <em>Temporis is a Python library for elegantly managing and transforming <code>dates</code> and <code>times</code>.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/jalvarezgom/temporis?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/jalvarezgom/temporis?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jalvarezgom/temporis?style=default&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/pypi/v/temporis.svg?style=default&color=0080ff" alt="repo-top-language">
</p>


-----
## Overview
Temporis is a developer tool created to help with the problem of using and managing dates in Python. Supporting the use and change of the different time uses, operate and modify dates and their formats.

## Features
- Definition and use of different time changes
- Format for formatting dates to different <code>str</code>, <code>datetime</code> or <code>date</code> format
- Performing different types of operations with a <code>datetime</code>
  - Add or subtract hours, days, months
  - Get the next business day, quarter, semester or year
  - Identify if a datetime is a business day, weekend or holiday
  - Get the difference between two <code>datetime</code>

## Installation

```console
pip install temporis
```
## Usage

### Create a new datetime object
```python
from datetime import datetime
from temporis.temporis import Temporis
from temporis.format import TemporisFormat
from temporis.timezone import TemporisTz


# Create a new datetime object
dt = datetime(2021, 1, 1, 0, 0, 0)
# Add 5 hours to the datetime
dt = Temporis.add_hours(dt, 5)
# Add 5 days to the datetime
dt = Temporis.add_days(dt, 5)
# Minus 5 months to the datetime
dt = Temporis.add_months(dt, -5)
# Get the next business day
dt = Temporis.next_business_day(dt)
# Get the next quarter
dt = Temporis.next_quarter(dt)
# Apply UTC timezone to the datetime
dt = TemporisTz.to_UTC(dt)
# Print the datetime
print(Temporis.to_str(dt, format_str=TemporisFormat.YEAR_MONTH_DAY))
```

##  Repository Structure

```sh
└── temporis/
    ├── LICENSE
    ├── pdm.lock
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── temporis
    └── tests
        ├── __init__.py
        ├── test_datetime.py
        └── test_timezone.py
```

## License

`temporis` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
