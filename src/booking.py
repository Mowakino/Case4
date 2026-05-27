BASE_PRICE = {
    "Standard": 100.0,
    "Family":   150.0,
}

SURCHARGE = {
    "Weekday": 0.0,
    "Weekend": 0.20,
    "Holiday": 0.40,
}

def hotel_booking_price(
    guest_age: int,
    room_type: str,
    booking_day: str,
    stay_duration: int,
) -> float:
    """
    Compute total booking price per the project specification.

    - Children under 5 stay for free.
    - Room rates: Standard=100/night, Family=150/night.
    - Weekend: +20%%, Holiday: +40%% surcharge.
    - stay_duration must be between 1 and 14 inclusive.
    - guest_age must be between 0 and 120 inclusive.
    """

    # Validate guest_age
    if not isinstance(guest_age, int):
        raise TypeError("guest_age must be int")
    if guest_age < 0 or guest_age > 120:
        raise ValueError("Invalid guest age")

    # Validate stay_duration
    if not isinstance(stay_duration, int):
        raise TypeError("stay_duration must be int")
    if stay_duration < 1 or stay_duration > 14:
        raise ValueError("Invalid stay duration")

    # Validate room_type
    if not isinstance(room_type, str) or not room_type:
        raise ValueError("Invalid room type")
    room_type = room_type.strip().capitalize()
    if room_type not in BASE_PRICE:
        raise ValueError("Invalid room type")

    # Validate booking_day
    if not isinstance(booking_day, str) or not booking_day:
        raise ValueError("Invalid booking day")
    booking_day = booking_day.strip().capitalize()
    if booking_day not in SURCHARGE:
        raise ValueError("Invalid booking day")

    # Children under 5 stay free
    if guest_age < 5:
        return 0.0

    total = BASE_PRICE[room_type] * stay_duration
    if booking_day == "Weekend":
        total *= 1.20
    elif booking_day == "Holiday":
        total *= 1.40

    return round(total, 2)