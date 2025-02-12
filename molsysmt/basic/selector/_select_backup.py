from molsysmt._private.exceptions import NotImplementedMethodError, NotSupportedSyntaxError
from molsysmt._private.digestion import digest
import numpy as np
from molsysmt._private.variables import is_all, is_iterable_of_iterables
from molsysmt._private.strings import get_parenthesis
from re import findall
from inspect import stack, getargvalues


def select_standard(molecular_system, selection='all', syntax='MolSysMT'):

    from . import where_is_attribute
    from molsysmt.form import _dict_modules

    if type(selection)==str:
        if is_all(selection):
            aux_item, aux_form = where_is_attribute(molecular_system, 'n_atoms')
            n_atoms = _dict_modules[aux_form].get_n_atoms_from_system(aux_item)
            atom_indices = np.arange(n_atoms, dtype='int64')
        else:
            #aux_item, aux_form = where_is_attribute(molecular_system, 'atom_index')
            if syntax=='MolSysMT':
                atom_indices = select_with_MolSysMT(molecular_system, selection)
            elif syntax=='MDTraj':
                atom_indices = select_with_MDTraj(molecular_system, selection)
            elif syntax=='Amber':
                atom_indices = select_with_Amber(molecular_system, selection)
            elif syntax=='ParmEd':
                atom_indices = select_with_ParmEd(molecular_system, selection)
            elif syntax=='MDAnalysis':
                atom_indices = select_with_MDAnalysis(molecular_system, selection)
            else:
                raise NotSupportedSyntaxError()

    elif type(selection) in [int, np.int64, np.int32]:
        atom_indices = np.array([selection], dtype='int64')
    elif type(selection)==set:
        atom_indices = np.array(list(selection), dtype='int64')
    elif hasattr(selection, '__iter__'):
        atom_indices = np.array(selection, dtype='int64')
    else :
        atom_indices = None

    return atom_indices


def select_within(molecular_system, selection, structure_indices, syntax):

    from molsysmt.structure.get_contacts import get_contacts

    not_within = False

    if "not within " in selection:
        selection_1, tmp_selection = selection.split(" not within ")
        not_within = True
    else:
        selection_1, tmp_selection = selection.split(" within ")

    pbc = False

    if "with pbc " in tmp_selection:
        pbc = True
        tmp_selection = tmp_selection.replace("with pbc ","")
    elif "without pbc " in tmp_selection:
        tmp_selection = tmp_selection.replace("without pbc ","")

    threshold, selection_2 = tmp_selection.split(" of ")

    atom_indices_1 = select(molecular_system, selection=selection_1, syntax=syntax)
    atom_indices_2 = select(molecular_system, selection=selection_2, syntax=syntax)
    cmap = get_contacts(molecular_system, selection=atom_indices_1, selection_2=atom_indices_2,
            structure_indices=structure_indices, threshold=threshold, pbc=pbc, engine='MolSysMT')

    if not_within:
        output = atom_indices_1[np.where(cmap.all(axis=2)[0]==False)[0]]
    else:
        output = atom_indices_1[np.where(cmap.any(axis=2)[0]==True)[0]]

    return output


def select_bonded_to(molecular_system, selection, syntax):

    from molsysmt.basic import get

    not_bonded=False

    if "not bonded to" in selection:
        selection_1, selection_2 = selection.split(" not bonded to")
        not_bonded=True
    else:
        selection_1, selection_2 = selection.split(" bonded to")

    atom_indices_1 = select(molecular_system, selection=selection_1, syntax=syntax)
    atom_indices_2 = get(molecular_system, element='atom', selection=selection_2, syntax=syntax, bonded_atoms=True)
    atom_indices_2 = np.unique(np.concatenate(atom_indices_2).ravel())

    if not_bonded:
        output = np.setdiff1d(atom_indices_1, atom_indices_2, assume_unique=True)
    else:
        output = np.intersect1d(atom_indices_1, atom_indices_2, assume_unique=True)

    return output


def select_in_groups_of(molecular_system, selection, syntax):

    from molsysmt.basic import get

    before, after=selection.split('in groups of')
    before = before.strip()
    after = after.strip()

    if before=='' or is_all(before):

        output = get(molecular_system, element='group', selection=after, atom_index=True)

    else:

        pre_output = get(molecular_system, element='group', selection=after, atom_index=True)
        mask = select(molecular_system, element='atom', selection=before)
        output = [np.intersect1d(ii, mask).astype('object') for ii in pre_output]
        output = [ii for ii in output if ii.shape[0]>0]
        output = np.array(output, dtype='object')

    return output


def select_in_components_of(molecular_system, selection, syntax):

    from molsysmt.basic import get

    before, after=selection.split('in components of')
    before = before.strip()
    after = after.strip()

    if before=='' or is_all(before):

        output = get(molecular_system, element='component', selection=after, atom_index=True)

    else:

        pre_output = get(molecular_system, element='component', selection=after, atom_index=True)
        mask = select(molecular_system, element='atom', selection=before)
        output = [np.intersect1d(ii, mask).astype('object') for ii in pre_output]
        output = [ii for ii in output if ii.shape[0]>0]
        output = np.array(output, dtype='object')

    return output

def select_in_molecules_of(molecular_system, selection, syntax):

    from molsysmt.basic import get

    before, after=selection.split('in molecules of')
    before = before.strip()
    after = after.strip()

    if before=='' or is_all(before):

        output = get(molecular_system, element='molecule', selection=after, atom_index=True)

    else:

        pre_output = get(molecular_system, element='molecule', selection=after, atom_index=True)
        mask = select(molecular_system, element='atom', selection=before)
        output = [np.intersect1d(ii, mask).astype('object') for ii in pre_output]
        output = [ii for ii in output if ii.shape[0]>0]
        output = np.array(output, dtype='object')

    return output

def select_in_chains_of(molecular_system, selection, syntax):

    from molsysmt.basic import get

    before, after=selection.split('in chains of')
    before = before.strip()
    after = after.strip()

    if before=='' or is_all(before):

        output = get(molecular_system, element='chain', selection=after, atom_index=True)

    else:

        pre_output = get(molecular_system, element='chain', selection=after, atom_index=True)
        mask = select(molecular_system, element='atom', selection=before)
        output = [np.intersect1d(ii, mask).astype('object') for ii in pre_output]
        output = [ii for ii in output if ii.shape[0]>0]
        output = np.array(output, dtype='object')

    return output

def select_in_entities_of(molecular_system, selection, syntax):

    from molsysmt.basic import get

    before, after=selection.split('in entities of')
    before = before.strip()
    after = after.strip()

    if before=='' or is_all(before):

        output = get(molecular_system, element='entity', selection=after, atom_index=True)

    else:

        pre_output = get(molecular_system, element='entity', selection=after, atom_index=True)
        mask = select(molecular_system, element='atom', selection=before)
        output = [np.intersect1d(ii, mask).astype('object') for ii in pre_output]
        output = [ii for ii in output if ii.shape[0]>0]
        output = np.array(output, dtype='object')

    return output

@digest()
def select(molecular_system, selection='all', structure_indices='all', element='atom',
        mask=None, syntax='MolSysMT', to_syntax=None):
    """
    Selecting elements in a molecular system

    The indices of the elements that matches a query string can be obtained with this function.


    Parameters
    ----------

    molecular_system : molecular system
        Molecular system in any of :ref:`the supported forms
        <Introduction_Forms>` to be analysed by the function.

    selection : tuple, list, numpy.ndarray or str, default 'all'
        Selection of elements of the molecular system to be extracted by the function. The selection can be
        given by a list, tuple or numpy array of element indices (0-based
        integers); or by means of a query string following any of :ref:`the selection
        syntaxes parsable by MolSysMT <Introduction_Selection>`.

    structure_indices : tuple, list, numpy.ndarray or 'all', default 'all'
        Indices of structures (0-based integers) to be analysed by the selection function if
        spatial constraints are included.

    element: {'atom', 'group', 'component', 'molecule', 'chain', 'entity', 'system'}, default 'system'
        The indices returned by this function corresponds to the elements specified by this input
        argument -matching the selecton criteria-.

    mask: tuple, list, numpy.ndarray or str, default=None
        Mask to be applied in the selection. If this argument is different
        from None, the selection is done only over the elements specified by this
        argument.

    syntax : str, default 'MolSysMT'
        :ref:`Supported syntax <Introduction_Selection>` used in the `selection` argument (in case
        it is a string).

    to_syntax : str, default None
        The function will return a query string with the syntax specified by this input argument if
        its value is different from None.


    Returns
    -------

    numpy.ndarray of int
        List of element indices in agreement with the selection criterion applied over the input molecular
        system. The nature of the elements is chosen with the input argument ``element``.


    Raises
    ------

    NotSupportedFormError
        The function raises a NotSupportedFormError in case a molecular system
        is introduced with a not supported form.

    ArgumentError
        The function raises an ArgumentError in case an input argument value
        does not meet the required conditions.

    SyntaxError
        The function raises a SyntaxError in case the syntax argument takes a not supported value.


    .. versionadded:: 0.1.0


    Notes
    -----

    The list of supported molecular systems' forms is detailed in the documentation section
    :ref:`User Guide > Introduction > Molecular systems > Forms <Introduction_Forms>`.

    The list of supported selection syntaxes can be checked in the documentation section
    :ref:`User Guide > Introduction > Selection syntaxes <Introduction_Selection>`.


    See Also
    --------

    :ref:'User Guide > Introduction > Configuration options'

    :ref:'User Guide > Introduction > Selection syntaxes'


    Examples
    --------

    The following example illustrates the use of the function.

    >>> import molsysmt as msm
    >>> molecular_system = msm.systems.demo['T4 lysozyme L99A']['181l.mmtf']
    >>> msm.basic.select(molecular_system, element='group', selection='group_name in ["HIS","THR"]')
    array([ 20,  25,  30,  33,  53,  58, 108, 114, 141, 150, 151, 154, 156])

    .. admonition:: User guide

       Follow this link for a tutorial on how to work with this function:
       :ref:`User Guide > Tools > Basic > Select <Tutorial_Select>`.


    """

    from . import get_form, where_is_attribute, is_a_molecular_system
    from molsysmt.form import _dict_modules

    if is_all(mask):
        mask=None

    if type(selection)==str:

        while selection_with_special_subsentences(selection):
            sub_selection = selection_with_special_subsentences(selection)
            sub_atom_indices = select(molecular_system, sub_selection, syntax=syntax)
            selection = selection.replace(sub_selection, 'atom_index==@sub_atom_indices')

        if 'in groups of' in selection:
            atom_indices = select_in_groups_of(molecular_system, selection=selection, syntax=syntax)

        elif 'in components of' in selection:
            atom_indices = select_in_components_of(molecular_system, selection=selection, syntax=syntax)

        elif 'in molecules of' in selection:
            atom_indices = select_in_molecules_of(molecular_system, selection=selection, syntax=syntax)

        elif 'in chains of' in selection:
            atom_indices = select_in_chains_of(molecular_system, selection=selection, syntax=syntax)

        elif 'in entities of' in selection:
            atom_indices = select_in_entities_of(molecular_system, selection=selection, syntax=syntax)

        elif 'within' in selection:
            atom_indices = select_within(molecular_system, selection=selection,
                                         structure_indices=structure_indices, syntax=syntax)
        elif 'bonded to' in selection:
            atom_indices = select_bonded_to(molecular_system, selection=selection, syntax=syntax)

        else:
            atom_indices = select_standard(molecular_system, selection=selection, syntax=syntax)

        if element=='atom':
            output_indices = atom_indices

        elif element in ['group', 'component', 'chain', 'molecule', 'entity']:

            if is_iterable_of_iterables(atom_indices):

                output_indices = []
                aux_item, aux_form = where_is_attribute(molecular_system, element+'_index')
                for aux_atom_indices in atom_indices:
                    temp_output_indices = getattr(_dict_modules[aux_form], f'get_{element}_index_from_atom')(aux_item, indices=aux_atom_indices)
                    output_indices.append(np.unique(temp_output_indices).astype('object'))
                output_indices = np.array(output_indices, dtype='object')

            else:

                aux_item, aux_form = where_is_attribute(molecular_system, element+'_index')
                output_indices = getattr(_dict_modules[aux_form], f'get_{element}_index_from_atom')(aux_item, indices=atom_indices)
                output_indices = np.unique(output_indices)


        elif element=='bond':
            aux_item, aux_form = where_is_attribute(molecular_system, 'inner_bond_index')
            output_indices = _dict_modules[aux_form].get_inner_bond_index_from_atom(aux_item, indices=atom_indices)

        else:
            raise NotImplementedMethodError()

    else:

        output_indices = selection
        #atom_indices = select_standard(molecular_system, selection, syntax)

    if mask is not None:
        if isinstance(mask, str):
            mask = select(molecular_system, selection=mask, element=element, syntax=syntax)
        output_indices = np.intersect1d(output_indices, mask, assume_unique=True)

    if to_syntax is None:
        return output_indices
    else:
        return indices_to_selection(molecular_system, output_indices, element=element, syntax=to_syntax)

def selection_with_special_subsentences(selection):

    output = None
    parenthesis = get_parenthesis(selection)
    for subselection in parenthesis:
        if ('within ' in subselection) or ('bonded to ' in subselection):
            output = subselection
            break

    return output



def select_with_MDTraj(item, selection):

    from . import convert, get_form

    form_in = get_form(item)

    if form_in == 'mdtraj.Topology':
        tmp_item = item
    else:
        tmp_item = convert(item, to_form='mdtraj.Topology')

    atom_indices = tmp_item.select(selection)

    return atom_indices

def select_with_MDAnalysis(item, selection):

    from . import convert, get_form

    form_in = get_form(item)

    if form_in == 'MDAnalysis.Topology':
        tmp_item = item
    else:
        tmp_item = convert(item, to_form='MDAnalysis.Topology')

    tmp_atomgroup = tmp_item.select_atoms(selection)
    atom_indices = tmp_atomgroup.atoms.ids
    del(tmp_atomgroup)

    return atom_indices


def select_with_MolSysMT(item, selection):

    from . import convert, get_form
    from molsysmt.config import selection_shortcuts

    form_in = get_form(item)

    if form_in == 'molsysmt.Topology':
        tmp_item = item
    else:
        tmp_item = convert(item, to_form='molsysmt.Topology')

    tmp_selection = selection


    if '@' in selection:

        var_names = [ii[1:] for ii in findall(r"@[\w']+", selection)]

        all_stack_frames = stack()

        counter = -1
        n_frames = len(all_stack_frames)

        no_wrapper_stack_frames = [ii for ii in all_stack_frames if ii[3]!='wrapper']

        for aux_stack in no_wrapper_stack_frames:
            args, args_paramname, kwargs_paramname, values = getargvalues(aux_stack.frame)
            if 'selection' in args:
                counter+=1
            else:
                break

        #print(counter)
        #for ii in range(len(no_wrapper_stack_frames)):
        #    aaa = no_wrapper_stack_frames[ii]
        #    print(ii, aaa[3])
        #    if 'selection' in getargvalues(aaa.frame)[3]:
        #        print('#####', getargvalues(aaa.frame)[3]['selection'])
        #    print('>>>', var_names[0] in aaa[0].f_locals)
        #    print('>>>', var_names[0] in aaa[0].f_globals)

        for var_name in var_names:
            if var_name in no_wrapper_stack_frames[counter][0].f_locals:
                var_value = no_wrapper_stack_frames[counter][0].f_locals[var_name]
            elif var_name in no_wrapper_stack_frames[counter][0].f_globals:
                var_value = no_wrapper_stack_frames[counter][0].f_globals[var_name]
            elif var_name in no_wrapper_stack_frames[counter+1][0].f_locals:
                var_value = no_wrapper_stack_frames[counter+1][0].f_locals[var_name]
            elif var_name in no_wrapper_stack_frames[counter+1][0].f_globals:
                var_value = no_wrapper_stack_frames[counter+1][0].f_globals[var_name]
            else:
                raise ValueError("The variable", var_name, "was not found by the selection tool.")
            tmp_selection = tmp_selection.replace('@'+var_name, '@auxiliar_variable_'+var_name)
            if type(var_value) in [np.ndarray]:
                var_value = list(var_value)
            locals()['auxiliar_variable_'+var_name]=var_value


    shortcuts = selection_shortcuts['MolSysMT']

    for key in shortcuts:
        if key in selection:
            tmp_selection = tmp_selection.replace(key, shortcuts[key])

    indices = tmp_item.atoms_dataframe.query(tmp_selection).index.to_numpy()

    return indices

def select_with_ParmEd(item, selection):

    from . import convert, get_form
    from parmed.amber import AmberMask as _AmberMask

    form_in = get_form(item)

    if form_in == 'parmed.Structure':
        tmp_item = item
    else:
        tmp_item = convert(item, to_form='parmed.Structure')

    atom_indices = list(_AmberMask(item,selection).Selected())
    del(_AmberMask)

    return tmp_atom_indices

def select_with_Amber(item, selection):

    from . import convert, get_form

    if form_in == 'pytraj.Topology':
        tmp_item = item
    else:
        tmp_item = convert(item, to_form='pytraj.Topology')

    raise NotImplementedMethodError()

def indices_to_selection(molecular_system, indices, element='atom', syntax=None):

    output_string = ''

    if syntax=='NGLView':

        if element=='atom':
            output_string = '@'+','.join([str(ii) for ii in indices])
        elif element=='group':
            from molsysmt import get
            group_ids, chain_ids = get(molecular_system, element='group', selection=indices, group_id=True, chain_id=True)
            if np.all(np.isin(np.unique(chain_ids), [' ', None])):
                output_string = ','.join([str(ii) for ii in group_ids])
            else:
                output_string = ' '.join([str(ii)+':'+str(jj) for ii,jj in zip(group_ids, chain_ids)])
        elif element=='chain':
            from molsysmt import get
            chain_ids = get(molecular_system, element='chain', selection=indices, chain_id=True)
            output_string = ' '.join([':'+ii for ii in chain_ids])
        else:
            raise NotImplementedMethodError

    elif syntax=='MDTraj':

        if element=='atom':
            output_string = 'index '+' '.join([str(ii) for ii in indices])
        elif element=='group':
            output_string = 'resid '+' '.join([str(ii) for ii in indices])
        elif element=='chain':
            output_string = 'chainid '+' '.join([str(ii) for ii in indices])
        else:
            raise NotImplementedMethodError

    else:

        raise NotImplementedMethodError

    return output_string

