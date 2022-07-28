from molsysmt._private.digestion import digest

@digest(form='string:pdb_id')
def to_molsysmt_Structures(item, atom_indices='all', structure_indices='all'):

    if check:

        try:
            is_string_pdb_id(item)
        except:
            raise WrongFormError('string:pdb_id')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

        try:
            structure_indices = digest_structure_indices(structure_indices)
        except:
            raise WrongStructureIndicesError()

    from . import to_mmtf_MMTFDecoder
    from ..mmtf_MMTFDecoder import to_molsysmt_Structures as mmtf_MMTFDecoder_to_molsysmt_Structures

    tmp_item = to_mmtf_MMTFDecoder(item)
    tmp_item = mmtf_MMTFDecoder_to_molsysmt_Structures(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices)

    return tmp_item

