from os.path import basename as _basename
from simtk.openmm.app import PDBFile as _openmm_PDBFile

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _openmm_PDBFile : form_name,
    'openmm.PDBFile' : form_name
}

def to_nglview(item, selection=None, frame_indices=None, syntaxis="MDTraj"):

    from .api_mdtraj_Trajectory import to_nglview as _mdtraj_to_nglview
    from .api_mdtraj_Trajectory import to_nglview as _mdtraj_to_nglview
    tmp_item = to_mdtraj(item)
    return _mdtraj_to_nglview(tmp_item)

def to_mdtraj(item, selection=None, frame_indices=None, syntaxis='MDTraj'):
    return to_mdtraj_Trajectory(item, selection=selection, syntaxis=syntaxis)

def to_mdtraj_Trajectory(item, selection=None, frame_indices=None, syntaxis='MDTraj'):

    from molmodmt import extract as _extract
    import simtk.unit as _unit
    from mdtraj.core.trajectory import Trajectory as _mdtraj_Trajectory

    tmp_topology = to_mdtraj_Topology(item)
    tmp_item = _mdtraj_Trajectory(item.positions/_unit.nanometers, tmp_topology)
    tmp_item = _extract(tmp_item, selection=selection, syntaxis=syntaxis)

    return tmp_item

def to_mdtraj_Topology(item, selection=None, frame_indices=None, syntaxis='MDTraj'):

    from .api_openmm_Topology import to_mdtraj_Topology as _to_mdtraj_Topology

    tmp_item = to_openmm_Topology(item)
    tmp_item = _to_mdtraj_Topology(tmp_item, selection=selection, syntaxis=syntaxis)
    return tmp_item

def to_openmm_Topology(item, selection=None, frame_indices=None, syntaxis='MDTraj'):

    return item.getTopology()

##### Set

## Atom

def get_coordinates_from_atom(item, indices=None, frame_indices=None):

    tmp_unit = item.positions.unit
    tmp_positions = [item.positions[ii]._value for ii in indices]
    result.append(tmp_positions*tmp_unit)

## System

