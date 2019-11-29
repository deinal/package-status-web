
from src.final_dependencies import add_alternatives, add_depend_on
from tests.variables import names, status, unsure, lines, before_alt, before_need


def test_add_alternatives():
    name = "libssl1.0.0"
    test_status = add_alternatives(before_alt, unsure, names, name)
    for key in ["Name", "Dependencies", "Alternatives", "Description"]:
        assert test_status[name][key] == status[name][key]


def test_add_depend_on():
    name = "libquadmath0"
    test_status = add_depend_on(before_need, name)
    for key in status[name]:
        assert test_status[name][key] == status[name][key]
