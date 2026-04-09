import zoneinfo
from datetime import datetime

from temporis.zones import TemporisZone


class TemporisTz:
    """
    A class to handle timezone-related operations.
    """

    __tz_utc = None

    def __init__(self, tz_info: str = TemporisZone.OTHER.UTC):
        """
        Initializes the TemporisTz class with the given timezone information.

        Parameters:
        -----------
        tz_info : str
            The timezone information to use (default is TemporisZone.OTHER.UTC).
        """
        self.tz_info = zoneinfo.ZoneInfo(tz_info)

    def now(self):
        """
        Returns the current datetime in the configured timezone.

        Returns:
        --------
        datetime
            The current date and time in the specified timezone.
        """
        return datetime.now(self.tz_info)

    def apply(self, dt: datetime):
        """
        Converts a datetime to the configured timezone.

        Parameters:
        -----------
        dt : datetime
            The datetime object to convert.

        Returns:
        --------
        datetime
            The converted datetime object in the specified timezone.
        """
        if dt.tzinfo is None:
            return dt.replace(tzinfo=self.tz_info)
        return dt.astimezone(self.tz_info)

    def replace(self, dt: datetime):
        """
        Replaces the datetime timezone with the configured timezone.

        Parameters:
        -----------
        dt : datetime
            The datetime object to modify.

        Returns:
        --------
        datetime
            The datetime object with the replaced timezone information.
        """
        return self.localize(dt.replace(tzinfo=None))

    def localize(self, dt: datetime):
        """
        Attaches the configured timezone to a naive datetime.

        Parameters:
        -----------
        dt : datetime
            The naive datetime object to localize.

        Returns:
        --------
        datetime
            The localized datetime object in the specified timezone.
        """
        return dt.replace(tzinfo=self.tz_info)

    @classmethod
    def to_UTC(cls, dt):
        """
        Converts a datetime to UTC.

        Parameters:
        -----------
        dt : datetime
            The datetime object to convert.

        Returns:
        --------
        datetime
            The converted datetime object in UTC timezone.
        """
        return dt.astimezone(zoneinfo.ZoneInfo(TemporisZone.OTHER.UTC))
