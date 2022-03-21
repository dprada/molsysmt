from .is_nglview_NGLWidget import is_nglview_NGLWidget
from molsysmt._private.exceptions import WrongFormError, WrongAtomIndicesError
from molsysmt._private.atom_indices import digest_atom_indices

def to_string_aminoacids3(item, atom_indices='all', check=True):

    if check:

        try:
            is_nglview_NGLWidget(item)
        except:
            raise WrongFormError('nglview.NGLWidget')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

    from . import to_molsysmt_Topology
    from ..molsysmt_Topology import to_string_aminoacids3 as molsysmt_Topology_to_string_aminoacids3

    tmp_item = to_molsysmt_Topology(item, atom_indices=atom_indices, check=False)
    tmp_item = molsysmt_Topolgy_to_string_aminoacids3(tmp_item, check=False)

    return tmp_item

