from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

inj_m1 = 20
#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest
f= open('parameters.txt', 'r')
parameters = []
for line in f:
        parameters.append(line.split()) 
f.close()

SNR_25_inc_0_m25_q4_m1_s1x_0_75_py = np.loadtxt('SNR_25_inc_0_M25_q4_m1_s1x_0.75_py.txt')
SNR_25_inc_0_m30_q2_m1_s1x_0_75_py = np.loadtxt('SNR_25_inc_0_M30_q2_m1_s1x_0.75_py.txt')
SNR_25_inc_0_m45_q8_m1_s1x_0_75_py =np.loadtxt('SNR_25_inc_0_M45_q8_m1_s1x_0.75_py.txt')


SNR_25_inc_0_m25_q4_m1_s1x_0_75_py_90_lower = np.percentile(SNR_25_inc_0_m25_q4_m1_s1x_0_75_py,5)
SNR_25_inc_0_m25_q4_m1_s1x_0_75_py_90_upper = np.percentile(SNR_25_inc_0_m25_q4_m1_s1x_0_75_py,95)
SNR_25_inc_0_m25_q4_m1_s1x_0_75_py_map = np.average(SNR_25_inc_0_m25_q4_m1_s1x_0_75_py)

SNR_25_inc_0_m30_q2_m1_s1x_0_75_py_90_lower = np.percentile(SNR_25_inc_0_m30_q2_m1_s1x_0_75_py,5)
SNR_25_inc_0_m30_q2_m1_s1x_0_75_py_90_upper = np.percentile(SNR_25_inc_0_m30_q2_m1_s1x_0_75_py,95)
SNR_25_inc_0_m30_q2_m1_s1x_0_75_py_map = np.average(SNR_25_inc_0_m30_q2_m1_s1x_0_75_py)


SNR_25_inc_0_m45_q8_m1_s1x_0_75_py_90_lower = np.percentile(SNR_25_inc_0_m45_q8_m1_s1x_0_75_py, 5)
SNR_25_inc_0_m45_q8_m1_s1x_0_75_py_90_upper = np.percentile(SNR_25_inc_0_m45_q8_m1_s1x_0_75_py,95)
SNR_25_inc_0_m45_q8_m1_s1x_0_75_py_map = np.average(SNR_25_inc_0_m45_q8_m1_s1x_0_75_py)

pycbc_m1 = (SNR_25_inc_0_m25_q4_m1_s1x_0_75_py_map,SNR_25_inc_0_m30_q2_m1_s1x_0_75_py_map,SNR_25_inc_0_m45_q8_m1_s1x_0_75_py_map )
pycbc_m1_lower = (SNR_25_inc_0_m25_q4_m1_s1x_0_75_py_90_lower,SNR_25_inc_0_m30_q2_m1_s1x_0_75_py_90_lower,SNR_25_inc_0_m45_q8_m1_s1x_0_75_py_90_lower )
pycbc_m1_upper = (SNR_25_inc_0_m25_q4_m1_s1x_0_75_py_90_upper,SNR_25_inc_0_m30_q2_m1_s1x_0_75_py_90_upper,SNR_25_inc_0_m45_q8_m1_s1x_0_75_py_90_upper )
inj_mass1 = (10,20,40)

list_of_pycbc_mass1_error=[]
list_of_pycbc_mass1_lower = []
list_of_pycbc_mass1_upper = []
for i in range (0,len(inj_mass1)):
    pycbc_mass1_error = float(abs((pycbc_m1[i] - inj_mass1[i])/inj_mass1[i])*100)
    pycbc_mass1_lower = float(abs((pycbc_m1_lower[i] - inj_mass1[i])/inj_mass1[i])*100)
    pycbc_mass1_upper = float(abs((pycbc_m1_upper[i] - inj_mass1[i])/inj_mass1[i])*100)
    list_of_pycbc_mass1_error.append(pycbc_mass1_error)
    list_of_pycbc_mass1_lower.append(pycbc_mass1_lower)
    list_of_pycbc_mass1_upper.append(pycbc_mass1_upper)
    

print pycbc_m1
print list_of_pycbc_mass1_error

conf_90 = ((list_of_pycbc_mass1_lower),(list_of_pycbc_mass1_upper))
pycbc_mass1 = list_of_pycbc_mass1_error

plt.errorbar(inj_mass1, pycbc_mass1, yerr=conf_90, color ='r')
plt.xlim(0,50)
plt.ylim(0,75)
