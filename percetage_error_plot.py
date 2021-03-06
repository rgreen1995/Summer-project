from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


inj_mass1 = [60,70,80,90,100]
lal_mass1 = [61.7, 74, 79, 92, 105]
pycbc_mass1 = [54, 76 ,82,86,110]
list_of_pycbc_mass1_error=[]
list_of_lal_mass1_error=[]
for i in range (0,5):
    pycbc_mass1_error = float(abs((pycbc_mass1[i] - inj_mass1[i])/inj_mass1[i])*100)
    lal_mass1_error = float(abs((lal_mass1[i] - inj_mass1[i])/inj_mass1[i])*100)
    list_of_pycbc_mass1_error.append(pycbc_mass1_error)
    list_of_lal_mass1_error.append(lal_mass1_error)
print list_of_pycbc_mass1_error
print list_of_lal_mass1_error  

N=5
ind = np.arange(N)    # the x locations for the groups
width = 0.2       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
lal = ax.bar(ind, lal_mass1 , width, color='r')   
inj = ax.bar(ind+ 2*width, inj_mass1, width, color ='b')                            #actual value
#lal = ax.bar(ind, list_of_lal_mass1_error , width, color='r',)                  #percentage error
pycbc = ax.bar(ind + width, pycbc_mass1 , width, color='y')                           #actual values
#pycbc = ax.bar(ind + width, list_of_pycbc_mass1_error , width, color='y',)      #percentage errors
ax.set_ylabel('percentage error')
ax.set_xlabel('mass1')
ax.set_title('pycbc v lal percentage errors')
ax.set_xticks(ind + width/2)
ax.set_xticklabels (('60', '70', '80', '90','100'))
ax.legend([lal,pycbc], ['LAL', 'PyCBC'])
