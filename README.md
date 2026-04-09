<h1 align="center">TEMPORIS</h1>

<p align="center">
    <em>An elegant Python library for managing and transforming dates and times</em>
</p>

<p align="center">
    <a href="https://github.com/jalvarezgom/temporis/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/jalvarezgom/temporis?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="License">
    </a>
    <a href="https://github.com/jalvarezgom/temporis/commits">
        <img src="https://img.shields.io/github/last-commit/jalvarezgom/temporis?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="Last commit">
    </a>
    <a href="https://pypi.org/project/temporis/">
        <img src="https://img.shields.io/pypi/v/temporis.svg?style=flat-square&logo=pypi&logoColor=white&color=0080ff" alt="PyPI Version">
    </a>
    <a href="https://pypi.org/project/temporis/">
        <img src="https://img.shields.io/pypi/pyversions/temporis?style=flat-square&logo=python&logoColor=white&color=0080ff" alt="Python Versions">
    </a>
</p>

## 🚀 Description

Temporis is a Python library designed to simplify date and time handling. It provides an elegant and functional interface to perform common date operations, manage time zones, and format dates consistently.

## ✨ Key Features

- 🔄 Flexible timezone conversion
- 📅 Advanced date operations:
  - Add and subtract hours, days, and months
  - Business day calculations
  - Quarter and semester determination
  - Holiday identification
- 🎨 Customizable date formatting
- ⚡ High performance and easy to use
- 📚 Comprehensive documentation and practical examples

## 🛠️ Installation

```bash
pip install temporis
```

## 💡 Usage Examples

### Basic Date Operations

```python
from datetime import date, datetime
from temporis.temporis import Temporis
from temporis.format import TemporisFormat
from temporis.timezone import TemporisTz

# Create a datetime object
moment = datetime(2024, 1, 1)

# Calendar-only APIs also accept plain date objects
calendar_day = date(2024, 1, 1)

# Date manipulation
moment = Temporis.add_hours(moment, 5)           # Add 5 hours
moment = Temporis.add_days(moment, 3)            # Add 3 days
moment = Temporis.next_business_day(moment)      # Get next business day
calendar_day = Temporis.next_business_day(calendar_day)

# Timezone change
date_utc = TemporisTz.to_UTC(moment)

# Date formatting
date_str = Temporis.to_str(moment, format_str=TemporisFormat.YEAR_MONTH_DAY)
print(date_str)  # Output: 2024-01-04
```

### Advanced Calculations

```python
# Get next quarter
next_quarter = Temporis.next_quarter(moment)

# Check if it's a business day
is_business = Temporis.is_business_day(moment)

# Calculate difference between dates
difference = Temporis.count_days_between(date1, date2)
```

### Supported input boundary

- Calendar-only APIs accept both `date` and `datetime` inputs: `add_days`, `add_months`, `next_business_day`, `previous_business_day`, `first_business_day_of_month`, `last_business_day_of_month`, `next_quarter`, `next_semester`, `next_year`, `first_day_of_month`, `last_day_of_month`, `count_days_between`, `is_weekend`, `is_holiday`, and `is_business_day`.
- These calendar methods preserve the caller runtime type when they return a date-like value.
- Time arithmetic (`add_seconds`, `add_minutes`, `add_hours`) remains `datetime`-only.
- Timezone operations from `TemporisTz` remain `datetime`-only.

## 📁 Project Structure

```
temporis/
├── src/
│   └── temporis/
│       ├── __init__.py
│       ├── temporis.py
│       ├── format.py
│       └── timezone.py
├── tests/
│   ├── test_datetime.py
│   └── test_timezone.py
├── LICENSE
├── README.md
└── pyproject.toml
```

## 🤝 Contributing

Contributions are welcome. Please feel free to:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add: AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📫 Contact

- GitHub: [@jalvarezgom](https://github.com/jalvarezgom)
- PyPI: [temporis](https://pypi.org/project/temporis/)

---

<p align="center">
    <em>Developed with ❤️ by Jancel</em>
</p>
