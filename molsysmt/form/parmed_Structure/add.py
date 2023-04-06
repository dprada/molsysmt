from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='parmed.Structure', to_form='parmed.Structure')
def add(to_item, item, atom_indices='all'):

    raise NotImplementedMethodError()

