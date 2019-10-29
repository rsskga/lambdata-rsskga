"""
lambdata - a collection of data science helper functions
"""
import pandas as pd
import numpy as np

# sample code
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))


# sample functions
# sample pylint suppression: https://google.github.io/styleguide/pyguide.html
def increment(x): # pylint: disable=invalid-name
    """Testing a pylint fix"""
    return x + 1

def inc_num(num):
    """Rewriting to pass rather than disable pylint"""
    return num + 1
