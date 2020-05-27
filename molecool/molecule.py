"""
Functions associated with a molecule.
"""

from .measure import calculate_distance 
from .atom_data import atomic_weights

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """Return the bonds in a system based on bond distance criteria.

    The pairwise distance between atoms is computed. If the distance 
    is within the range 'min_bond' and 'max_bond", the atoms are counted as bonded.

    Parameters
    ----------
    coordinates : np.ndarray 
        The coordinates of the atoms.
    max_bond : float (optional)
        The maximum distance to be considered bonded. Default = 1.5
    min_bond : float (optional)
        The minimum distance to be considered bonded. Default = 0

    Returns
    -------
    bonds : dict
        A dictionary where the keys are tuples of the bonded atom indices,
        and the associated values are the bond lengths.
    """ 

    # Throwing exceptions
    if min_bond < 0:
        raise ValueError("Invalid minimum bond distance entered! Minimum bond       distance must be greater than zero!")


    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """
    mass = 0.0

    for atom in symbols:
       mass  += atomic_weights[atom]

    return mass

def calculate_center_of_mass(symbols, coordinates):
   """Calculate the center of mass of a molecule.
   
   The center of mass is weighted by each atom's weight.
   
   Parameters
   ----------
   symbols : list
       A list of elements for the molecule
   coordinates : np.ndarray
       The coordinates of the molecule.
   
   Returns
   -------
   center_of_mass: np.ndarray
       The center of mass of the molecule.

   Notes
   -----
   The center of mass is calculated with the formula
   
   .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
   
   """

   return np.array([])



