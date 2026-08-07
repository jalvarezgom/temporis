from datetime import datetime, date, timezone

import pytest

from temporis.timezone import TemporisTz
from temporis.zones import TemporisZone


@pytest.fixture
def temporis_tz():
    return TemporisTz()


def test_initialization_with_default_timezone():
    tz = TemporisTz()
    assert tz.tz_info.key == TemporisZone.OTHER.UTC


def test_initialization_with_specific_timezone():
    tz = TemporisTz(TemporisZone.AMERICA.NEW_YORK)
    assert tz.tz_info.key == TemporisZone.AMERICA.NEW_YORK


def test_now_in_specified_timezone(temporis_tz):
    now = temporis_tz.now()
    assert now.tzinfo == temporis_tz.tz_info


def test_apply_converts_datetime_to_specified_timezone(temporis_tz):
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    converted = temporis_tz.apply(dt)
    assert converted.tzinfo == temporis_tz.tz_info


def test_apply_localizes_naive_datetime(temporis_tz):
    dt = datetime(2023, 1, 1)
    converted = temporis_tz.apply(dt)
    assert converted.tzinfo == temporis_tz.tz_info


def test_to_UTC_converts_datetime_to_utc(temporis_tz):
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    utc_dt = temporis_tz.to_UTC(dt)
    assert str(utc_dt.tzinfo) == str(timezone.utc)


def test_apply_and_localize(temporis_tz):
    dt = datetime(2023, 1, 1)
    converted = temporis_tz.apply(dt)
    localized = temporis_tz.localize(dt)
    assert localized.tzinfo == converted.tzinfo


def test_replace(temporis_tz):
    tz = TemporisTz(TemporisZone.AMERICA.NEW_YORK)
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    replaced = tz.replace(dt)
    assert dt.hour == replaced.hour
    assert replaced.tzinfo != temporis_tz.tz_info


def test_timezone_apply_rejects_date_inputs(temporis_tz):
    with pytest.raises(AttributeError):
        temporis_tz.apply(date(2024, 1, 1))


def test_to_UTC_assumes_naive_datetime_is_utc(temporis_tz):
    dt = datetime(2024, 1, 1, 12, 0)
    utc_dt = temporis_tz.to_UTC(dt)
    assert str(utc_dt.tzinfo) == str(timezone.utc)
    assert utc_dt.hour == 12
