from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='mmtf.MMTFDecoder')
def copy(item):

    from copy import deepcopy
    tmp_item = deepcopy(item)

    return tmp_item

