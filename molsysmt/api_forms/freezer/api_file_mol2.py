from molsysmt._private.exceptions import *
from molsysmt.api_forms.common_gets import *
import numpy as np
from molsysmt.native.molecular_system import molecular_system_components
from molsysmt._private.files_and_directories import temp_filename
import sys
import importlib

form_name='file:mol2'
from_type='file'

is_form = {
        'file:mol2': form_name
    }

info=["",""]

has = molecular_system_components.copy()
for ii in ['elements', 'bonds', 'coordinates', 'ff_parameters']:
    has[ii]=True

def to_parmed_Structure(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from parmed import load_file as _parmed_file_loader

    tmp_item = _parmed_file_loader(item)
    tmp_item = tmp_item.to_structure()
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def to_mdtraj_Trajectory(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from mdtraj import load_mol2 as _mdtraj_load_mol2

    tmp_item = _mdtraj_load_mol2(item)
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def to_mdtraj_Topology(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from mdtraj import load_mol2 as _mdtraj_load_mol2

    tmp_item = _mdtraj_load_mol2(item).topology
    del(_mdtraj_load_mol2)
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def to_openmm_Topology(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.api_forms.api_mdtraj_Topology import to_openmm_Topology as mdtraj_Topology_to_openmm_Topology

    tmp_item, tmp_molecular_system = to_mdtraj_Topology(item, molecular_system=molecular_system, atom_indices=atom_indices, structure_indices=atom_indices)
    tmp_item, tmp_molecular_system = mdtraj_Topology_to_openmm_Topology(tmp_item, molecular_system=tmp_molecular_system)

    return tmp_item, tmp_molecular_system

def to_openmm_Modeller(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from molsysmt.api_forms.api_mdtraj_Trajectory import to_openmm_Modeller as mdtraj_Trajectory_to_openmm_Modeller

    tmp_item, tmp_molecular_system = to_mdtraj_Trajectory(item, molecular_system=molecular_system, atom_indices=atom_indices, structure_indices=atom_indices)
    tmp_item, tmp_molecular_system = mdtraj_Trajectory_to_openmm_Modeller(tmp_item, molecular_system=tmp_molecular_system)

    return tmp_item, tmp_molecular_system

    #from molsysmt.api_forms.engines.api_parmed import to_modeller as _parmed_to_modeller
    #tmp_form = to_parmed(item)
    #tmp_form = _parmed_to_modeller(tmp_form)
    #del(_parmed_to_modeller)
    #return tmp_form

def to_file_pdb(item, molecular_system=None, atom_indices='all', structure_indices='all', output_filename=None):

    from parmed import load_file as _parmed_file_loader

    tmp_item = _parmed_file_loader(item)
    tmp_item.save(output_filename)
    tmp_item = output_filename
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None
    return tmp_item, tmp_molecular_system

def to_nglview_NGLWidget(item, molecular_system=None, atom_indices='all', structure_indices='all'):

    from nglview import show_file as nglview_show_file

    tmp_item = nglview_show_file(item)
    if molecular_system is not None:
        tmp_molecular_system = molecular_system.combine_with_items(tmp_item)
    else:
        tmp_molecular_system = None

    return tmp_item, tmp_molecular_system

def to_file_mol2(item, molecular_system=None, atom_indices='all', structure_indices='all', output_filename=None, copy_if_all=True):

    tmp_molecular_system = None

    if (atom_indices is 'all') and (structure_indices is 'all'):
        if copy_if_all:
            tmp_item = extract(item)
            if molecular_system is not None:
                tmp_molecular_system = molecular_system.combine_with_items(tmp_item, output_filename=output_filename)
        else:
            tmp_item = item
            if molecular_system is not None:
                tmp_molecular_system = molecular_system
    else:
        tmp_item = extract(item, atom_indices=atom_indices, structure_indices=structure_indices, output_filename=output_filename)
        if molecular_system is not None:
            tmp_molecular_system = molecular_system.combine_with_items(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item, tmp_molecular_system

def extract(item, atom_indices='all', structure_indices='all', output_filename=None):

    if output_filename is None:
        output_filename = temp_filename(extension='mol2')

    if (atom_indices is 'all') and (structure_indices is 'all'):
        raise NotImplementedError()
    else:
        raise NotImplementedError()

    return tmp_item

def merge(item_1, item_2):

    raise NotImplementedError

def add(to_item, item):

    raise NotImplementedError

def append_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

def concatenate_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

###### Get

def aux_get(item, indices='all', structure_indices='all'):

    from molsysmt.api_forms import forms

    method_name = sys._getframe(1).f_code.co_name

    if 'mdtraj.Trajectory' in forms:

        tmp_item, _ = to_mdtraj_Trajectory(item)
        module = importlib.import_module('molsysmt.api_forms.api_mdtraj_Trajectory')
        _get = getattr(module, method_name)
        output = _get(tmp_item, indices=indices, structure_indices=structure_indices)

    else:

        raise NotImplementedError

    return output

## atom

def get_atom_id_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_name_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_type_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_group_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_component_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_chain_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_molecule_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_entity_index_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_inner_bonded_atoms_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_inner_bonds_from_atom (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## group

def get_group_id_from_group(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_group_name_from_group(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_group_type_from_group(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## component

def get_component_id_from_component (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_component_name_from_component (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_component_type_from_component (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## molecule

def get_molecule_id_from_molecule (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_molecule_name_from_molecule (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_molecule_type_from_molecule (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## chain

def get_chain_id_from_chain (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_chain_name_from_chain (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_chain_type_from_chain (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## entity

def get_entity_id_from_entity (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_entity_name_from_entity (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_entity_type_from_entity (item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## system

def get_n_atoms_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_groups_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_components_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_chains_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_molecules_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_entities_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_bonds_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_coordinates_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_shape_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_lengths_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_angles_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_box_volume_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_time_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_step_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_n_structures_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_bonded_atoms_from_system(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

## bond

def get_bond_order_from_bond(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_bond_type_from_bond(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

def get_atom_index_from_bond(item, indices='all', structure_indices='all'):

    return aux_get(item, indices=indices, structure_indices=structure_indices)

###### Set

def set_box_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', structure_indices='all', value=None):

    raise NotImplementedError


