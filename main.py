"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    ### TODO
    pass
    ###

def subquadratic_multiply(x, y):
    ### TODO
    pass
    ###

## Feel free to add your own tests here.
def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

def test_subquadratic_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000
    
def compare_multiply():
    pass
    # compare the empirical runtimes of multiplication functions
    ### TODO - add test cases and measure runtime
    
    

