from molsysmt._private.digestion import digest

@digest(form='pdbfixer.PDBFixer')
def copy(item):

    from copy import deepcopy
    tmp_item = deepcopy(item)

    return tmp_item
