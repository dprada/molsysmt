from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='openmm.CharmmCrdFile', to_form='openmm.CharmmCrdFile')
def add(to_item, item):

    raise NotImplementedMethodError()

