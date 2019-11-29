
import sys
from src.filters import *
from src.final_dependencies import *


def get_lines(filename):
    """
    Returns a list of lines of a file.

    Parameters
    filename : str, name of control file
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def get_content(filename):
    """
    Returns the list of package names in alphabetical order and
    a dictionary with their information.

    Parameters
    filename : str, name of control file
    """

    lines = get_lines(filename)

    # all package names
    names = []
    # main returned dict for package info
    status = {}
    # each package that goes into status
    package = {}
    # dict for dependencies separated by "|"
    unsure = {}

    i = 0
    while i < len(lines):
        line = lines[i]

        if "Package:" in line:
            name = get_name(line)
            names.append(name)
            package["Name"] = name

        if ("Depends:" in line) and ("Pre-Depends:" not in line):
            alt, deps = get_dependencies(line)
            if alt:
                unsure[name] = alt
            package["Dependencies"] = deps

        if "Description:" in line:
            package, i = add_description(package, lines, line, i)
            status[name] = package
            package = {}
        i += 1

    for name in names:
        status = add_alternatives(status, unsure, names, name)

    for name in names:
        status = add_depend_on(status, name)

    return(sorted(names), status)
