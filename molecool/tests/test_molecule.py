''' Contains all tests for the 'molecule' module. '''

import molecool
import numpy as np
import pytest
import pdb


# TEST FIXTURES
@pytest.fixture()
def methane_molecule():
    symbols = ['C', 'H', 'H', 'H', 'H']
    coordinates = np.array([[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
    return symbols, coordinates


# TEST FUNCTIONS


def test_move_methane(methane_molecule):
    symbols, coordinates = methane_molecule

    coordinates[0] += 5


def test_build_bond_list(methane_molecule):
    ''' Tests the build_bond_list function. There are multiple sub-tests.'''

    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    # Test coordinates used above should have 4 bonds using default
    # values for minimum and maximum bond length.

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4

    # Test 2 : Exception should be thrown in min bond length is < 0.
    with pytest.raises(ValueError):
        bonds = molecool.build_bond_list(coordinates, min_bond=-1)


def test_molecular_mass(methane_molecule):
    ''' Tests the molecular_mass function in molecule.py '''

    symbols, coordinates = methane_molecule

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    # assertion below checks if calculated_mass is approximately equal to
    # actual_mass with absolute range on difference.
    assert calculated_mass == pytest.approx(actual_mass, abs=1e-2)


def test_center_of_mass(methane_molecule):
    # symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    # coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    symbols, coordinates = methane_molecule

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1, 1, 1])

    assert np.array_equal(expected_center, center_of_mass)
