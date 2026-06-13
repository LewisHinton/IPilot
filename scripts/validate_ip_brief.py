#!/usr/bin/env python3
"""Validate a IPilot IP brief Markdown file.

The validator is intentionally dependency-light. It checks for required
semantic labels rather than enforcing a strict schema. This makes it useful for
Markdown briefs written by humans while still catching missing essentials.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_FIELDS = [
    "IP Name",
    "Brand / Project Name",
    "Target Audience",
    "Primary Use Case",
    "Material Route",
    "Character Type",
    "Fixed Visual Features",
    "Core Traits",
    "Forbidden Visual Changes",
    "Forbidden Tone",
    "Forbidden Topics",
    "Target Platform",
]

ALTERNATIVE_REQUIRED_GROUPS = [
    ("Asset Types Needed", "Asset Discovery Needed"),
]

RECOMMENDED_FIELDS = [
    "Main Color",
    "Secondary Color",
    "Fixed Accessories",
    "Visual Style",
    "Visual Anchors",
    "Line Style",
    "Drawing Style",
    "Color Ratio",
    "Shape Language",
    "Rendering Style",
    "Structural Rules",
    "Reference Image Available",
    "Humor Style",
    "Copyright / Imitation Restrictions",
    "Campaign Topic",
    "Material Type Confirmation Needed",
    "Safety Strictness",
]

DIGITAL_RECOMMENDED_FIELDS = [
    "Platform Adaptation Needed",
    "Platform Placement",
]

PHYSICAL_RECOMMENDED_FIELDS = [
    "Physical Material Needed",
    "Material Type",
    "Audience Orientation",
    "Distribution Context",
    "Usage Scenario",
]

OCCASION_RECOMMENDED_FIELDS = [
    "Occasion Asset Needed",
    "Occasion Type",
    "Occasion Date or Publishing Window",
    "Cultural Context",
    "Desired Tone",
    "Single Asset or Series",
]

DEEP_CONSISTENCY_RECOMMENDED_FIELDS = [
    "Deep Consistency Needed",
    "Identity Anchors",
    "Line Language",
    "Color System",
    "Shape and Construction Rules",
    "Quality Constraints",
    "Text Rendering Rule",
]

REFERENCE_IMAGE_RECOMMENDED_FIELDS = [
    "Reference Images Available",
    "Number of Reference Images",
    "Primary Reference",
    "Supporting References",
    "Reference Fidelity Level",
    "Reference Image Roles",
    "Source of Truth",
    "User-Confirmed Invariants",
    "Allowed Reference-Based Variations",
    "Forbidden Reference Drift",
]

EMPTY_VALUE_RE = re.compile(r"^\s*[-*]\s*([^:]+):\s*(?:\[.*\])?\s*$")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def field_present(text: str, field: str) -> bool:
    return field.lower() in normalize(text)


def empty_labeled_fields(text: str) -> list[str]:
    empty: list[str] = []
    for line in text.splitlines():
        match = EMPTY_VALUE_RE.match(line)
        if match:
            empty.append(match.group(1).strip())
    return empty


def validate(text: str) -> tuple[list[str], list[str], list[str]]:
    missing_required = [field for field in REQUIRED_FIELDS if not field_present(text, field)]

    for alternatives in ALTERNATIVE_REQUIRED_GROUPS:
        if not any(field_present(text, field) for field in alternatives):
            missing_required.append(" or ".join(alternatives))

    missing_recommended = [field for field in RECOMMENDED_FIELDS if not field_present(text, field)]

    normalized = normalize(text)
    is_physical = "physical material needed: yes" in normalized or "material route: physical" in normalized or "offline / physical" in normalized
    is_digital = "material route: digital" in normalized or "digital promotional" in normalized or "platform adaptation needed: yes" in normalized
    is_occasion = (
        "occasion asset needed: yes" in normalized
        or "material route: occasion" in normalized
        or "occasion /" in normalized
        or "ip birthday" in normalized
        or "holiday" in normalized
        or "festival" in normalized
        or "anniversary" in normalized
    )
    is_deep_consistency = "deep consistency needed: yes" in normalized
    is_reference_image = (
        "reference images available: yes" in normalized
        or "reference image available: yes" in normalized
        or "primary reference:" in normalized
        or "source of truth:" in normalized
    )

    if is_digital and not is_physical:
        missing_recommended.extend(field for field in DIGITAL_RECOMMENDED_FIELDS if not field_present(text, field))

    if is_occasion:
        missing_recommended.extend(field for field in OCCASION_RECOMMENDED_FIELDS if not field_present(text, field))

    if is_physical:
        missing_recommended.extend(field for field in PHYSICAL_RECOMMENDED_FIELDS if not field_present(text, field))

    if is_deep_consistency:
        missing_recommended.extend(field for field in DEEP_CONSISTENCY_RECOMMENDED_FIELDS if not field_present(text, field))

    if is_reference_image:
        missing_recommended.extend(field for field in REFERENCE_IMAGE_RECOMMENDED_FIELDS if not field_present(text, field))

    # Preserve order while removing duplicates.
    missing_recommended = list(dict.fromkeys(missing_recommended))

    empty_fields = empty_labeled_fields(text)
    return missing_required, missing_recommended, empty_fields


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a IPilot IP brief Markdown file.")
    parser.add_argument("path", type=Path, help="Path to an IP brief Markdown file")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat missing recommended fields and empty labeled fields as errors.",
    )
    args = parser.parse_args()

    if not args.path.exists():
        raise SystemExit(f"File not found: {args.path}")

    text = args.path.read_text(encoding="utf-8")
    missing_required, missing_recommended, empty_fields = validate(text)

    has_error = False

    if missing_required:
        has_error = True
        print("Missing required fields:")
        for item in missing_required:
            print(f"- {item}")

    if missing_recommended:
        print("Missing recommended fields:")
        for item in missing_recommended:
            print(f"- {item}")

    if empty_fields:
        print("Empty labeled fields:")
        for item in empty_fields:
            print(f"- {item}")

    if args.strict and (missing_recommended or empty_fields):
        has_error = True

    if has_error:
        raise SystemExit(1)

    print("IP brief passes IPilot validation.")


if __name__ == "__main__":
    main()

