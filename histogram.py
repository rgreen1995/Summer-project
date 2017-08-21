
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

test=(1,2.3,3,4,5,6,6,7,7,88,9,)
#m1=24th index
#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest
f = open('test.txt', 'r')
    
    #create empty list to store numerics of interest
data = []
    
    #loop over all lines the file and add each column to the list as a tuple
for line in f:
    data.append([float(x) for x in line.split()])
    m1_freq= [ x[24] for x in data]
    
plt.hist(m1_freq,50, normed=True)
plt.xlabel('m1')
plt.ylabel('probability density')
