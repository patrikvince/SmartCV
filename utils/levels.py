# utils/levels.py

import re


LEVEL_KEYWORDS = {
    "Intern / Gyakornok": [
        "student status", "hallgatói jogviszony", "intern", "gyakornok"
    ],
    "Junior": [
        "junior",
        re.compile(r"\b(0|1|2)(\+)?\s+years?( of relevant)? experience\b")  # 0-2 év
    ],
    "Medior": [
        "medior", "mid-level",
        re.compile(r"\b(3|4|5)(\+)?\s+years?( of relevant)? experience\b")  # 3-5 év
    ],
    "Senior": [
        "senior", "lead developer",
        re.compile(r"\b(6|7|8|9|\d{2,})(\+)?\s+years?( of relevant)? experience\b")  # 6+ év
    ],
    "Lead": [
        "lead", "team lead", "vezető"
    ]
}


def detect_application_level(text: str, level_keywords: dict=LEVEL_KEYWORDS) -> str:
    text_lower = text.lower()
    matched_levels = set()
    level_order = ["Intern / Gyakornok", "Junior", "Medior", "Senior", "Lead"]

    for level, keywords in level_keywords.items():
        for kw in keywords:
            if isinstance(kw, str):
                if kw.lower() in text_lower:
                    matched_levels.add(level)
                    break
            else:  # feltételezzük, hogy regex objektum
                if kw.search(text_lower):
                    matched_levels.add(level)
                    break

    if not matched_levels:
        return "Junior"  # alapértelmezett

    matched_levels_sorted = sorted(matched_levels, key=lambda l: level_order.index(l))
    return matched_levels_sorted[-1]
