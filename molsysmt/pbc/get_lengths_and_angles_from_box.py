from molsysmt._private.digestion import digest
from molsysmt import pyunitwizard as puw
from molsysmt import lib as msmlib

@digest()
def get_lengths_and_angles_from_box(box):
    """
    To be written soon...
    """

    box_value, box_unit  = puw.get_value_and_unit(box)
    lengths_value, angles_value = msmlib.pbc.get_lengths_and_angles_from_box(box_value)
    lengths = puw.quantity(lengths_value.round(6), box_unit)
    lengths = puw.standardize(lengths)
    angles = puw.quantity(angles_value.round(6), 'radians')
    angles = puw.standardize(angles)

    return lengths, angles

