from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='pytraj.Trajectory')
def copy(item):

    from copy import deepcopy
    tmp_item = deepcopy(item)

    return tmp_item

