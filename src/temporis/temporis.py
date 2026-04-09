from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


DateLike = date | datetime


class Temporis:
    """
    A class for various date and time operations.
    """

    @staticmethod
    def get_current_datetime() -> datetime:
        """Returns the current date and time."""
        return datetime.now()

    @staticmethod
    def get_current_date() -> date:
        """Returns the current date."""
        return Temporis.get_current_datetime().date()

    @staticmethod
    def to_str(dt: datetime | date, format_str: str) -> str:
        """Converts a datetime or date object to a string based on the given format."""
        return dt.strftime(format_str)

    @staticmethod
    def from_str(date_str: str, format_str: str) -> datetime:
        """Parses a string to a datetime object based on the given format."""
        return datetime.strptime(date_str, format_str)

    @staticmethod
    def add_seconds(dt: datetime, seconds: int) -> datetime:
        """Adds seconds to a datetime object. This API remains datetime-only."""
        dt = Temporis._require_datetime(dt, "add_seconds")
        return dt + timedelta(seconds=seconds)

    @staticmethod
    def add_minutes(dt: datetime, minutes: int) -> datetime:
        """Adds minutes to a datetime object. This API remains datetime-only."""
        dt = Temporis._require_datetime(dt, "add_minutes")
        return dt + timedelta(minutes=minutes)

    @staticmethod
    def add_hours(dt: datetime, hours: int) -> datetime:
        """Adds hours to a datetime object. This API remains datetime-only."""
        dt = Temporis._require_datetime(dt, "add_hours")
        return dt + timedelta(hours=hours)

    @staticmethod
    def add_days(dt: DateLike, days: int) -> DateLike:
        """Adds days to a date or datetime while preserving the runtime type."""
        return dt + timedelta(days=days)

    @staticmethod
    def add_months(dt: DateLike, months: int) -> DateLike:
        """Adds months to a date or datetime while preserving the runtime type."""
        return dt + relativedelta(months=months)

    @staticmethod
    def next_business_day(dt: DateLike, holidays: list[date] | None = None) -> DateLike:
        """
        Returns the next business day for a date or datetime, skipping weekends and holidays.

        Parameters:
        -----------
        dt : date | datetime
            The starting calendar value.
        holidays : list[date] | None, optional
            A list of holiday dates to skip.
        """
        holidays = holidays or []
        while True:
            dt = Temporis.add_days(dt, 1)
            if Temporis.is_business_day(dt, holidays):
                return dt

    @staticmethod
    def next_quarter(dt: DateLike) -> DateLike:
        """Returns the first day of the next quarter, preserving the runtime type."""
        current_quarter = (dt.month - 1) // 3
        next_quarter_month = current_quarter * 3 + 4
        if next_quarter_month > 12:
            return dt.replace(year=dt.year + 1, month=1, day=1)
        return dt.replace(month=next_quarter_month, day=1)

    @staticmethod
    def next_semester(dt: DateLike) -> DateLike:
        """Returns the first day of the next semester, preserving the runtime type."""
        current_semester = (dt.month - 1) // 6
        next_semester_month = current_semester * 6 + 7
        if next_semester_month > 12:
            return dt.replace(year=dt.year + 1, month=1, day=1)
        return dt.replace(month=next_semester_month, day=1)

    @staticmethod
    def next_year(dt: DateLike) -> DateLike:
        """Returns the start of the next year, preserving the runtime type."""
        return dt.replace(day=1, month=1, year=dt.year + 1)

    @staticmethod
    def previous_business_day(
        dt: DateLike, holidays: list[date] | None = None
    ) -> DateLike:
        """
        Returns the previous business day for a date or datetime, skipping weekends and holidays.

        Parameters:
        -----------
        dt : date | datetime
            The starting calendar value.
        holidays : list[date] | None, optional
            A list of holiday dates to skip.
        """
        holidays = holidays or []
        while True:
            dt = Temporis.add_days(dt, -1)
            if Temporis.is_business_day(dt, holidays):
                return dt

    @staticmethod
    def first_business_day_of_month(
        dt: DateLike, holidays: list[date] | None = None
    ) -> DateLike:
        """
        Returns the first business day of the month for a date or datetime.

        Parameters:
        -----------
        dt : date | datetime
            The starting calendar value.
        holidays : list[date] | None, optional
            A list of holiday dates to skip.
        """
        holidays = holidays or []
        dt = Temporis.first_day_of_month(dt)
        if not Temporis.is_business_day(dt, holidays):
            return Temporis.next_business_day(dt, holidays)
        return dt

    @staticmethod
    def last_business_day_of_month(
        dt: DateLike, holidays: list[date] | None = None
    ) -> DateLike:
        """
        Returns the last business day of the month for a date or datetime.

        Parameters:
        -----------
        dt : date | datetime
            The starting calendar value.
        holidays : list[date] | None, optional
            A list of holiday dates to skip.
        """
        holidays = holidays or []
        dt = Temporis.last_day_of_month(dt)
        if not Temporis.is_business_day(dt, holidays):
            return Temporis.previous_business_day(dt, holidays)
        return dt

    @staticmethod
    def is_business_day(dt: DateLike, holidays: list[date] | None = None) -> bool:
        """
        Checks if a date-like value is a business day, excluding weekends and holidays.

        Parameters:
        -----------
        dt : date | datetime
            The calendar value to check.
        holidays : list[date] | None, optional
            A list of holiday dates to skip.

        Returns:
        --------
        bool
            True if the date is a business day, False otherwise.
        """
        holidays = holidays or []
        return not Temporis.is_weekend(dt) and not Temporis.is_holiday(dt, holidays)

    @staticmethod
    def is_weekend(dt: DateLike) -> bool:
        """
        Checks if a date-like value falls on a weekend.

        Parameters:
        -----------
        dt : date | datetime
            The calendar value to check.

        Returns:
        --------
        bool
            True if the date is a weekend, False otherwise.
        """
        return dt.weekday() in [5, 6]

    @staticmethod
    def is_holiday(dt: DateLike, holidays: list[date]) -> bool:
        """
        Checks if a date-like value matches a holiday by calendar day.

        Parameters:
        -----------
        dt : date | datetime
            The calendar value to check.
        holidays : list[date]
            A list of holiday dates.

        Returns:
        --------
        bool
            True if the date is a holiday, False otherwise.
        """
        return Temporis._calendar_date(dt) in holidays

    @staticmethod
    def first_day_of_month(dt: DateLike) -> DateLike:
        """
        Returns the first day of the month, preserving the runtime type.

        Parameters:
        -----------
        dt : date | datetime
            The calendar value to modify.

        Returns:
        --------
        date | datetime
            The first day of the month.
        """
        return dt.replace(day=1)

    @staticmethod
    def last_day_of_month(dt: DateLike) -> DateLike:
        """
        Returns the last day of the month, preserving the runtime type.

        Parameters:
        -----------
        dt : date | datetime
            The calendar value to modify.

        Returns:
        --------
        date | datetime
            The last day of the month.
        """
        if dt.month == 12:
            first_day_next_month = dt.replace(year=dt.year + 1, month=1, day=1)
        else:
            first_day_next_month = dt.replace(month=dt.month + 1, day=1)
        return first_day_next_month - timedelta(days=1)

    @staticmethod
    def count_days_between(start: DateLike, end: DateLike) -> int:
        """
        Counts the number of days between two homogeneous date-like values.

        Parameters:
        -----------
        start : date | datetime
            The start calendar value.
        end : date | datetime
            The end calendar value.

        Returns:
        --------
        int
            The number of days between the start and end dates.
        """
        return (end - start).days

    @staticmethod
    def _require_datetime(value: datetime, method_name: str) -> datetime:
        """Validates that a time-based API receives a datetime input."""
        if not isinstance(value, datetime):
            raise TypeError(f"{method_name} only supports datetime inputs")
        return value

    @staticmethod
    def _calendar_date(value: DateLike) -> date:
        """Normalizes a date-like value to a calendar date for comparisons."""
        if isinstance(value, datetime):
            return value.date()
        return value