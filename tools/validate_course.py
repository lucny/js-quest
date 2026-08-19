#!/usr/bin/env python3
"""Lehká strukturální kontrola pilotu JS Quest bez vlastního parseru LiaScriptu."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "AGENTS.md",
    "AUTHORING-GUIDE.md",
    "GAME-DESIGN.md",
    "GAME-MACROS.md",
    "README.md",
    "TECHNICAL-NOTES.md",
    "01-variables/01-moving-ball.md",
)
LESSON = ROOT / "01-variables" / "01-moving-ball.md"
MACROS = ROOT / "GAME-MACROS.md"
REQUIRED_MACROS = {
    "styles",
    "predict",
    "experiment",
    "complete",
    "bug",
    "mission",
    "bonus",
    "quiz",
    "boss",
    "flag",
    "xp",
    "codeflag",
    "thinkflag",
    "buildflag",
    "worldflag",
    "world",
}
CARD_MACROS = {
    "predict",
    "experiment",
    "complete",
    "bug",
    "mission",
    "bonus",
    "quiz",
    "boss",
    "flag",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{path.relative_to(ROOT)} není UTF-8.")
        return ""


def validate_fences(path: Path, text: str) -> None:
    open_fence: str | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if not match:
            continue
        fence = match.group(1)
        if open_fence is None:
            open_fence = fence
        elif fence[0] == open_fence[0] and len(fence) >= len(open_fence):
            open_fence = None
    if open_fence is not None:
        fail(f"{path.relative_to(ROOT)} má neuzavřený code fence ({open_fence}).")


def main_header(text: str) -> str | None:
    stripped = text.lstrip("\ufeff\n\r \t")
    if not stripped.startswith("<!--"):
        return None
    end = re.search(r"(?m)^-->\s*$", stripped)
    return stripped[4:end.start()] if end is not None else None


def validate_lesson_header(text: str) -> None:
    header = main_header(text)
    if header is None:
        fail("Pilotní lekce nemá uzavřený hlavní HTML komentář s metadaty.")
        return

    for field in ("author", "version", "language", "comment"):
        if not re.search(rf"(?m)^\s*{field}:\s*\S", header):
            fail(f"V hlavní hlavičce lekce chybí metadata '{field}:'.")

    if "language:   cs" not in header and "language: cs" not in header:
        fail("Pilotní lekce nemá nastavený jazyk cs.")

    expected_imports = (
        "https://raw.githubusercontent.com/lucny/js-quest/experimental/pilot/GAME-MACROS.md",
        "https://raw.githubusercontent.com/LiaTemplates/p5js/0.0.2/README.md",
    )
    for url in expected_imports:
        if url not in header:
            fail(f"V hlavní hlavičce lekce chybí import {url}.")


def validate_macros(macro_text: str, lesson_text: str) -> None:
    header = main_header(macro_text)
    if header is None:
        fail("GAME-MACROS.md nemá uzavřený hlavní HTML komentář s makry.")
        return

    defined = set(re.findall(r"(?m)^@JSQ\.([a-z]+):", header))
    if re.search(r"(?m)^@JSQ\.styles\s*$", header):
        defined.add("styles")
    missing = REQUIRED_MACROS - defined
    if missing:
        fail(f"GAME-MACROS.md postrádá makra: {', '.join(sorted(missing))}.")

    used = set(re.findall(r"@JSQ\.([A-Za-z][A-Za-z0-9]*)", lesson_text))
    unknown = used - REQUIRED_MACROS - {"flagbox"}
    if unknown:
        fail(f"Pilot používá neznámá makra JSQ: {', '.join(sorted(unknown))}.")

    for name in CARD_MACROS:
        if not re.search(rf"(?m)^@JSQ\.{name}\s*$", lesson_text):
            fail(f"Pilot neobsahuje požadovaný typ aktivity @{name}.")
        if not re.search(rf"(?m)^@JSQ\.{name}\s*$\n>", lesson_text):
            fail(f"Karta @{name} není následovaná samostatným Markdown blockquotem.")

    for path, text in ((MACROS, macro_text), (LESSON, lesson_text)):
        relative = path.relative_to(ROOT)
        legacy_closing_macro = "@JSQ." + "end"
        if legacy_closing_macro in text:
            fail(f"{relative} stále používá zastaralé uzavírací makro.")
        if re.search(r"</?section\b", text, flags=re.IGNORECASE):
            fail(f"{relative} obsahuje HTML section element.")


def validate_progressive_help(text: str) -> None:
    for heading in ("Nápověda:", "Řešení:"):
        if heading in text:
            fail(f"Pilot obsahuje přímo viditelný nadpis '{heading}'.")

    if text.count("<details>") != text.count("</details>"):
        fail("Pilot má nevyvážené prvky <details> pro skrytou pomoc.")

    for attribute in ('data-hint-button="1"', 'data-solution-button="1"'):
        if attribute not in text:
            fail(f"Pilotní kvízy nepoužívají {attribute}.")

    if text.count("[[?]]") < 2:
        fail("Pilot neobsahuje alespoň dvě nativní LiaScript nápovědy [[?]].")

    if re.search(r"(?m)^\s*(?:>\s*)?[-*+]\s+\[[ xX]\]", text):
        fail("Pilot obsahuje checklist/task-list syntaxi, která by vytvořila samostatný formulář.")

    if re.search(r"(?m)^>\s*(?:\[\(|\[\[\?|\*\*\*)", text):
        fail("Nativní kvíz, nápověda nebo řešení nesmí být uvnitř blockquotu herní karty.")


def validate_typography(macro_text: str) -> None:
    required_fonts = ('font-family:', '"Segoe UI"', '"Noto Sans"')
    for token in required_fonts:
        if token not in macro_text:
            fail(f"GAME-MACROS.md postrádá globální typografickou pojistku {token!r}.")

    for selector in ("body nav", "body aside", '[role="navigation"]', '[class*="sidebar"]'):
        if selector not in macro_text:
            fail(f"GAME-MACROS.md nepokrývá navigační selektor {selector!r} font-family pravidlem.")


def validate_world(text: str) -> None:
    title = re.search(r"(?m)^# WORLD\s+(\d+)\s+—", text)
    if title is None:
        fail("Pilot nemá nadpis ve formátu '# WORLD N — …'.")
        return
    directory = LESSON.parent.name
    expected = f"{int(title.group(1)):02d}-"
    if not directory.startswith(expected):
        fail(f"Adresář {directory} neodpovídá WORLD {title.group(1)}.")


def validate_local_links(path: Path, text: str) -> None:
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        target = target.strip().split("#", maxsplit=1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if not (path.parent / target).resolve().is_file():
            fail(f"Neplatný lokální odkaz v {path.relative_to(ROOT)}: {target}")


def validate_no_lesson_macro_definitions(text: str) -> None:
    if re.search(r"(?m)^@JSQ\.[a-z]+:\s", text):
        fail("Pilot definuje makra lokálně; společná makra patří do GAME-MACROS.md.")


ERRORS: list[str] = []


def run() -> int:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"Chybí povinný soubor {relative}.")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        validate_fences(path, read(path))

    lesson_text = read(LESSON)
    macro_text = read(MACROS)
    validate_lesson_header(lesson_text)
    validate_macros(macro_text, lesson_text)
    validate_world(lesson_text)
    validate_no_lesson_macro_definitions(lesson_text)
    validate_progressive_help(lesson_text)
    validate_typography(macro_text)

    for path in markdown_files:
        validate_local_links(path, read(path))

    if ERRORS:
        print(f"\nValidation failed: {len(ERRORS)} error(s).")
        return 1

    print(f"Validation passed: {len(markdown_files)} Markdown file(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(run())
