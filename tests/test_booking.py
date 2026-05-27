import pytest
from src.booking import hotel_booking_price

def test_TC05_holiday_surcharge():
    result = hotel_booking_price(40, "Family", "Holiday", 7)
    assert result == 1470.0

def test_TC06_minimum_duration_boundary():
    result = hotel_booking_price(25, "Standard", "Weekday", 1)
    assert result == 100.0