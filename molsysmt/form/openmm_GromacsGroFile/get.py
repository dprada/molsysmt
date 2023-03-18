#######################################################################################
########### THE FOLLOWING LINES NEED TO BE CUSTOMIZED FOR EVERY CLASS  ################
#######################################################################################

from molsysmt._private.execfile import execfile
from molsysmt._private.exceptions import NotImplementedMethodError, NotWithThisFormError
from molsysmt._private.digestion import digest
from molsysmt._private.variables import is_all
from molsysmt import pyunitwizard as puw
import numpy as np

form='openmm.GromacsGroFile'


## From atom

@digest(form=form)
def get_atom_id_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_atom_id_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_atom_name_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_atom_name_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_atom_type_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_atom_type_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_group_index_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_group_index_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_component_index_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_component_index_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_chain_index_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_chain_index_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_molecule_index_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_molecule_index_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_entity_index_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_entity_index_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_inner_bonded_atoms_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_inner_bonded_atoms_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_n_inner_bonds_from_atom(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_inner_bonds_from_atom as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    unit = puw.get_unit(item.positions)
    coordinates = np.array(puw.get_value(item.getPositions(asNumpy=True)))
    coordinates = coordinates.reshape(1, coordinates.shape[0], coordinates.shape[1])

    if not is_all(structure_indices):
        coordinates = coordinates[structure_indices,:,:]

    if not is_all(indices):
        coordinates = coordinates[:,indices,:]

    coordinates = coordinates * unit
    coordinates = puw.standardize(coordinates)

    return coordinates


## From group

@digest(form=form)
def get_group_id_from_group(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_group_id_from_group as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_group_name_from_group(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_group_name_from_group as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_group_type_from_group(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_group_type_from_group as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## From component

@digest(form=form)
def get_component_id_from_component(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_component_id_from_component as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_component_name_from_component(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_component_name_from_component as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_component_type_from_component(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_component_type_from_component as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## From molecule

@digest(form=form)
def get_molecule_id_from_molecule(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_molecule_id_from_molecule as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_molecule_name_from_molecule(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_molecule_name_from_molecule as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_molecule_type_from_molecule(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_molecule_type_from_molecule as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## From chain

@digest(form=form)
def get_chain_id_from_chain(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_chain_id_from_chain as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_chain_name_from_chain(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_chain_name_from_chain as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_chain_type_from_chain(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_chain_type_from_chain as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## From entity

@digest(form=form)
def get_entity_id_from_entity(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_entity_id_from_entity as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_entity_name_from_entity(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_entity_name_from_entity as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_entity_type_from_entity(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_entity_type_from_entity as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## From system

@digest(form=form)
def get_n_atoms_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_atoms_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_groups_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_groups_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_components_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_components_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_chains_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_chains_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_molecules_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_molecules_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_entities_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_entities_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_n_bonds_from_system(item):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_n_bonds_from_system as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_structures_from_system(item, structure_indices='all'):

    if is_all(structure_indices):
        return item.getNumFrames()
    else:
        len(structure_indices)

@digest(form=form)
def get_box_from_system(item, structure_indices='all'):

    box = item.getPeriodicBoxVectors()
    unit = puw.get_unit(box)
    box = np.expand_dims(puw.get_value(box), axis=0)
    box = puw.standardize(box*unit)

    return box

@digest(form=form)
def get_time_from_system(item, structure_indices='all'):

    return None

@digest(form=form)
def get_structure_id_from_system(item, structure_indices='all'):

    return None


## From bond

@digest(form=form)
def get_bond_order_from_bond(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_bond_order_from_bond as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_bond_type_from_bond(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_bond_type_from_bond as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_bonded_atoms_from_bond(item, indices='all'):

    from . import to_openmm_Topology
    from ..openmm_Topology import get_bonded_atoms_from_bond as aux_get

    tmp_item = to_openmm_Topology(item)
    output = aux_get(tmp_item, indices=indices)

    return output


#######################################################################################
######### DO NOT TOUCH THE FOLLOWING LINES, JUST INCLUDE THEM AS THEY ARE #############
#######################################################################################

from os import path
this_folder = path.dirname(path.abspath(__file__))
common_get = path.join(this_folder, '../../_private/common_get.py')
execfile(common_get, globals(), locals())
del(path, this_folder, common_get)

