"""
Unit and regression test for measure module. 
"""

import molecool
import numpy as np 

def test_calculate_distance():
    """ Test to ensure that calculate_distance returns expected value."""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    # if the value of assert is true, no issue
    # if assert's value is false, then there will be an assertion error
    assert expected_distance == calculated_distance

def test_calculate_angle():
    """ Test function calculate_angle to ensure it returns expected value."""

    r1 = np.array([0.0, 0.0, -1.0])
    r2 = np.array([0.0, 0.0, 0.0])
    r3 = np.array([1.0, 0.0, 0.0])

    calculated_angle = round(molecool.calculate_angle(r1, r2, r3, degrees=True), 4)
    expected_angle = 90.0

    assert expected_angle == calculated_angle