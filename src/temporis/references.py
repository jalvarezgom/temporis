from enum import StrEnum


class TemporisReference(StrEnum):
    WEEKDAYS_NAME = (
        "%A"  # Example: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    )
    WEEKDAYS_SHORT_NAME = "%a"  # Example: Mon, Tue, Wed, Thu, Fri, Sat, Sun
    WEEKDAYS_NUMBER = "%w"  # Example: 0, 1, 2, 3, 4, 5, 6
    WEEK_OF_YEAR = (
        "%W"  # Example: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, ..., 51, 52
    )
    WEEK_OF_YEAR_SUNDAY = (
        "%U"  # Example: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, ..., 51, 52
    )
    DAY_OF_MONTH = "%d"  # Example: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11
    DAY_OF_YEAR = "%j"  # Example: 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, ..., 365, 366
    MONTH_NAME = "%B"  # Example: January, February, March, April, May, June, July, August, September, October, November, December
    MONTH_SHORT_NAME = (
        "%b"  # Example: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
    )
    MONTH_NUMBER = "%m"  # Example: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
    YEAR = "%Y"  # Example: 2021, 2022, 2023, 2024, 2025
    YEAR_SHORT = "%y"  # Example: 21, 22, 23, 24, 25
    HOUR_24 = "%H"  # Example: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16
    HOUR_12 = "%I"  # Example: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
    AM_PM = "%p"  # Example: AM, PM
    MINUTE = "%M"  # Example: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16
    SECOND = "%S"  # Example: 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16
    MICROSECOND = (
        "%f"  # Example: 000000, 000001, 000002, 000003, 000004, 000005, 000006
    )
    UTC_OFFSET = "%z"  # Example: +0000, -0000
    TIMEZONE_NAME = "%Z"  # Example: UTC, GMT, EST, CST, MST, PST
    LOCAL_DATE = "%x"  # Example: 09/30/13
    LOCAL_TIME = "%X"  # Example: 07:06:05
    LOCAL_DATE_TIME = "%c"  # Example: Mon Sep 30 07:06:05 2013
    ISO_8601_YEAR = "%G"  # Example: 2021, 2022, 2023, 2024, 2025
    ISO_8601_WEEKDAY = "%u"  # Example: 1, 2, 3, 4, 5, 6, 7
    ISO_8601_WEEK = (
        "%V"  # Example: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, ..., 51, 52
    )
