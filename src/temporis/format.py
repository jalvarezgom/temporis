from temporis.references import TemporisReference as DT_REF


class TemporisFormat:
    """
    A class to format date and time strings based on predefined templates.

    Attributes:
    -----------
    MONTH_NAME : str
        The name of the month.
    YEAR_MONTH_DAY : str
        The date format in 'YYYY-MM-DD'.
    YEAR_MONTH_DAY_HOUR_MINUTE : str
        The date and time format in 'YYYY-MM-DD HH:MM'.
    YEAR_MONTH_DAY_HOUR_MINUTE_SECOND : str
        The date and time format in 'YYYY-MM-DD HH:MM:SS'.
    YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_TZ : str
        The date and time format with timezone in 'YYYY-MM-DD HH:MM:SS%z'.
    TIMESTAMP_DATE_FILENAME : str
        The date format for filenames in 'YYYYMMDD'.
    TIMESTAMP_DATETIME_FILENAME : str
        The date and time format for filenames in 'YYYYMMDDHHMMSS'.
    ISOFORMAT : str
        The ISO 8601 date and time format in 'YYYY-MM-DDTHH:MM:SS.mmmmmm'.
    ISOFORMAT_WITHOUT_MICROSECOND : str
        The ISO 8601 date and time format in 'YYYY-MM-DDTHH:MM:SS'.
    WITH_TZINFO : str
        The date and time format with timezone in 'YYYY-MM-DD HH:MM:SS%z'.
    __exclude__ : set
        A set of format names to exclude from delimiter replacement.
    """

    MONTH_NAME = f"{DT_REF.MONTH_NAME}"
    YEAR_MONTH_DAY = f"{DT_REF.YEAR}-{DT_REF.MONTH_NUMBER}-{DT_REF.DAY_OF_MONTH}"
    YEAR_MONTH_DAY_HOUR_MINUTE = f"{YEAR_MONTH_DAY} {DT_REF.HOUR_24}:{DT_REF.MINUTE}"
    YEAR_MONTH_DAY_HOUR_MINUTE_SECOND = f"{YEAR_MONTH_DAY_HOUR_MINUTE}:{DT_REF.SECOND}"
    YEAR_MONTH_DAY_HOUR_MINUTE_SECOND_TZ = f"{YEAR_MONTH_DAY_HOUR_MINUTE_SECOND}%z"
    TIMESTAMP_DATE_FILENAME = f"{DT_REF.YEAR}{DT_REF.MONTH_NUMBER}{DT_REF.DAY_OF_MONTH}"
    TIMESTAMP_DATETIME_FILENAME = (
        f"{TIMESTAMP_DATE_FILENAME}{DT_REF.HOUR_24}{DT_REF.MINUTE}{DT_REF.SECOND}"
    )
    ISOFORMAT_WITHOUT_MICROSECOND = f"{YEAR_MONTH_DAY}T{DT_REF.HOUR_24}:{DT_REF.MINUTE}:{DT_REF.SECOND}"
    ISOFORMAT = f"{ISOFORMAT_WITHOUT_MICROSECOND}.{DT_REF.MICROSECOND}"
    WITH_TZINFO = f"{YEAR_MONTH_DAY_HOUR_MINUTE_SECOND}%z"

    __exclude__ = {"ISOFORMAT", "ISOFORMAT_WITHOUT_MICROSECOND"}

    def __init__(self, datetime_delimiter: str | None = None):
        """
        Initializes the format constants with an optional delimiter override.

        Parameters:
        -----------
        datetime_delimiter : str | None
            A string to replace the default '-' delimiter in date-based formats.
        """
        self.DATETIME_DELIMITER = datetime_delimiter
        if self.DATETIME_DELIMITER:
            for name in self.__keys__().difference(self.__exclude__):
                setattr(
                    self,
                    name,
                    getattr(self, name).replace("-", self.DATETIME_DELIMITER),
                )

    def __keys__(self) -> set[str]:
        """
        Returns public attribute names defined on the instance.

        Returns:
        --------
        set[str]
            A set of attribute names.
        """
        return set(name for name in dir(self) if not name.startswith("_"))
