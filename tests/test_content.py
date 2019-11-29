
from src.content import get_lines, get_content
from tests.variables import lines, names, status


def test_get_lines():
    assert get_lines("tests/status.sample") == lines


def test_get_content():
    test_names, test_status = get_content("tests/status.sample")
    assert test_names == names
    assert test_status == status
