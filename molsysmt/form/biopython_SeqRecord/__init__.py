form_name = 'biopython.SeqRecord'
form_type = 'class'
form_info = ["", ""]

from .is_form import is_form

from .attributes import attributes
from .has_attribute import has_attribute

from .extract import extract
from .add import add
from .merge import merge
from .get import *
from .set import *
from .iterators import TopologyIterator

_convert_to={
        'biopython.SeqRecord': extract,
        }
