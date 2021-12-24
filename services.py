import calendar

from datetime import date, datetime, timedelta

calendar.setfirstweekday(calendar.SUNDAY)


def week_number(target_date: date) -> int:
    """
    Calculates week number.

    Week starts from first day of the year. Next week starts from sunday.
    Examples:
    - 2019-1-5, saturday -> 1
    - 2019-1-6, sunday -> 2
    """
    weekday_1_january = (datetime(target_date.year, 1, 1).weekday() + 1) % 7
    start_week_date = datetime(target_date.year, 1, 1) - timedelta(
        days=weekday_1_january
    )
    return (
        datetime(target_date.year, target_date.month, target_date.day) - start_week_date
    ).days // 7 + 1
