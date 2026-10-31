"""pytest-html ANSI color output examples.

Run this module with:
    uv run pytest src/try_playwright/test_pytest_html.py --html=report.html --self-contained-html
"""

import pytest


@pytest.mark.parametrize(
    ("label", "ansi_color"),
    [
        ("passed check", "\x1b[32m"),
        ("warning message", "\x1b[33m"),
        ("error detail", "\x1b[31m"),
    ],
)
def test_html_report_converts_ansi_output(label: str, ansi_color: str) -> None:
    """The report preserves ANSI color codes in captured test output."""
    print(f"{ansi_color}{label}\x1b[0m")
    assert label


@pytest.mark.xfail(reason="Demonstrates ANSI output for an expected failure.", strict=True)
def test_html_report_shows_ansi_output_for_expected_failure() -> None:
    """Expected failures retain captured ANSI output in the HTML report."""
    print("\x1b[31mExpected failure: simulated service error\x1b[0m")
    assert False, "Intentional expected failure for the report example"


def test_html_report_supports_multiple_ansi_styles() -> None:
    """ANSI styles can be combined in one captured output block."""
    print("\x1b[1;34mINFO\x1b[0m preparing test data")
    print("\x1b[1;32mSUCCESS\x1b[0m test data is ready")
    assert True