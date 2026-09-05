import json
import math
import time
from pathlib import Path


submission_path = Path("submission/score.txt")
numbers_path = Path("numbers")
score_path = Path("score.json")


def read_number(path: Path) -> float:
    try:
        value = float(path.read_text(encoding="utf-8").strip())
    except ValueError as error:
        raise ValueError(f"{path} must contain one finite number") from error
    if not math.isfinite(value):
        raise ValueError(f"{path} must contain one finite number")
    return value


verification_started = time.perf_counter_ns()
number_paths = [
    submission_path,
    *(path for path in sorted(numbers_path.rglob("*")) if path.is_file()),
]
score = 2 * math.fsum(read_number(path) for path in number_paths)
verification_time_ms = (time.perf_counter_ns() - verification_started) / 1_000_000

result = {
    "score": score,
    "metrics": {
        "verificationTimeMs": verification_time_ms,
        "numberFileCount": len(number_paths),
    },
}
score_path.write_text(json.dumps(result) + "\n", encoding="utf-8")
print(f"score: {score}")
