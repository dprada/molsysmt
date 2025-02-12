"""
Unit and regression test for the convert module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
from molsysmt.systems import tests as tests_systems
import numpy as np
import os

# Whole systems (selection='all' and structure_indices='all')

def test_mdtraj_Trajectory_to_string_aminoacids1():
    molsys = tests_systems['chicken villin HP35']['1vii.pdb']
    molsys = msm.convert(molsys, to_form='mdtraj.Trajectory')
    molsys = msm.convert(molsys, to_form='string:aminoacids1')
    form = msm.get_form(molsys)
    assert 'string:aminoacids1'==form

# Selection

## Multiple outputs


