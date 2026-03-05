import utils
from scipy.integrate import quad
from math import isclose

def test_fact():
    assert utils.fact(3) == 6

def test_roots():
    assert utils.roots(1,0,-1) == (-1,1)

def test_integrate():
    assert utils.integrate("2*x", 0, 2) == 4.0
    
