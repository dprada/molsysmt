from molsysmt._private.digestion import digest

@digest(form='file:gro')
def to_mdtraj_Topology(item, atom_indices='all', structure_indices='all', digest=True):

    from . import to_mdtraj_Trajectory
    from ..mdtraj_Trajectory import to_mdtraj_Topology as mdtraj_Trajectory_to_mdtraj_Topology

    tmp_item = to_mdtraj_Trajectory(item, atom_indices=atom_indices,
            structure_indices=structure_indices, digest=False)
    tmp_item = mdtraj_Trajectory_to_mdtraj_Topology(tmp_item, digest=False)

    return tmp_item

