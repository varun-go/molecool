"""
Functions for calculations 
"""

import numpy as np

def calculate_angle(rA, rB, rC, degrees=False):
    """Calculate the angle between three points. 

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        The coordinates of each point. 
    degrees : boolean, optional
        Specifies whether angle should be in degrees.

    Returns
    -------
    angle : float
        The angle between the three points. 

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> r3 = np.array([0.0, 1.0, 0.0])
    >>> calculate_angle(r1, r2, r3)
    0.7853

    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> r3 = np.array([0.0, 1.0, 0.0])
    >>> calculate_angle(r1, r2, r3, True)
    45.000001
    """
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
    

def calculate_distance(rA, rB):
    """
    Calculate the distance between two points. 

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point. 

    Returns
    -------
    distance : float
        The distance between the two points. 

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> calculate_distance(r1, r2)
    1.0
    """
    # Above docstring is in the numpy formatting style.

    # This function calculates the distance between two points given as numpy arrays.

    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray) is False:
        raise TypeError("rA and rB must be numpy arrays")
    
    dist_vec = (rA-rB)
    distance = np.linalg.norm(dist_vec)

    if dist == 0.0:
        raise Exception("Two atoms are located at the same point.")
    return dist