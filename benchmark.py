import json
import math
import time
from pathlib import Path


submission_path = Path("submission/score.txt")
score_path = Path("score.json")

verification_started = time.perf_counter_ns()
score = float(submission_path.read_text(encoding="utf-8").strip())
if not math.isfinite(score):
    raise ValueError(f"{submission_path} must contain one finite number")
verification_time_ms = (time.perf_counter_ns() - verification_started) / 1_000_000

result = {
    "score": score,
    "metrics": {"verificationTimeMs": verification_time_ms},
}
score_path.write_text(json.dumps(result) + "\n", encoding="utf-8")
print(f"score: {score}")
