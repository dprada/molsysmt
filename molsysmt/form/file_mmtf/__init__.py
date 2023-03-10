form_name = 'file:mmtf'
form_type = 'file'
form_info = ["", ""]

from .is_form import is_form

from .attributes import attributes

from .extract import extract
from .copy import copy
from .add import add
from .append_structures import append_structures
from .get import *
from .set import *
from .iterators import StructuresIterator, TopologyIterator

from .to_mdtraj import load_mmtf, MMTFTrajectoryFile

from .to_file_pdb import to_file_pdb
from .to_MDAnalysis_Universe import to_MDAnalysis_Universe
from .to_mmtf_MMTFDecoder import to_mmtf_MMTFDecoder
from .to_molsysmt_MolSys import to_molsysmt_MolSys
from .to_molsysmt_Structures import to_molsysmt_Structures
from .to_molsysmt_Topology import to_molsysmt_Topology
from .to_openmm_Topology import to_openmm_Topology
from .to_string_aminoacids1 import to_string_aminoacids1
from .to_string_aminoacids3 import to_string_aminoacids3
from .to_string_pdb_text import to_string_pdb_text

_convert_to={
        'file:pdb': to_file_pdb,
        'mmtf.MMTFDecoder': to_mmtf_MMTFDecoder,
        'molsysmt.MolSys': to_molsysmt_MolSys,
        'molsysmt.Structures': to_molsysmt_Structures,
        'molsysmt.Topology': to_molsysmt_Topology,
        'openmm.Topology': to_openmm_Topology,
        'string:aminoacids1': to_string_aminoacids1,
        'string:aminoacids3': to_string_aminoacids3,
        'string:pdb_text': to_string_pdb_text,
        }
