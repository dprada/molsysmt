from molsysmt._private_tools.exceptions import *

from molsysmt.tools.biopython_SeqRecord.is_biopython_SeqRecord import is_biopython_SeqRecord as is_form
from molsysmt.tools.biopython_SeqRecord.extract import extract
from molsysmt.tools.biopython_SeqRecord.add import add
from molsysmt.tools.biopython_SeqRecord.merge import merge
from molsysmt.tools.biopython_SeqRecord.append_structures import append_structures
from molsysmt.tools.biopython_SeqRecord.concatenate_structures import concatenate_structures
from molsysmt.tools.biopython_SeqRecord.get import *
from molsysmt.tools.biopython_SeqRecord.set import *

form_name='biopython.SeqRecord'
form_type='class'
form_info=["",""]

form_attributes = {

    'atom_index' : False,
    'atom_id' : False,
    'atom_name' : False,
    'atom_type' : False,

    'bond_index' : False,
    'bond_id' : False,
    'bond_name' : False,
    'bond_type' : False,

    'group_index' : True,
    'group_id' : False,
    'group_name' : True,
    'group_type' : False,

    'component_index' : False,
    'component_id' : False,
    'component_name' : False,
    'component_type' : False,

    'molecule_index' : False,
    'molecule_id' : False,
    'molecule_name' : False,
    'molecule_type' : False,

    'chain_index' : False,
    'chain_id' : False,
    'chain_name' : False,
    'chain_type' : False,

    'entity_index' : False,
    'entity_id' : False,
    'entity_name' : False,
    'entity_type' : False,

    'coordinates' : False,
    'velocities' : False,
    'box' : False,
    'time' : False,
    'step' : False,

    'forcefield' : False,
    'temperature' : False,
    'pressure' : False,
    'integrator' : False,
    'damping' : False,

}


