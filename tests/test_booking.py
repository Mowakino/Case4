import pytest
from src.booking import calculate_booking_fee

# TC01 - Harga Standard Weekday normal
def test_TC01():
    assert calculate_booking_fee(30, "Standard", "Weekday", 3) == 300.0

# TC02 - Anak di bawah 5 tahun gratis
def test_TC02():
    assert calculate_booking_fee(4, "Standard", "Weekday", 2) == 0.0

# TC03 - Umur pas 5 tahun (bayar normal)
def test_TC03():
    assert calculate_booking_fee(5, "Standard", "Weekday", 2) == 200.0

# TC04 - Family room + Weekend surcharge (+20%)
def test_TC04():
    assert calculate_booking_fee(35, "Family", "Weekend", 5) == 900.0

# TC09 & Validasi Durasi Inap - Di atas 14 malam
def test_invalid_duration_above_max():
    with pytest.raises(ValueError):
        calculate_booking_fee(
            guest_age=25,
            room_type="Standard",
            booking_day="Weekday",
            stay_duration=15
        )

# Validasi Durasi Inap - Di bawah 1 malam
def test_invalid_duration_below_min():
    with pytest.raises(ValueError):
        calculate_booking_fee(
            guest_age=25,
            room_type="Standard",
            booking_day="Weekday",
            stay_duration=0
        )

# TC10 — Invalid Age (Usia negatif)
def test_invalid_age_negative():
    with pytest.raises(ValueError):
        calculate_booking_fee(
            guest_age=-1,
            room_type="Standard",
            booking_day="Weekday",
            stay_duration=3
        )
