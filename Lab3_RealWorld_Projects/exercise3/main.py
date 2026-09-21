"""
Exercise 3 - Intelligent Equipment Monitoring Pipeline
Student: SANTARIN
Seed: 65
Favorite artist: UNCLE DAGS
"""

from telemetry import generate_telemetry
from diagnostics import process_stream


LAST_NAME = "SANTARIN"
SEED_NUM = 65
FAVORITE_ARTIST = "UNCLE DAGS"


def main():
    print("=== EXERCISE 3: INTELLIGENT EQUIPMENT MONITORING PIPELINE ===")
    print(
        f"Student-Specific Inputs: LAST_NAME={LAST_NAME}, "
        f"SEED_NUM={SEED_NUM}, FAVORITE_ARTIST={FAVORITE_ARTIST}"
    )

    # Required lambda: transform each valid telemetry value.
    calibration = lambda value: round(value * 1.065, 2)

    generated = list(
        generate_telemetry(
            LAST_NAME, SEED_NUM, FAVORITE_ARTIST, count=10
        )
    )

    print("\nGenerated Telemetry Data:")
    print([item["value"] for item in generated])

    # A fresh generator is used for the actual pipeline.
    results, invalid, abnormal = process_stream(
        generate_telemetry(
            LAST_NAME, SEED_NUM, FAVORITE_ARTIST, count=10
        ),
        calibration
    )

    print("\nValid/Invalid Results:")
    print(f"Valid readings: {len(results)}")
    for sensor, raw, processed, status in results:
        print(f"  Sensor {sensor}: {raw} -> {processed} -> {status}")

    print(f"Invalid readings: {len(invalid)}")
    for sensor, value, error in invalid:
        print(f"  Sensor {sensor}: {value} -> INVALID ({error})")

    print("\nProcessed Results:")
    for sensor, raw, processed, status in results:
        print(f"  Sensor {sensor}: processed={processed}, status={status}")

    print("\nRecursive Analysis:")
    for sensor, value, trace in abnormal:
        sequence = " -> ".join(str(v) for _, v in trace)
        print(f"  Sensor {sensor} abnormal value {value}: {sequence}")

    high = sum(status == "HIGH" for _, _, _, status in results)
    normal = sum(status == "NORMAL" for _, _, _, status in results)
    low = sum(status == "LOW" for _, _, _, status in results)

    overall = "ABNORMAL" if invalid or high or low else "NORMAL"

    print("\nFinal Diagnostic Summary:")
    print(f"Number of processed readings: {len(generated)}")
    print(f"Valid: {len(results)}")
    print(f"Invalid: {len(invalid)}")
    print(f"Detected abnormal conditions: {len(abnormal)}")
    print(f"Classification: LOW={low}, NORMAL={normal}, HIGH={high}")
    print(f"Overall equipment status: {overall}")

    print("\nExecution Log:")
    print("  Generator produced telemetry values one at a time.")
    print("  Lambda calibration was applied to valid readings.")
    print("  Decorator monitored the main processing function.")
    print("  Exception handling skipped invalid readings without stopping.")
    print("  Recursion traced the detected abnormal condition to its base case.")

    print("\nFinal Output:")
    print(f"Equipment status: {overall}")
    print(
        f"Processed={len(generated)}, Valid={len(results)}, "
        f"Invalid={len(invalid)}, Abnormal={len(abnormal)}"
    )


if __name__ == "__main__":
    main()
