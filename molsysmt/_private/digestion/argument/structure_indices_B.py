import numpy as np
from ...exceptions import ArgumentError
from ...variables import is_all


def digest_structure_indices_B(structure_indices_B, caller=None):
    """ Checks if atom_indices has the expected type and value.

    Parameters
    ----------
    structure_indices : str or int or list or tuple or range.
        The structure indices.

    caller: str, optional
        Name of the function or method that is being digested.
        For debugging purposes.

    Returns
    -------
    str or ndarray or None
        Either None, 'all' or an numpy array of integers with the indices.

    Raises
    -------
    WrongIndicesError
        If the given structure_indices has not of the correct type.
    """

    # Depending on the method this could digest multiple structure_indices

    if structure_indices_B is None:
        return None
    elif is_all(structure_indices_B):
        return 'all'
    elif isinstance(structure_indices_B, (int, np.int64, np.int32)):
        return np.array([structure_indices_B], dtype='int64')
    elif isinstance(structure_indices_B, (np.ndarray, list, tuple, range)):
        return np.array(structure_indices_B, dtype='int64')

    raise ArgumentError('structure_indices_B', value=structure_indices_B, caller=caller, message=None)

