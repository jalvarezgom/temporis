import zoneinfo

from temporis.zones import TemporisZone


def test_singapore_is_only_defined_in_asia():
    assert TemporisZone.ASIA.SINGAPORE == "Asia/Singapore"
    assert not hasattr(TemporisZone.EUROPE, "SINGAPURE")


def test_common_zones_are_valid_zoneinfo():
    zoneinfo.ZoneInfo(TemporisZone.EUROPE.MADRID)
    zoneinfo.ZoneInfo(TemporisZone.AMERICA.NEW_YORK)
    zoneinfo.ZoneInfo(TemporisZone.ASIA.SINGAPORE)
    zoneinfo.ZoneInfo(TemporisZone.ETC.UTC)
    zoneinfo.ZoneInfo(TemporisZone.OTHER.UTC)
