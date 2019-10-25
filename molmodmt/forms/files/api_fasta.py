from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form = {
    'fasta': form_name,
    'FASTA': form_name
    }

def to_biopython_SeqRecord(item, atom_indices=None, frame_indices=None):

    from Bio.SeqIO import read as Bio_SeqRecord_reader
    from molmodmt.forms.classes.api_Bio_SeqRecord import extract_subsystem as extract_Bio_SeqRecord
    tmp_item=Bio_SeqRecord_reader(item,'fasta')
    tmp_item=extract_Bio_SeqRecord(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError


###### Get

## system

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)

