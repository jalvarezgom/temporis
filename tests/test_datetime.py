from datetime import datetime, date

import pytest

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
    new_date = datetime(2024, 1, 15)
    assert Temporis.add_months(new_date, 2) == datetime(2024, 3, 15)


def test_datetime_add_months_uses_argument():
    new_date = datetime(2024, 1, 31)
    assert Temporis.add_months(new_date, 2).month == 3


def test_last_day_of_month_handles_december():
    new_date = datetime(2024, 12, 15)
    assert Temporis.last_day_of_month(new_date) == datetime(2024, 12, 31, 0, 0)


def test_next_quarter_moves_to_next_period():
    new_date = datetime(2024, 2, 15)
    assert Temporis.next_quarter(new_date) == datetime(2024, 4, 1, 0, 0)


def test_next_quarter_wraps_year():
    new_date = datetime(2024, 11, 15)
    assert Temporis.next_quarter(new_date) == datetime(2025, 1, 1, 0, 0)


def test_next_semester_moves_to_next_period():
    new_date = datetime(2024, 2, 15)
    assert Temporis.next_semester(new_date) == datetime(2024, 7, 1, 0, 0)


def test_next_semester_wraps_year():
    new_date = datetime(2024, 11, 15)
    assert Temporis.next_semester(new_date) == datetime(2025, 1, 1, 0, 0)


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


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (date(2024, 4, 6), True),
        (datetime(2024, 4, 6, 12, 30), True),
        (date(2024, 4, 8), False),
        (datetime(2024, 4, 8, 12, 30), False),
    ],
)
def test_is_weekend_accepts_date_like_inputs(value, expected):
    assert Temporis.is_weekend(value) is expected


def test_calendar_predicates_match_for_date_and_datetime_inputs():
    holiday = date(2024, 5, 1)
    holiday_as_datetime = datetime(2024, 5, 1, 15, 45)

    assert Temporis.is_holiday(holiday, [holiday]) is True
    assert Temporis.is_holiday(holiday_as_datetime, [holiday]) is True
    assert Temporis.is_business_day(holiday, [holiday]) is False
    assert Temporis.is_business_day(holiday_as_datetime, [holiday]) is False


def test_business_day_navigation_preserves_date_type_for_date_inputs():
    monday_holiday = date(2024, 5, 6)

    next_day = Temporis.next_business_day(date(2024, 5, 3), [monday_holiday])
    previous_day = Temporis.previous_business_day(date(2024, 5, 6), [monday_holiday])

    assert next_day == date(2024, 5, 7)
    assert type(next_day) is date
    assert previous_day == date(2024, 5, 3)
    assert type(previous_day) is date


def test_month_business_day_helpers_preserve_date_type_for_date_inputs():
    first_holiday = date(2024, 6, 3)
    last_holiday = date(2024, 8, 30)

    first_day = Temporis.first_business_day_of_month(date(2024, 6, 20), [first_holiday])
    last_day = Temporis.last_business_day_of_month(date(2024, 8, 1), [last_holiday])

    assert first_day == date(2024, 6, 4)
    assert type(first_day) is date
    assert last_day == date(2024, 8, 29)
    assert type(last_day) is date


@pytest.mark.parametrize(
    ("operation", "date_input", "date_expected", "datetime_input", "datetime_expected"),
    [
        (
            lambda value: Temporis.add_days(value, 2),
            date(2024, 1, 15),
            date(2024, 1, 17),
            datetime(2024, 1, 15, 9, 30),
            datetime(2024, 1, 17, 9, 30),
        ),
        (
            lambda value: Temporis.add_months(value, 2),
            date(2024, 1, 31),
            date(2024, 3, 31),
            datetime(2024, 1, 31, 9, 30),
            datetime(2024, 3, 31, 9, 30),
        ),
        (
            Temporis.next_quarter,
            date(2024, 11, 15),
            date(2025, 1, 1),
            datetime(2024, 11, 15, 9, 30),
            datetime(2025, 1, 1, 9, 30),
        ),
        (
            Temporis.next_semester,
            date(2024, 11, 15),
            date(2025, 1, 1),
            datetime(2024, 11, 15, 9, 30),
            datetime(2025, 1, 1, 9, 30),
        ),
        (
            Temporis.next_year,
            date(2024, 11, 15),
            date(2025, 1, 1),
            datetime(2024, 11, 15, 9, 30),
            datetime(2025, 1, 1, 9, 30),
        ),
        (
            Temporis.first_day_of_month,
            date(2024, 5, 18),
            date(2024, 5, 1),
            datetime(2024, 5, 18, 9, 30),
            datetime(2024, 5, 1, 9, 30),
        ),
        (
            Temporis.last_day_of_month,
            date(2024, 12, 15),
            date(2024, 12, 31),
            datetime(2024, 12, 15, 9, 30),
            datetime(2024, 12, 31, 9, 30),
        ),
    ],
)
def test_calendar_transformers_accept_date_like_inputs_and_preserve_runtime_type(
    operation, date_input, date_expected, datetime_input, datetime_expected
):
    date_result = operation(date_input)
    datetime_result = operation(datetime_input)

    assert date_result == date_expected
    assert type(date_result) is date
    assert datetime_result == datetime_expected
    assert type(datetime_result) is datetime


def test_count_days_between_accepts_homogeneous_date_inputs():
    assert Temporis.count_days_between(date(2024, 1, 1), date(2024, 1, 10)) == 9


def test_count_days_between_keeps_native_mixed_type_error():
    with pytest.raises(TypeError):
        Temporis.count_days_between(date(2024, 1, 1), datetime(2024, 1, 10, 9, 30))


@pytest.mark.parametrize(
    ("method", "amount"),
    [
        (Temporis.add_seconds, 1),
        (Temporis.add_minutes, 1),
        (Temporis.add_hours, 1),
    ],
)
def test_time_arithmetic_methods_remain_datetime_only(method, amount):
    with pytest.raises(TypeError):
        method(date(2024, 1, 1), amount)
