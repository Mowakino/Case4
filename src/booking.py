MIN_AGE = 0
MAX_AGE = 120

MIN_STAY = 1
MAX_STAY = 14

BASE_PRICE = {
    "Standard": 100.0,
    "Family": 150.0
}

SURCHARGE = {
    "Weekday": 0.0,
    "Weekend": 0.20,
    "Holiday": 0.40
}


def normalize_text(text):
    return text.strip().capitalize()


def validate_guest_age(age):
    if not isinstance(age, int):
        raise TypeError("guest_age must be int")

    if not (MIN_AGE <= age <= MAX_AGE):
        raise ValueError("Invalid guest age")


def validate_stay_duration(duration):
    if not isinstance(duration, int):
        raise TypeError("stay_duration must be int")

    if not (MIN_STAY <= duration <= MAX_STAY):
        raise ValueError("Invalid stay duration")


def validate_room_type(room_type):
    if not isinstance(room_type, str) or not room_type:
        raise ValueError("Invalid room type")

    room_type = normalize_text(room_type)

    if room_type not in BASE_PRICE:
        raise ValueError("Invalid room type")

    return room_type


def validate_booking_day(booking_day):
    if not isinstance(booking_day, str) or not booking_day:
        raise ValueError("Invalid booking day")

    booking_day = normalize_text(booking_day)

    if booking_day not in SURCHARGE:
        raise ValueError("Invalid booking day")

    return booking_day


def calculate_price(room_type, booking_day, stay_duration):
    base = BASE_PRICE[room_type]
    surcharge = SURCHARGE[booking_day]

    return base * (1 + surcharge) * stay_duration


def hotel_booking_price(
    guest_age: int,
    room_type: str,
    booking_day: str,
    stay_duration: int
) -> float:

    validate_guest_age(guest_age)
    validate_stay_duration(stay_duration)

    room_type = validate_room_type(room_type)
    booking_day = validate_booking_day(booking_day)

    # Children under 5 stay free
    if guest_age < 5:
        return 0.0

    total = calculate_price(
        room_type,
        booking_day,
        stay_duration
    )

    return round(total, 2)


calculate_booking_fee = hotel_booking_price