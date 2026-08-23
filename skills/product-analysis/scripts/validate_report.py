#!/usr/bin/env python3
"""Validate a generated product-architecture HTML report."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


PLACEHOLDERS = ("TODO", "PLACEHOLDER", "Lorem ipsum", "待填写", "填写 Agent 名称")
EVIDENCE_MARKERS = ("页面事实", "合理推断", "尚未确认", "已确认", "建议设计", "未知")


class ReportParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: dict[str, int] = {}
        self.title_text: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_text.append(data.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--kind", choices=("journey", "contracts", "prompt", "panorama"))
    args = parser.parse_args()

    path = args.report.expanduser().resolve()
    if not path.is_file():
        parser.error(f"not a file: {path}")
    text = path.read_text(encoding="utf-8")
    report = ReportParser()
    report.feed(text)

    errors: list[str] = []
    warnings: list[str] = []
    for tag in ("html", "head", "title", "body"):
        if report.tags.get(tag, 0) != 1:
            errors.append(f"expected exactly one <{tag}>, found {report.tags.get(tag, 0)}")
    if not "".join(report.title_text).strip():
        errors.append("document title is empty")
    if report.tags.get("section", 0) < 3:
        errors.append("expected at least three report sections")
    for token in PLACEHOLDERS:
        if token.casefold() in text.casefold():
            errors.append(f"placeholder remains: {token}")
    if not any(marker in text for marker in EVIDENCE_MARKERS):
        errors.append("no evidence-level marker found")
    if not re.search(r"\bE\d{3,}\b", text):
        warnings.append("no E### evidence identifier found")
    if "<style" not in text:
        warnings.append("no inline style block found")
    if args.kind == "prompt" and not ("<pre" in text and "System Prompt" in text):
        errors.append("prompt report must include a copyable <pre> block and System Prompt label")
    if args.kind == "panorama":
        expected_layers = ("用户与渠道", "交互与工作台", "产品应用", "Agent", "工具与服务", "模型接入", "全局上下文", "知识与公共资产", "基础设施与治理")
        missing = [name for name in expected_layers if name not in text]
        if missing:
            errors.append("panorama is missing layers: " + ", ".join(missing))

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL: {path}")
        return 1
    print(f"OK: {path} ({report.tags.get('section', 0)} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
