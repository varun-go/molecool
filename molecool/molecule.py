"""
Functions associated with a molecule.
"""

from .measure import calculate_distance 

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """
    Find the bonds in a molecule (set of coordinates) based on distance criteria.

    Parameters
    ----------
    coordinates : list 
        A list of numpy.arrays corresponding to atomic locations.

    max_bond : float, optional
        Specifies the maximum for the bond length.

    min_bond : float, optional
        Specifies the minimum for the bond length.

    Returns
    -------
    ax : histogram
        A histogram representation of all bond lengths.

    """ 

    # Throwing exceptions
    if min_bond < 0:
        raise ValueError("Minimum bond length cannot be less than 0")
    
       
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds