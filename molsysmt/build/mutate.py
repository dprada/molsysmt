from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest()
def mutate(molecular_system, mutations=None, keys='group_index', selection="all", syntax='MolSysMT', engine='PDBFixer'):


    if engine=="PDBFixer":

        from molsysmt.basic import get, convert, get_form, contains

        if isinstance(mutations, (tuple, list)):

            for mutation_string in mutations:
                old_group_name, group_id, new_group_name = nutation_string.split('-')

        elif isinstance(mutations, dict):
            if keys=='group_index':
                group_indices = list(mutations.keys())
                to_group_names = list(mutations.values())
            elif keys=='group_id':
                group_ids = list(mutations.keys())
                to_group_names = list(mutations.values())
                group_indices = []
                for ii in group_ids:
                    aux_indices = get(molecular_system, element='group', selection='group_id==@ii', mask='', group_index=True)
                    if aux_indices.shape[0]>1:
                        raise ValueError(f'There are multiple groups with the group_id: {ii}')
                    else:
                        group_indices.append(aux_indices[0])
            elif keys=='group_name':
                group_indices = []
                to_group_names = []
                for from_name, to_name in mutations.items():
                    aux_indices = get(molecular_system, element='group', selection='group_name==@from_name', group_index=True)
                    for aux_index in aux_indices:
                        group_indices.append(aux_index)
                        to_group_names.append(to_name)

        to_group_names = [name.upper() for name in to_group_names]

        form_in = get_form(molecular_system)
        tmp_molecular_system = convert(molecular_system, to_form="pdbfixer.PDBFixer")

        from_group_names, group_ids, in_chain_ids = get(tmp_molecular_system, element='group',
                                                            indices=group_indices, group_name=True, group_id=True,
                                                            chain_id=True)

        for group_id, from_group_name, to_group_name, in_chain_id in zip(group_ids, from_group_names, to_group_names, in_chain_ids):
            mutation_string = "-".join([from_group_name,str(group_id),to_group_name])
            if verbose: print(mutation_string)
            tmp_molecular_system.applyMutations([mutation_string], in_chain_id)

        tmp_molecular_system.findMissingResidues()
        tmp_molecular_system.findMissingAtoms()
        tmp_molecular_system.addMissingAtoms()

        if contains(tmp_molecular_system, hydrogens=True):
            tmp_molecular_system.addMissingHydrogens(7.4)

        tmp_molecular_system = convert(tmp_molecular_system, to_form=form_in)

        return tmp_molecular_system

    else:
        raise NotImplementedMethodError


