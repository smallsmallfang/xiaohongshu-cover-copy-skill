#!/usr/bin/env python3
"""Count a Xiaohongshu title and body against configurable limits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def read_value(value: str | None, file_path: str | None, label: str) -> str:
    if value is not None and file_path is not None:
        raise ValueError(f"use either --{label} or --{label}-file, not both")
    if file_path is not None:
        text = Path(file_path).read_text(encoding="utf-8")
        return text.rstrip("\r\n")
    if value is not None:
        return value
    raise ValueError(f"one of --{label} or --{label}-file is required")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Count Unicode code points in Xiaohongshu copy. Whitespace and tags count."
    )
    parser.add_argument("--title")
    parser.add_argument("--title-file")
    parser.add_argument("--body")
    parser.add_argument("--body-file")
    parser.add_argument("--title-limit", type=int, default=20)
    parser.add_argument("--body-limit", type=int, default=1000)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.title_limit <= 0 or args.body_limit <= 0:
        parser.error("limits must be positive integers")

    try:
        title = read_value(args.title, args.title_file, "title")
        body = read_value(args.body, args.body_file, "body")
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))

    result = {
        "title_chars": len(title),
        "title_limit": args.title_limit,
        "title_within_limit": len(title) <= args.title_limit,
        "body_chars": len(body),
        "body_limit": args.body_limit,
        "body_within_limit": len(body) <= args.body_limit,
    }
    result["within_limits"] = bool(
        result["title_within_limit"] and result["body_within_limit"]
    )

    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(
            f"title: {result['title_chars']}/{result['title_limit']} "
            f"({'ok' if result['title_within_limit'] else 'over'})"
        )
        print(
            f"body: {result['body_chars']}/{result['body_limit']} "
            f"({'ok' if result['body_within_limit'] else 'over'})"
        )

    return 0 if result["within_limits"] else 1


if __name__ == "__main__":
    sys.exit(main())
