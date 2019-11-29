

def add_alternatives(status, unsure, names, name):
    """
    Add alternative dependencies to either the list of dependencies
    for the current package, or to a list of unused dependencies.

    Parameters
    status : dict, main package contents
    unsure : dict, alternative dependencies
    names : list, package names
    name : str, name of current package
    """
    # dependencies without links
    leftovers = []
    # try block since some packages lack alternative dependencies
    try:
        for d in unsure[name]:
            d = d.split()[0]
            if d in names:
                status[name]["Dependencies"].append(d)
            else:
                leftovers.append(d)
        status[name]["Alternatives"] = leftovers
    except:
        pass
    return status


def add_depend_on(status, name):
    """
    Add the names of the packages that depend on the current package.

    Parameters
    status : dict, main package contents
    name : str, current package name
    """
    # list for those that dependends on this package
    depon = []
    for key in status:
        # try block since some packages lack dependencies altogether
        try:
            if name in status[key]["Dependencies"]:
                depon.append(key)
        except:
            continue
    if depon:
        status[name]["Need me"] = depon
    return status
