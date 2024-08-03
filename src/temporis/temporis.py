from datetime import datetime, date, timedelta


class Temporis:
    # Today date
    @staticmethod
    def get_current_datetime() -> datetime:
        return datetime.now()

    @staticmethod
    def get_current_date() -> date:
        return Temporis.get_current_datetime().date()

    # Transform datetime/string
    @staticmethod
    def to_str(dt: datetime | date, format_str: str) -> str:
        return dt.strftime(format_str)

    @staticmethod
    def from_str(date_str: str, format_str: str) -> datetime:
        return datetime.strptime(date_str, format_str)

    # Date operations
    @staticmethod
    def add_hours(dt: datetime, hours: int) -> datetime:
        return dt + timedelta(hours=hours)

    @staticmethod
    def add_days(dt: datetime, days: int) -> datetime:
        return dt + timedelta(days=days)

    @staticmethod
    def add_months(dt: datetime, months: int) -> datetime:
        return dt.replace(month=dt.month + months)

    # Business logic
    @staticmethod
    def next_business_day(dt: datetime, holidays: list[date] = []) -> datetime:
        while True:
            dt = Temporis.add_days(dt, 1)
            if Temporis.is_business_day(dt, holidays):
                return dt

    @staticmethod
    def next_quarter(dt: datetime) -> datetime:
        current_quarter = (dt.month - 1) // 3
        return dt.replace(month=current_quarter * 3 + 4)

    @staticmethod
    def next_semester(dt: datetime) -> datetime:
        current_semester = (dt.month - 1) // 6
        return dt.replace(month=current_semester * 6 + 7)

    @staticmethod
    def next_year(dt: datetime) -> datetime:
        return dt.replace(day=1, month=1, year=dt.year + 1)

    @staticmethod
    def previous_business_day(dt: datetime, holidays: list[date] = []) -> datetime:
        while True:
            dt = Temporis.add_days(dt, -1)
            if Temporis.is_business_day(dt, holidays):
                return dt

    @staticmethod
    def first_business_day_of_month(
        dt: datetime, holidays: list[date] = []
    ) -> datetime:
        dt = Temporis.first_day_of_month(dt)
        if not Temporis.is_business_day(dt, holidays):
            return Temporis.next_business_day(dt, holidays)
        return dt

    @staticmethod
    def last_business_day_of_month(
        dt: datetime, holidays: list[date] = []
    ) -> datetime:
        dt = Temporis.last_day_of_month(dt)
        if not Temporis.is_business_day(dt, holidays):
            return Temporis.previous_business_day(dt, holidays)

    # Utils
    @staticmethod
    def is_business_day(dt: datetime, holidays: list[date] = []) -> bool:
        return not Temporis.is_weekend(dt) and not Temporis.is_holiday(dt, holidays)

    @staticmethod
    def is_weekend(dt: datetime) -> bool:
        return dt.weekday() in [5, 6]

    @staticmethod
    def is_holiday(dt: datetime, holidays: list[date]) -> bool:
        return dt.date() in holidays

    @staticmethod
    def first_day_of_month(dt: datetime) -> datetime:
        return dt.replace(day=1)

    @staticmethod
    def last_day_of_month(dt: datetime) -> datetime:
        return dt.replace(day=1, month=dt.month + 1) - timedelta(days=1)

    @staticmethod
    def count_days_between(start: datetime, end: datetime) -> int:
        return (end - start).days
