
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

inj_m1 = 20


f= open('parameters.txt', 'r')
parameters = []
for line in f:
        parameters.append(line.split())   

f.close()


g = open('SNR_25_mode_PhenomPv2_inc_0.0_M30_q2_s1x_0.75.txt', 'r')
lal_data = []
for line in g:
    lal_data.append([float(x) for x in line.split()])
g.close()  
#add parameters as required
lal_m1= [ x[28] for x in lal_data]
lal_m2 =[x[31] for x in lal_data ]
lal_chi_p = [x[45] for x in lal_data ]
 
lal_m1_lower_90 = np.percentile(lal_m1,5)
lal_m1_upper_90 = np.percentile(lal_m1, 95)
lal_m1_map = 20.5246013637

pycbc_m1_data= np.loadtxt('py_M30_test.txt')

pycbc_m1_lower_90 = np.percentile(pycbc_m1_data, 5)
pycbc_m1_upper_90 = np.percentile(pycbc_m1_data, 95)
pycbc_map_m1 = np.average(pycbc_m1_data)
