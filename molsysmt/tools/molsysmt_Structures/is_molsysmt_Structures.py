from molsysmt._private_tools.exceptions import WrongFormError

def is_molsysmt_Structures(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'molsysmt.native.structures.Structures')

    return output

def _checking_form(item, check_form=True):

    if check_form:
        if not is_molsysmt_Structures(item):
            raise WrongFormError('molsysmt.Structures')

    pass

