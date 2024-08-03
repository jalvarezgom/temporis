from temporis.references import TemporisReference as DT_REF


class TemporisFormat:
    MONTH_NAME = f"{DT_REF.MONTH_NAME}"
    YEAR_MONTH_DAY = f"{DT_REF.YEAR}-{DT_REF.MONTH_NUMBER}-{DT_REF.DAY_OF_MONTH}"
    YEAR_MONTH_DAY_HOUR_MINUTE = f"{YEAR_MONTH_DAY} {DT_REF.HOUR_24}:{DT_REF.MINUTE}"
    YEAR_MONTH_DAY_HOUR_MINUTE_SECOND = f"{YEAR_MONTH_DAY_HOUR_MINUTE}:{DT_REF.SECOND}"
    TIMESTAMP_DATE_FILENAME = f"{DT_REF.YEAR}{DT_REF.MONTH_NUMBER}{DT_REF.DAY_OF_MONTH}"
    TIMESTAMP_DATETIME_FILENAME = (
        f"{TIMESTAMP_DATE_FILENAME}{DT_REF.HOUR_24}{DT_REF.MINUTE}{DT_REF.SECOND}"
    )
    ISOFORMAT = f"{YEAR_MONTH_DAY}T{DT_REF.HOUR_24}:{DT_REF.MINUTE}:{DT_REF.SECOND}.{DT_REF.MICROSECOND}"
    WITH_TZINFO = f"{YEAR_MONTH_DAY_HOUR_MINUTE_SECOND}%z"

    __exclude__ = {"ISOFORMAT"}

    def __init__(self, datetime_delimiter: str | None = None):
        self.DATETIME_DELIMITER = datetime_delimiter
        if self.DATETIME_DELIMITER:
            for name in self.__keys__().difference(self.__exclude__):
                setattr(
                    self,
                    name,
                    getattr(self, name).replace("-", self.DATETIME_DELIMITER),
                )

    def __keys__(self) -> set[str]:
        return set(name for name in dir(self) if not name.startswith("_"))
