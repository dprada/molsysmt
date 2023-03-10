form_name = 'string:aminoacids3'
form_type = 'string'
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

from .to_string_aminoacids1 import to_string_aminoacids1
from .to_biopython_SeqRecord import to_biopython_SeqRecord
from .to_biopython_Seq import to_biopython_Seq

_convert_to={
        'string:aminoacids1': to_string_aminoacids1,
        'biopython.SeqRecord': to_biopython_SeqRecord,
        'biopython.Seq': to_biopython_Seq,
        }
