from molsysmt._private.digestion import digest
import numpy as np

@digest()
def get_atoms_with_alternate_locations(molecular_system):

    from molsysmt.basic import get, select

    output_atoms = []

    alternate_location = get(molecular_system, element='atom', alternate_location=True)

    for A_index in np.where(alternate_location=='A')[0]:

        atom_name, group_id, chain_id = get(molecular_system, element='atom',
                selection=A_index, atom_name=True, group_id=True, chain_id=True)

        equal_atoms = select(molecular_system, element='atom', selection='atom_name==@atom_name and group_id==@group_id and chain_id==@chain_id')

        output_atoms.append(equal_atoms)

    return output_atoms

