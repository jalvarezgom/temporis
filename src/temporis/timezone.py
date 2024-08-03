import zoneinfo
from temporis.temporis import datetime
from temporis.zones import TemporisZone


class TemporisTz:
    __tz_utc = None

    def __init__(self, tz_info: str = TemporisZone.OTHER.UTC):
        self.tz_info = zoneinfo.ZoneInfo(tz_info)

    def now(self):
        return datetime.now(self.tz_info)

    def apply(self, dt):
        return dt.astimezone(self.tz_info)

    @classmethod
    def to_UTC(cls, dt):
        return dt.astimezone(zoneinfo.ZoneInfo(TemporisZone.OTHER.UTC))
