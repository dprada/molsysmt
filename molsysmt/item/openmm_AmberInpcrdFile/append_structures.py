from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='openmm.AmberInpcrdFile')
def append_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedMethodError()


