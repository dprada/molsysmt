from molsysmt._private.digestion import digest

@digest(form='molsysmt.MolSys')
def to_file_psf(item, atom_indices='all', output_filename=None):

    from .to_molsysmt_Topology import to_molsysmt_Topology as molsysmt_MolSys_to_molsysmt_Topology
    from ..molsysmt_Topology import to_file_psf as molsysmt_Topology_to_file_psf

    tmp_item = molsysmt_MolSys_to_molsysmt_Topology(item, atom_indices=atom_indices)
    tmp_item = molsysmt_Topology_to_file_psf(tmp_item, output_filename=output_filename)

    return tmp_item

