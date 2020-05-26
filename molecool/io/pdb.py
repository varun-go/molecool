"""
Functions for manipulating pdb files. 
"""
import os
import numpy as np

def open_pdb(file_location):
    '''
        Reads in a pdb file and returns the atom names and coordinates.
    '''
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            symbols.append(l[76:79].strip())
            try:
                c2 = [float(x) for x in l[30:55].split()]
            except ValueError as error:
                print(error + ": The pdb file format is not properly formatted. Coordinates must be in columns 30 through 55.")
            else:
                coordinates.append(c2)

    coords = np.array(coordinates)

    return symbols, coords   