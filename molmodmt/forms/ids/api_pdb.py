from os.path import basename as _basename
from os import remove as _remove
import urllib as _urllib
import json as _json

form_name=_basename(__file__).split('.')[0][4:]+':id'

is_form = {
    'pdb:id': form_name,
    'PDB:id': form_name
    }

def to_pdb(form_id, output_file_path=None, atom_indices=None, frame_indices=None):

    from molmodmt.utils.miscellanea import download_pdb as _download_pdb
    return _download_pdb(form_id.split(':')[-1],output_file_path)

def to_fasta(item, output_file_path=None, atom_indices=None, frame_indices=None):

    tmp_item = item.split(':')[-1]
    url = 'https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList='+tmp_item+'&compressionType=uncompressed'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    fasta_txt = response.read().decode('utf-8')
    if output_file is None:
        return fasta_txt
    else:
        with open(output_file_path,'w') as f:
            f.write(fasta_txt)
        pass

def to_mmtf(item, output_file_path=None, atom_indices=None, frame_indices=None):

    from mmtf import fetch
    from molmodmt import convert

    tmp_item = to_mmtf_MMTFDecoder(item, atom_indices=atom_indices, frame_indices=frame_indices)
    return convert(tmp_item, to_form=output_file_path)

def to_mmtf_MMTFDecoder(item, atom_indices=None, frame_indices=None):

    from mmtf import fetch
    tmp_item = item.split(':')[-1]
    tmp_item = fetch(tmp_item)
    del(fetch)
    return tmp_item

def to_molmodmt_MolMod(item, atom_indices=None, frame_indices=None):

    from molmodmt.utils.miscellanea import download_pdb as download_pdb
    from molmodmt.native.io_molmod import from_pdb as pdb_to_molmodmt
    tmp_file=download_pdb(item.split(':')[-1])
    tmp_item=pdb_to_molmodmt(tmp_file, atom_indices=None, frame_indices=None)
    _remove(tmp_file)
    return tmp_item

def to_mdtraj_Trajectory(item, atom_indices=None, frame_indices=None):

    from molmodmt.utils.miscellanea import download_pdb as _download_pdb
    from molmodmt.forms.files.api_pdb import to_mdtraj as _pdb_to_mdtraj
    _tmp_file=_download_pdb(item.split(':')[-1])
    _tmp_item=_pdb_to_mdtraj(_tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    _remove(_tmp_file)
    return _tmp_item

def to_mdtraj_Topology(form_id, selection='all', frame_indices='all', syntaxis='MDTraj'):

    from molmodmt import convert as _convert
    tmp_item = to_mdtraj_Trajectory(item, selection=selection, syntaxis=syntaxis)
    tmp_item = _convert(tmp_item,'mdtraj.Topology')
    return tmp_item

def to_parmed_Structure(form_id):

    from molmodmt.forms.files.api_pdb import to_parmed_Structure as _pdb_to_parmed_Structure
    _tmp_file=to_pdb(form_id)
    _tmp_form=_pdb_to_parmed_Structure(_tmp_file)
    _remove(_tmp_file)
    del(_pdb_to_parmed_Structure)
    return _tmp_form

def to_pdbfixer_PDBFixer(form_id, atom_indices=None, frame_indices=None):
    from molmodmt.utils.miscellanea import download_pdb
    from molmodmt import convert
    pdbid = form_id.split(':')[-1]
    tmp_file=download_pdb(pdbid)
    tmp_item=convert(tmp_file, 'pdbfixer.PDBFixer', atom_indices=atom_indices,
                     frame_indices=frame_indices)
    _remove(tmp_file)
    return tmp_item

def to_openmm_Modeller(form_id, atom_indices=None, frame_indices=None):
    from molmodmt.utils.miscellanea import download_pdb
    from molmodmt import convert
    pdbid = form_id.split(':')[-1]
    tmp_file=download_pdb(pdbid)
    tmp_item=convert(tmp_file, 'openmm.Modeller', atom_indices=atom_indices,
                     frame_indices=frame_indices)
    _remove(tmp_file)
    return tmp_item

def to_yank_Topography(form_id, atom_indices=None, frame_indices=None):
    from molmodmt.forms.files.api_pdb import to_yank_Topography as _pdb_to_yank_Topography
    _tmp_file=to_pdb(form_id)
    _tmp_form=_pdb_to_yank_Topography(_tmp_file)
    _remove(_tmp_file)
    del(_pdb_to_yank_Topography)
    return _tmp_form

def to_mdanalysis(form_id, atom_indices=None, frame_indices=None):
    from molmodmt.forms.files.api_pdb import to_mdanalysis as _pdb_to_mdanalysis
    _tmp_file=to_pdb(form_id)
    _tmp_form=_pdb_to_mdanalysis(_tmp_file)
    _remove(_tmp_file)
    del(_pdb_to_mdanalysis)
    return _tmp_form

def to_pytraj_Trajectory(form_id, atom_indices=None, frame_indices=None):
    from pytraj import fetch_pdb as _pytraj_fetch_pdb
    _tmp_form=_pytraj_fetch_pdb(form_id)
    del(_pytraj_fetch_pdb)
    return _tmp_form

def to_nglview(form_id, atom_indices=None, frame_indices=None):
    # from nglview import show_pdbid as _nglview_show_pdbid
    # return _nglview_show_pdbid(form_id.split(':')[-1])
    from molmodmt.utils.miscellanea import download_pdb as _download_pdb
    from nglview import show_file as _nglview_show_file
    tmp_pdb_file = _download_pdb(form_id.split(':')[-1])
    tmp_view = _nglview_show_file(tmp_pdb_file)
    _remove(tmp_pdb_file)
    return tmp_view

def select_with_MDTraj(item, selection):
    tmp_form=to_mdtraj(item)
    tmp_sel=tmp_form.topology.select(selection)
    del(tmp_form)
    return tmp_sel

###### Get

## system

def get_n_atoms_from_system(item, indices=None, frame_indices=None):

    tmp_item = to_mmtf_MMTFDecoder(item)
    return tmp_item.num_atoms

def get_n_frames_from_system(item, indices=None, frame_indices=None):

    tmp_item = to_mmtf_MMTFDecoder(item)
    return tmp_item.num_models

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import _get_form
    return _get_form(item)

