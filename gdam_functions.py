"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math as m
import numpy as np

# Define your new functions below
def gaussian(mean, stddev, x):
    """
    Function for calculating 

    Parameters
    ------------
    x: <list>
        def
    mean: <numerical>
        def

    stddev: <numerical>
        def

    Returns
    -------------
    <float>
        def
    """
    normal = []
    for y in x:
        gauss = (np.exp(-(y-mean)**2/(2*stddev**2)))/(stddev*np.sqrt(2*np.pi))
        normal.append(gauss)
    return normal

    