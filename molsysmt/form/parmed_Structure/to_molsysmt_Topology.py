from molsysmt._private.digestion import digest

@digest(form='parmed.Structure')
def to_molsysmt_Topology(item, atom_indices='all'):

    from molsysmt.native import Topology
    from numpy import empty, array, arange, reshape, where, unique, nan, sort, zeros
    from molsysmt.element.group import get_group_type_from_group_name
    from molsysmt.element.atom import get_atom_type_from_atom_name
    from ..molsysmt_Topology import extract

    tmp_item = Topology()

    n_atoms = len(item.atoms)

    # atoms, groups and chains

    atom_index_array = empty(n_atoms, dtype=int)
    atom_name_array = empty(n_atoms, dtype=object)
    atom_id_array = empty(n_atoms, dtype=int)
    atom_type_array = empty(n_atoms, dtype=object)
    atom_partial_charge_array = empty(n_atoms, dtype=object)
    atom_formal_charge_array = empty(n_atoms, dtype=object)

    group_index_array = empty(n_atoms, dtype=int)
    group_name_array = empty(n_atoms, dtype=object)
    group_id_array = empty(n_atoms, dtype=int)
    group_type_array = empty(n_atoms, dtype=object)

    chain_index_array = empty(n_atoms, dtype=int)
    chain_name_array = empty(n_atoms, dtype=object)
    chain_id_array = empty(n_atoms, dtype=object)
    chain_type_array = empty(n_atoms, dtype=object)

    atom_index = 0

    aux_dict_chains={}

    for atom in item.atoms:

        atom_index_array[atom_index] = atom.idx
        atom_name_array[atom_index] = atom.name
        atom_id_array[atom_index] = atom.idx
        atom_type_array[atom_index] = get_atom_type_from_atom_name(atom.name)
        atom_partial_charge_array[atom_index] = atom.charge
        atom_formal_charge_array[atom_index] = atom.formal_charge

        group_index_array[atom_index] = atom.residue.idx
        group_name_array[atom_index] = atom.residue.name
        group_id_array[atom_index] = atom.residue.idx
        group_type_array[atom_index] = get_group_type_from_group_name(atom.residue.name)

        chain_id = atom.residue.chain
        if chain_id not in aux_dict_chains:
            aux_dict_chains[chain_id]=len(aux_dict_chains)
        chain_index = aux_dict_chains[chain_id]
        chain_index_array[atom_index] = chain_index
        chain_id_array[atom_index] = chain_id

        chain_index_array[atom_index] = 0
        chain_id_array[atom_index] = None

        atom_index+=1

    if len(aux_dict_chains)==1:
        if '' in aux_dict_chains:
            chain_id_array[:]='A'

    tmp_item.atoms_dataframe["atom_index"] = atom_index_array
    tmp_item.atoms_dataframe["atom_name"] = atom_name_array
    tmp_item.atoms_dataframe["atom_id"] = atom_id_array
    tmp_item.atoms_dataframe["atom_type"] = atom_type_array
    tmp_item.atoms_dataframe["formal_charge"] = atom_formal_charge_array
    tmp_item.atoms_dataframe["partial_charge"] = atom_partial_charge_array
    del(atom_index_array, atom_name_array, atom_id_array, atom_type_array)
    del(atom_formal_charge_array, atom_partial_charge_array)

    tmp_item.atoms_dataframe["group_index"] = group_index_array
    tmp_item.atoms_dataframe["group_name"] = group_name_array
    tmp_item.atoms_dataframe["group_id"] = group_id_array
    tmp_item.atoms_dataframe["group_type"] = group_type_array
    del(group_index_array, group_id_array, group_name_array, group_type_array)

    tmp_item.atoms_dataframe["chain_index"] = chain_index_array
    tmp_item.atoms_dataframe["chain_id"] = chain_id_array
    del(chain_index_array, chain_id_array, chain_name_array, chain_type_array)

    # bonds

    n_bonds = len(item.bonds)

    bond_atom1_array = empty(n_bonds, dtype=int)
    bond_atom2_array = empty(n_bonds, dtype=int)
    bond_type_array = empty(n_bonds, dtype=object)
    bond_order_array = empty(n_bonds, dtype=object)

    bond_index = 0

    for bond in item.bonds:

        bond_atom1_array[bond_index] = bond.atom1._idx
        bond_atom2_array[bond_index] = bond.atom2._idx
        bond_order_array[bond_index] = bond.order
        bond_type_array[bond_index] = bond.type

        bond_index +=1

    tmp_item.bonds_dataframe["atom1_index"] = bond_atom1_array
    tmp_item.bonds_dataframe["atom2_index"] = bond_atom2_array
    tmp_item.bonds_dataframe["order"] = bond_order_array
    tmp_item.bonds_dataframe["type"] = bond_type_array

    # components

    tmp_item._build_components()

    ## molecules

    tmp_item._build_molecules()

    ## entity

    tmp_item._build_entities()

    ## nan to None

    tmp_item._nan_to_None()

    ## extract if atom_indices is not 'all'

    tmp_item = extract(tmp_item, atom_indices=atom_indices, copy_if_all=False)

    return tmp_item

