import pytest

from printnomad import rules
from printnomad.cli import build_parser

BASE = ["model.3mf", "--printer", "Some Printer"]


@pytest.mark.parametrize(("extra", "expected"), [
    ([], rules.ASSIGNMENT_COMPATIBLE),
    (["--assignment-mode", "exact"], rules.ASSIGNMENT_EXACT),
    (["--assignment-mode", "by_slicer"], rules.ASSIGNMENT_BY_SLICER),
    # Former flag and value, still accepted by existing scripts.
    (["--map-mode", "exact"], rules.ASSIGNMENT_EXACT),
    (["--map-mode", "slicer"], rules.ASSIGNMENT_BY_SLICER),
])
def test_assignment_mode_flag(extra, expected):
    assert build_parser().parse_args(BASE + extra).assignment_mode == expected


def test_former_flag_is_not_in_the_help():
    assert "--map-mode" not in build_parser().format_help()
