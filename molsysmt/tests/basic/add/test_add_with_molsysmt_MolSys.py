"""
Unit and regression test for the add module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
from molsysmt.systems import tests as tests_systems
import numpy as np

def test_add_with_molsysmt_MolSys():
    molsys_1 = msm.convert(tests_systems['proline dipeptide']['proline_dipeptide.msmpk'], to_form='molsysmt.MolSys')
    molsys_2 = msm.convert(tests_systems['valine dipeptide']['valine_dipeptide.msmpk'], to_form='molsysmt.MolSys')
    molsys_3 = msm.convert(tests_systems['lysine dipeptide']['lysine_dipeptide.msmpk'], to_form='molsysmt.MolSys')
    n_atoms_1 = msm.get(molsys_1, element='system', n_atoms=True)
    n_atoms_2 = msm.get(molsys_2, element='system', n_atoms=True)
    n_atoms_3 = msm.get(molsys_3, element='system', n_atoms=True)
    msm.add(molsys_1, molsys_2)
    msm.add(molsys_1, molsys_3)
    n_atoms, n_structures = msm.get(molsys_1, element='system', n_atoms=True, n_structures=True)
    assert 'molsysmt.MolSys'==msm.get_form(molsys_1)
    assert n_atoms == n_atoms_1+n_atoms_2+n_atoms_3
    assert n_structures == 1

