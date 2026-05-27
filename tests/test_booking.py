import pytest
from src.booking import calculate_booking_fee

# Test untuk batas bawah (kurang dari 1 hari)
def test_stay_duration_less_than_one():
    with pytest.raises(ValueError, match="Booking duration must be between 1 and 14 nights"):
        # Kita isi parameter lain dengan nilai standar saja
        calculate_booking_fee(guest_age=30, room_type="standard", booking_day="weekday", stay_duration=0)

# Test untuk batas atas (lebih dari 14 hari)
def test_stay_duration_more_than_fourteen():
    with pytest.raises(ValueError, match="Booking duration must be between 1 and 14 nights"):
        calculate_booking_fee(guest_age=30, room_type="standard", booking_day="weekday", stay_duration=15)

def test_stay_duration_valid():
    result = calculate_booking_fee(guest_age=30, room_type="standard", booking_day="weekday", stay_duration=5)
    assert result == "Valid booking"
