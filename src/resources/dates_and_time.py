from datetime import date
import calendar

def prev_month():
    today = date.today()
    if today.month == 1:
        prev_month = 12
        prev_year = today.year - 1
    else:
        prev_month = today.month - 1
        prev_year = today.year

    prev_month_name = calendar.month_name[prev_month]  # e.g., "January"

    return prev_month_name, prev_year


def next_month():
    today = date.today()