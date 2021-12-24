from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

from services import week_number

app = FastAPI()


class WeekNumber(BaseModel):
    week_number: int
    date: date


@app.get("/")
def get_week_number(date: date):
    """Handler to get week number by date."""
    week = week_number(date)
    return WeekNumber(week_number=week, date=date)
