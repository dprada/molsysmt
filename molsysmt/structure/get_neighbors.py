from molsysmt._private.digestion import digest
from molsysmt import pyunitwizard as puw
import numpy as np

@digest()
def get_neighbors(molecular_system, selection="all", structure_indices="all", center_of_atoms=False, weights=None,
                  molecular_system_2=None, selection_2=None, structure_indices_2=None, center_of_atoms_2=False, weights_2=None,
                  threshold=None, n_neighbors=None, pbc=False, engine='MolSysMT', syntax='MolSysMT'):
    """
    To be written soon...
    """

    from . import get_distances
    from molsysmt.basic import select

    same_set = False

    same_selections = False
    same_structures = False

    if (selection is not None) and (selection_2 is None):
        same_selections = True

    if structure_indices_2 is None:
        same_structures = True

    same_set= same_selections and same_structures

    all_dists = get_distances(molecular_system=molecular_system, selection=selection,
            structure_indices=structure_indices, center_of_atoms=center_of_atoms, weights=weights,
            selection_2=selection_2, structure_indices_2=structure_indices_2, center_of_atoms_2=center_of_atoms_2,
            weights_2=weights_2, pbc=pbc, engine=engine, syntax=syntax)

    nstructures, nelements_1, nelements_2 = all_dists.shape
    length_units = puw.get_unit(all_dists)
    all_dists = puw.get_value(all_dists)

    if n_neighbors is not None and threshold is None:

        neighs=np.empty((nstructures, nelements_1, n_neighbors), dtype=int)
        dists=np.empty((nstructures, nelements_1, n_neighbors), dtype=float)

        offset = 0
        if same_set:
            offset = 1

        for indice_structure in range(nstructures):
            for ii in range(nelements_1):
                neighs_aux = np.argpartition(all_dists[indice_structure,ii,:], n_neighbors-1+offset)[:n_neighbors+offset]
                dists_aux = all_dists[indice_structure,ii,neighs_aux]
                good_order = np.argsort(dists_aux)
                neighs_aux = neighs_aux[good_order]
                dists_aux = dists_aux[good_order]
                neighs[indice_structure,ii,:]=neighs_aux[offset:]
                dists[indice_structure,ii,:]=dists_aux[offset:]
                if same_set:
                    if dists_aux[0] > 0.01:
                        raise ValueError("Error in algorithm, sets are different.")

        del(all_dists)

        dists=dists*length_units

    elif threshold is not None and n_neighbors is None:

        threshold = puw.get_value(threshold, to_unit=length_units)

        neighs=np.empty((nstructures, nelements_1), dtype=object)
        dists=np.empty((nstructures, nelements_1), dtype=object)

        offset = 0
        if same_set:
            offset = 1

        for indice_structure in range(nstructures):
            for ii in range(nelements_1):
                neighs_aux = np.argwhere(all_dists[indice_structure,ii,:]<=threshold)[:,0]
                dists_aux = all_dists[indice_structure,ii,neighs_aux]
                good_order = np.argsort(dists_aux)
                neighs_aux = neighs_aux[good_order]
                dists_aux = dists_aux[good_order]
                neighs[indice_structure,ii]=np.array(neighs_aux,dtype=int)[offset:]
                dists[indice_structure,ii]=np.array(dists_aux,dtype=float)[offset:]
                if same_set:
                    if dists_aux[0] > 0.01:
                        raise ValueError("Error in algorithm, sets are different.")

        del(all_dists)

        dists=dists*length_units

    else:

        raise ValueError("Use either threshold or n_neighbors, but not both at the same time")


    return neighs, dists

