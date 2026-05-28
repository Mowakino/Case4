import pytest
from src.booking import hotel_booking_price



# TC03 - Umur pas 5 tahun (bayar normal)
def test_TC03():
    assert hotel_booking_price(5, "Standard", "Weekday", 2) == 200.0

# TC04 - Family room + Weekend surcharge (+20%)
def test_TC04():
    assert hotel_booking_price(35, "Family", "Weekend", 5) == 900.0

# TC05 - Holiday surcharge
def test_TC05_holiday_surcharge():
    result = hotel_booking_price(40, "Family", "Holiday", 7)
    assert result == 1470.0

# TC06 - Minimum duration boundary
def test_TC06_minimum_duration_boundary():
    result = hotel_booking_price(25, "Standard", "Weekday", 1)
    assert result == 100.0

# TC09 & Validasi Durasi Inap - Di atas 14 malam
def test_invalid_duration_above_max():
    with pytest.raises(ValueError):
        hotel_booking_price(
            guest_age=25,
            room_type="Standard",
            booking_day="Weekday",
            stay_duration=15
        )

# Validasi Durasi Inap - Di bawah 1 malam 
def test_invalid_duration_below_min():
    with pytest.raises(ValueError):
        hotel_booking_price(
            guest_age=25,
            room_type="Standard",
            booking_day="Weekday",
            stay_duration=0
        )

# TC10 — Invalid Age (Usia negatif)
def test_invalid_age_negative():
    with pytest.raises(ValueError):
        hotel_booking_price(
            guest_age=-1,
            room_type="Standard",
            booking_day="Weekday",
            stay_duration=3
        )