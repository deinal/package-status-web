

def get_name(line):
    """
    Returns package name (str) of a Package: line in a control file.

    Parameters
    line : str, current line
    """
    return line[9:].strip("\n")


def get_dependencies(line):
    """
    Returns dependencies (list) of a Depends: line in a control file.
    Those separeted by | are returned as a separate list.

    Parameters
    line : str, current line
    """
    deps = line[9:].split(",")
    alt = []
    ind = []
    for n, d in enumerate(deps):
        # check for alternative dependencies
        if "|" in d:
            alt.extend(d.split("|"))
            ind.append(n)
        else:
            # split at space to remove version numbers
            deps[n] = d.split()[0]
    for n in sorted(ind, reverse=True):
        del deps[n]
    return alt, deps


def add_description(package, lines, line, i):
    """
    Add package description of a Description: line in a control file to
    the package dictionary, also update line index.

    Parameters
    package : dict, package information
    lines : list, control file lines
    line : str, current line
    i : int, line index
    """
    package["Description"] = line[13:].replace("\n", "<br/>")
    while True:
        i += 1
        # Description ends when Homepage or Original-Maintainer begins
        if "Homepage:" not in lines[i] and \
            "Original-Maintainer:" not in lines[i] and \
            lines[i] != "\n":
            package["Description"] += lines[i].replace("\n", "<br/>")
        else:
            break
    return package, i
