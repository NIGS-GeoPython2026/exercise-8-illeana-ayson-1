"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math as m
import numpy as np

# Define your new functions below
def gaussian(mean, stddev, x):
    
    """
    Function for calculating gaussian distribution

    Parameters
    ------------
    x: <list>
        list of values for which the normal distribution will be calculated
    mean: <numerical>
        average
    stddev: <numerical>
        standard deviation

    Returns
    -------------
    <list>
        list of calculated normal distribution for x
    """
    
    #create new list to store calculated values
    normal = []
    
    #iterate for all values in x
    for y in x:
        
        #gaussian function formula
        gauss = (np.exp(-(y-mean)**2/(2*stddev**2)))/(stddev*np.sqrt(2*np.pi))
        
        #add to list
        normal.append(gauss)
        
    #return list of calculated values
    return normal

    