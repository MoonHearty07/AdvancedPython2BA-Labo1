import pytest
import utils
from scipy.integrate import quad

def test_fact():
    assert utils.fact(3) == 6
    assert utils.fact(4) == 24

def test_roots():
    assert utils.roots(1,0,-1) == (-1,1)
    assert utils.roots(1,0,-4) == (-2,2)

def test_integrate():
    
    def integrand(x, a, b):
        return a*x**b
    
    assert utils.integrate(integrand, -5, 7) == quad(integrand, -5, 7, args=(1,2))
    
