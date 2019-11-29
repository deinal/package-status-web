
from src.filters import get_name, get_dependencies, add_description


def test_get_name():
    line = "Package: python-pkg-resources"
    name = "python-pkg-resources"
    assert get_name(line) == name


def test_get_dependencies():
    line = "Depends: libc6 (>= 2.4), libwrap0 (>= 7.6-4~)"
    alt, deps = get_dependencies(line)
    assert alt == []
    assert deps == ["libc6", "libwrap0"]
    line = "Depends: libc6 (>= 2.14), zlib1g (>= 1:1.1.4), debconf (>= 0.5) | debconf-2.0"
    alt, deps = get_dependencies(line)
    assert alt == [" debconf (>= 0.5) ", " debconf-2.0"]
    assert deps == ["libc6", "zlib1g"]


def test_add_description():
    package = {"Name": "tcpd", "Dependencies": ["libc6", "libwrap0"]}
    lines = ["Package: tcpd",
             "Status: install ok installed",
             "Depends: libc6 (>= 2.4), libwrap0 (>= 7.6-4~)",
             "Description: TCP wrapper utilities\n",
             " Network logger\n",
             "Original-Maintainer: Marco d'Itri <md@linux.it>\n"]
    line = "Description: TCP wrapper utilities\n"
    i = 3
    description = "TCP wrapper utilities<\br> Network logger"
    result, i = add_description(package, lines, line, i)
    package["Description"] = description
    assert package == result
    assert i == 5
