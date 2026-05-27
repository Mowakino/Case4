def hotel_booking_price(
    guest_age: int,
    room_type: str,
    booking_day: str,
    stay_duration: int,
) -> float:
    """
    Compute hotel booking price based on business rules.
    - Children under 5 stay free
    - Standard room: $100/night, max 2 guests
    - Family room: $150/night, max 5 guests
    - Weekend booking: +20%
    - Holiday season: +40%
    - Booking duration: 1-14 nights
    """
    # Validasi age
    if guest_age < 0:
        raise ValueError("Invalid age: age cannot be negative.")

    # Validasi duration
    if stay_duration < 1 or stay_duration > 14:
        raise ValueError("Invalid duration: stay must be between 1 and 14 nights.")

    # Anak di bawah 5 tahun gratis
    if guest_age < 5:
        return 0.0

    # Base rate per malam
    base_rate = 100.0 if room_type == "standard" else 150.0

    # Hitung subtotal
    subtotal = base_rate * stay_duration

    # Surcharge
    if booking_day == "weekend":
        subtotal *= 1.20
    elif booking_day == "holiday":
        subtotal *= 1.40

    return round(subtotal, 2)
    # """Compute total booking price per the project specification.

    # - Children under 5 stay for free.
    # - Room rates: Standard=100/night, Family=150/night.
    # - Weekend: +20%%, Holiday: +40%% surcharge.
    # - stay_duration must be between 1 and 14 inclusive.
    # - guest_age must be between 0 and 120 inclusive.
    # """
    # if not isinstance(guest_age, int):
    #     raise TypeError("guest_age must be int")
    # if guest_age < 0 or guest_age > 120:
    #     raise ValueError("Invalid guest age")

    # if not isinstance(stay_duration, int):
    #     raise TypeError("stay_duration must be int")
    # if stay_duration < 1 or stay_duration > 14:
    #     raise ValueError("Invalid stay duration")

    # if not isinstance(room_type, str) or not room_type:
    #     raise ValueError("Invalid room type")
    # room_type = room_type.strip().capitalize()
    # if room_type not in ("Standard", "Family"):
    #     raise ValueError("Invalid room type")

    # if not isinstance(booking_day, str) or not booking_day:
    #     raise ValueError("Invalid booking day")
    # booking_day = booking_day.strip().capitalize()
    # if booking_day not in ("Weekday", "Weekend", "Holiday"):
    #     raise ValueError("Invalid booking day")

    # # Children under 5 stay free
    # if guest_age < 5:
    #     return 0.0

    # rates = {"Standard": 100.0, "Family": 150.0}
    # total = rates[room_type] * stay_duration

    # if booking_day == "Weekend":
    #     total *= 1.20
    # elif booking_day == "Holiday":
    #     total *= 1.40

    # return round(total, 2)
