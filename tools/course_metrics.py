#!/usr/bin/env python3
"""Reprodukovatelné metriky studentského obsahu JS Quest."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSONS = tuple(sorted(ROOT.glob("[0-9][0-9]-*/*.md")))
ACTIVITIES = {
    "predict": "@JSQ.predict",
    "experiment": "@JSQ.experiment",
    "complete_code": "@JSQ.complete",
    "bug_hunt": "@JSQ.bug",
    "quick_quiz": "@JSQ.quiz",
    "mission": "@JSQ.mission",
    "bonus": "@JSQ.bonus",
    "boss": "@JSQ.boss",
    "flag": "@JSQ.flag",
}


def count(marker: str, texts: list[str]) -> int:
    return sum(text.count(marker) for text in texts)


def main() -> None:
    texts = [path.read_text(encoding="utf-8") for path in LESSONS]
    worlds = sorted({path.parent.name.split("-", maxsplit=1)[0] for path in LESSONS})
    metrics = {
        "worlds": len(worlds),
        "student_lessons": len(LESSONS),
        **{name: count(marker, texts) for name, marker in ACTIVITIES.items()},
        "p5_interactive_blocks": count("@P5.eval", texts),
        "web_dom_activities": count("@WebDev.HTML_JS", texts),
        # A pure-JS runner is intentionally not introduced without a separately
        # verified official LiaScript template. Static JS examples are not counted.
        "pure_js_interactive_blocks": 0,
    }
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
