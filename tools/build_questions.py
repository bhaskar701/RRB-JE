from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "data" / "questions.json"
dst = ROOT / "data" / "questions.v2.min.json"

with src.open("r", encoding="utf-8") as f:
    questions = json.load(f)

if not isinstance(questions, list):
    raise ValueError("questions.json must contain a JSON array")

for i, q in enumerate(questions, 1):
    required = ["section", "topic", "question", "options", "answer", "date", "shift"]
    missing = [k for k in required if k not in q]
    if missing:
        raise ValueError(f"Question {i} is missing: {', '.join(missing)}")
    if not isinstance(q["options"], list) or len(q["options"]) != 4:
        raise ValueError(f"Question {i} must have exactly 4 options")
    if q["answer"] not in range(4):
        raise ValueError(f"Question {i} has an answer index outside 0–3")
    if q["section"] not in {"numerical", "reasoning", "science"}:
        raise ValueError(f"Question {i} has an invalid section: {q['section']}")

with dst.open("w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, separators=(",", ":"))

print(f"Built {len(questions)} questions -> {dst}")
