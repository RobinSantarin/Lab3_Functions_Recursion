"""
Exercise 1 - Equipment Diagnostic System
Student: SANTARIN
Seed: 65
Favorite artist: UNCLE DAGS
"""

LAST_NAME = "SANTARIN"
SEED_NUM = 65
FAVORITE_ARTIST = "UNCLE DAGS"


def generate_readings(last_name, seed_num, favorite_artist):
    name_value = sum(ord(c) for c in last_name)
    artist_value = sum(ord(c) for c in favorite_artist)
    base = name_value + seed_num + artist_value

    readings = []
    for i in range(1, 7):
        value = 50 + ((base + i * seed_num + artist_value) % 71)
        if i == 3:
            value = -5
        readings.append(round(value, 2))
    return readings


def validate_reading(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Reading must be numeric.")
    if value < 0 or value > 120:
        raise ValueError(f"Reading {value} is outside the valid range 0-120.")
    return True


def calculate_reading(value, seed_num):
    return round(value * (1 + seed_num / 1000), 2)


def classify_reading(value):
    if value < 40:
        return "LOW"
    if value <= 80:
        return "NORMAL"
    return "HIGH"


def diagnostic_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed {func.__name__}")
        return result
    return wrapper


@diagnostic_logger
def process_readings(readings):
    valid, invalid = [], []
    for index, reading in enumerate(readings, start=1):
        try:
            validate_reading(reading)
            calculated = calculate_reading(reading, SEED_NUM)
            status = classify_reading(calculated)
            valid.append((index, reading, calculated, status))
        except (TypeError, ValueError) as exc:
            invalid.append((index, reading, str(exc)))
    return valid, invalid


def main():
    readings = generate_readings(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)

    print("=== EXERCISE 1: EQUIPMENT DIAGNOSTIC SYSTEM ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")
    print(f"Generated Equipment Data: {readings}")

    valid, invalid = process_readings(readings)

    print("\nValidation Results:")
    print(f"Valid readings: {len(valid)}")
    print(f"Invalid readings: {len(invalid)}")
    for item in invalid:
        print(f"  Reading {item[0]} = {item[1]} -> INVALID ({item[2]})")

    print("\nDiagnostic Results:")
    for index, raw, calculated, status in valid:
        print(f"  Reading {index}: {raw:.2f} -> calibrated {calculated:.2f} -> {status}")

    high = sum(1 for x in valid if x[3] == "HIGH")
    low = sum(1 for x in valid if x[3] == "LOW")
    normal = sum(1 for x in valid if x[3] == "NORMAL")
    overall = "ABNORMAL" if high or low or invalid else "NORMAL"

    print("\nFinal Output:")
    print(f"Processed readings: {len(readings)}")
    print(f"Valid: {len(valid)} | Invalid: {len(invalid)}")
    print(f"Classification: LOW={low}, NORMAL={normal}, HIGH={high}")
    print(f"Overall equipment status: {overall}")


if __name__ == "__main__":
    main()
