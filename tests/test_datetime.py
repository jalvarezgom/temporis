from datetime import datetime, date

from temporis.temporis import Temporis
from temporis.format import TemporisFormat


def test_datetime_format_change_delimiter():
    assert TemporisFormat.YEAR_MONTH_DAY == "%Y-%m-%d"
    datetime_format = TemporisFormat(datetime_delimiter="/")
    assert datetime_format.YEAR_MONTH_DAY == "%Y/%m/%d"


def test_datetime_today():
    new_date = Temporis.get_current_datetime()
    assert isinstance(new_date, datetime)
    assert Temporis.to_str(new_date, "%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d")


def test_datetime_today_date():
    new_date = Temporis.get_current_date()
    assert isinstance(new_date, date)
    assert Temporis.to_str(new_date, "%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d")


def test_datetime_to_str():
    new_date = datetime.now()
    assert Temporis.to_str(
        new_date, TemporisFormat.YEAR_MONTH_DAY
    ) == new_date.strftime(TemporisFormat.YEAR_MONTH_DAY)


def test_datetime_from_str():
    new_date = datetime.now()
    assert isinstance(
        Temporis.from_str(
            new_date.strftime(TemporisFormat.YEAR_MONTH_DAY),
            TemporisFormat.YEAR_MONTH_DAY,
        ),
        datetime,
    )


def test_datetime_add_days():
    new_date = datetime.now()
    assert Temporis.add_days(new_date, 1) > new_date


def test_datetime_add_months():
    new_date = datetime.now()
    assert Temporis.add_months(new_date, 1) > new_date


def test_datetime_next_business_day():
    new_date = Temporis.next_business_day(datetime.now())
    assert Temporis.is_business_day(new_date)


def test_count_days():
    new_date = datetime.now()
    assert Temporis.count_days_between(new_date, new_date) == 0
    assert Temporis.count_days_between(new_date, Temporis.add_days(new_date, 1)) == 1
    assert Temporis.count_days_between(new_date, Temporis.add_days(new_date, -1)) == -1
    assert (
        Temporis.count_days_between(new_date, Temporis.add_days(new_date, 365)) == 365
    )
    assert (
        Temporis.count_days_between(new_date, Temporis.add_days(new_date, -365)) == -365
    )
