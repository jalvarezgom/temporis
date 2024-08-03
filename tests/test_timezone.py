import zoneinfo
from datetime import datetime, timezone

import pytest

from temporis.timezone import TemporisTz
from temporis.zones import TemporisZone


@pytest.fixture
def temporis_tz():
    return TemporisTz()


def test_initialization_with_default_timezone():
    print(zoneinfo.available_timezones())
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


def test_to_UTC_converts_datetime_to_utc(temporis_tz):
    dt = datetime(2023, 1, 1, tzinfo=timezone.utc)
    utc_dt = temporis_tz.to_UTC(dt)
    assert str(utc_dt.tzinfo) == str(timezone.utc)
