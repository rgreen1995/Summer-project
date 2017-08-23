
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle

#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest
g= open('parameters.txt', 'r')

parameters = []
for line in g:
        parameters.append(line.split())   

g.close()


f = open('test.txt', 'r')
lal_data = []

for line in f:
    lal_data.append([float(x) for x in line.split()])
#add parameters as required
m1_freq= [ x[28] for x in lal_data]
m2_freq =[x[31] for x in lal_data ]
chi_p = [x[45] for x in lal_data ]
f.close()    
    #create empty list to store numerics of interest


#use this to search for parameters

#m1=24th index
#m2 = 27th index    
    
#print parameters    
    #loop over all lines the file and add each column to the list as a tuple
    

pycbc_data= np.loadtxt('pycbc_test.txt')

#for line in h :
#    pycbc_data.append(line.split( ))
#h.close()
#pycbc_dat =pickle.dumps(pycbc_data)
#pycbc_dataa = pickle.loads(pycbc_dat)  

#print pycbc_dataa[100]


#    chi_eff = [x[46] for x in data ]
plt.figure(1)

#plt.xlabel('m1')
#plt.ylabel('probability density')

plt.figure(1)
plt.hist(pycbc_data,50, normed=True, color='w')
plt.hist(m1_freq,50, normed=True, color='r')
plt.xlabel('m1')
plt.ylabel('probability density')



"""
plt.figure(2)
plt.hist(m2_freq,50, normed=True)
plt.xlabel('m2')
plt.ylabel('probability density')
plt.figure(3)
plt.hist(chi_p,50, normed=True)
plt.xlabel(r'$\chi_p$')
plt.ylabel('probability density')

"""
