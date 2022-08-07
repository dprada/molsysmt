from molsysmt._private.exceptions import ArgumentError
from molsysmt._private.variables import is_all

def digest_selections(selections, syntax="MolSysMT", caller=None):
    """ Checks if a list of selections have the correct types and syntax

       Parameters
       ----------
       item : list or tuple
           List of tuple of selections to be checked.
       syntax : str, default="MolSysMT"
           Name of the syntax used in the selections.
       caller: str, optional
           Name of the function or method that is being digested.

       Raises
       ------
       WrongSelectionError or WrongSelectionSyntaxisError or WrongSyntaxisError or WrongMultipleSelectionsError
           A WrongMultipleSelectionsError is raised if a single, or none, selection is given.
           A WrongSelectionError is raised if the a selection given is not in deed a selection.
           A WrongSelectionSyntaxisError is raised if a selection given is not using the expected
           syntax.
           A WrongSyntaxisError is raised if the syntax given is not in deed a syntax.

    """
    from .selection import digest_selection
    if isinstance(selections, (list, tuple)):
        return [digest_selection(ii, syntax) for ii in selections]
    elif is_all(selections):
        return selections

    raise ArgumentError('selections', value=selections, caller=caller, message=None)

