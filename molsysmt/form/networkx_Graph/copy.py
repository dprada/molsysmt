from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all

@digest(form='networkx.Graph')
def copy(item):

    tmp_item = item.copy()

    return tmp_item

