''' Contains all tests for the 'molecule' module. '''

import molecool
import numpy as np
import pytest
import pdb

def test_build_bond_list():
    ''' Tests the build_bond_list function. There are multiple sub-tests.'''
    
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
        ])

    bonds = molecool.build_bond_list(coordinates)

    # Test coordinates used above should have 4 bonds using default
    # values for minimum and maximum bond length.

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4

    # Test 2 : Exception should be thrown in min bond length is < 0.
    with pytest.raises(ValueError):
        bonds = molecool.build_bond_list(coordinates, min_bond=-1)

def test_molecular_mass():
    ''' Tests the molecular_mass function in molecule.py '''

    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)
    
    actual_mass = 16.04

    # assertion below checks if calculated_mass is approximately equal to 
    # actual_mass with absolute range on difference.
    assert calculated_mass == pytest.approx(actual_mass, abs=1e-2)