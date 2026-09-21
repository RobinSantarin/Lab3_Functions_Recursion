"""Telemetry generation module for Exercise 3."""

def generate_telemetry(last_name, seed_num, favorite_artist, count=10):
    """Generator: yields one telemetry record at a time."""
    name_value = sum(ord(c) for c in last_name)
    artist_value = sum(ord(c) for c in favorite_artist)
    base = name_value + artist_value + seed_num

    for i in range(1, count + 1):
        raw = 50 + ((base + i * 17 + seed_num) % 71)

        # Deliberate invalid/abnormal cases for exception handling.
        if i == 4:
            raw = 135
        elif i == 8:
            raw = -8

        yield {"sensor": i, "value": raw}
