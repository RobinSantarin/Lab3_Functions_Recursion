"""
Exercise 2 - Recursive Fault Trace
Student: SANTARIN
Seed: 65
Favorite artist: UNCLE DAGS
"""

LAST_NAME = "SANTARIN"
SEED_NUM = 65
FAVORITE_ARTIST = "UNCLE DAGS"


def generate_fault_code(last_name, seed_num, favorite_artist):
    name_value = sum(ord(c) for c in last_name)
    artist_value = sum(ord(c) for c in favorite_artist)
    return (name_value * 3 + artist_value * 2 + seed_num) % 900000 + 100000


def recursive_trace(code, trace=None, calls=0):
    if trace is None:
        trace = []

    trace.append(code)
    calls += 1

    if code < 10:
        return trace, calls

    return recursive_trace(code // 10, trace, calls)


def main():
    fault_code = generate_fault_code(
        LAST_NAME, SEED_NUM, FAVORITE_ARTIST
    )
    trace, calls = recursive_trace(fault_code)

    print("=== EXERCISE 2: RECURSIVE FAULT TRACE ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")
    print(f"\nGenerated Fault Data: {fault_code}")

    print("\nRecursive Trace:")
    for level, value in enumerate(trace):
        print(f"  Level {level}: {value}")

    print(f"\nNumber of Recursive Calls: {calls}")

    print("\nExecution Log:")
    print(f"  Fault code generated: {fault_code}")
    print(f"  Recursion started at {fault_code}")
    print(f"  Base condition reached at {trace[-1]}")
    print(f"  Total calls: {calls}")

    print("\nFinal Output:")
    print(f"Fault Trace: {' -> '.join(map(str, trace))}")
    print(f"Final fault level: {trace[-1]}")
    print(f"Total recursive calls: {calls}")


if __name__ == "__main__":
    main()
