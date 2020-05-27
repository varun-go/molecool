''' Contains all tests for the 'molecule' module. '''

import molecool
import numpy as np
import pytest

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