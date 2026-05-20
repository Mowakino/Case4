import pytest
from src.booking import calculate_booking

def test_tc03_normal_charge():
    # Umur 5, Standard, Weekday, 2 malam -> Normal charge
    result = calculate_booking(5, "Standard", "Weekday", 2)
    assert result == "Normal charge"

def test_tc04_weekend_surcharge():
    # Umur 35, Family, Weekend, 5 malam -> Weekend surcharge (+20%)
    result = calculate_booking(35, "Family", "Weekend", 5)
    assert result == "Weekend surcharge (+20%)"
    
    def test_invalid_stay_duration():
        with pytest.raises(ValueError):
            calculate_booking(25, "Standard", "Weekday", 15) # 15 malam (Invalid)