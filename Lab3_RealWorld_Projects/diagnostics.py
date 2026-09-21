"""Diagnostic module for Exercise 3."""

def classify(value):
    if value < 40:
        return "LOW"
    if value <= 80:
        return "NORMAL"
    return "HIGH"


def trace_abnormal(value, depth=0, trace=None):
    """Recursively reduce an abnormal value until the base condition."""
    if trace is None:
        trace = []

    trace.append((depth, value))

    if value <= 120:
        return trace

    return trace_abnormal(value - 15, depth + 1, trace)


def monitor(func):
    """Decorator that logs execution of a major processing function."""
    def wrapper(*args, **kwargs):
        print("[DECORATOR] Monitoring diagnostic processing...")
        result = func(*args, **kwargs)
        print("[DECORATOR] Diagnostic processing complete.")
        return result
    return wrapper


@monitor
def process_stream(stream, transform_fn):
    results = []
    invalid = []
    abnormal = []

    for item in stream:
        try:
            value = item["value"]

            if not isinstance(value, (int, float)):
                raise TypeError("Non-numeric telemetry.")

            if value < 0 or value > 120:
                raise ValueError(f"Out-of-range telemetry: {value}")

            processed = transform_fn(value)
            status = classify(processed)
            results.append((item["sensor"], value, processed, status))

        except (TypeError, ValueError) as exc:
            invalid.append((item["sensor"], value, str(exc)))

            if isinstance(value, (int, float)) and value > 120:
                abnormal.append(
                    (item["sensor"], value, trace_abnormal(value))
                )

    return results, invalid, abnormal
