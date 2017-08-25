from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest
g= open('parameters.txt', 'r')

parameters = []
for line in g:
        parameters.append(line.split())   

g.close()

f = open('SNR_25_inc_0_M30_q2_s1x_0.75_lal.txt', 'r')
lal_data = []

for line in f:
    lal_data.append([float(x) for x in line.split()])
#add parameters as required check parameters list for index
lal_mass1= [ x[28] for x in lal_data]
lal_mass2 =[x[31] for x in lal_data ]
lal_chi_p = [x[52] for x in lal_data ]
lal_chi_eff = [x[69] for x in lal_data ]
lal_q = [x[70] for x in lal_data ]
lal_mc = [x[61] for x in lal_data ]
lal_inc = [x[35] for x in lal_data ]

f.close()
param = ('mass1', 'mass 2', 'chi_p', 'chi_eff', 'q', 'mc') 
inj_vals=(20,10,0.75,0,0.5,12.2)   

    #create empty list to store numerics of interest


#use this to search for parameters

#m1=24th index
#m2 = 27th index    
    
#load in pycbc values, in this code we have loaded values from separate parameter txt files    

pycbc_chi_p= np.loadtxt('chi_p_SNR_25_inc_0_M30_q2_s1x_0.75_py.txt')
pycbc_mass1= np.loadtxt('SNR_25_inc_0_M30_q2_m1_s1x_0.75_py.txt')
pycbc_mass2 = np.loadtxt('SNR_25_inc_0_M30_q2_m1_s1x_0.75_py.txt')
pycbc_chi_eff = np.loadtxt('chi_eff_SNR_25_inc_0_M30_q2_s1x_0.75_py.txt')
pycbc_q = np.loadtxt('q_SNR_25_inc_0_M30_q2_s1x_0.75_py.txt')
pycbc_mc = np.loadtxt('mc_SNR_25_inc_0_M30_q2_s1x_0.75_py.txt')
pycbc_inc = np.loadtxt('inc_SNR_25_inc_0_M30_q2_s1x_0.75_py.txt')

##confidence intervals
pycbc_chi_p_low90 = np.percentile(pycbc_chi_p, 5)
pycbc_chi_p_up90 = np.percentile(pycbc_chi_p, 95)
lal_chi_p_low90 = np.percentile(lal_chi_p, 5)
lal_chi_p_up90 = np.percentile(lal_chi_p, 95)

pycbc_mass1_low90 = np.percentile(pycbc_mass1, 5)
pycbc_mass1_up90 = np.percentile(pycbc_mass1, 95)
lal_mass1_low90 = np.percentile(lal_mass1, 5)
lal_mass1_up90 = np.percentile(lal_mass1, 95)

pycbc_mass2_low90 = np.percentile(pycbc_mass2, 5)
pycbc_mass2_up90 = np.percentile(pycbc_mass2, 95)
lal_mass2_low90 = np.percentile(lal_mass2, 5)
lal_mass2_up90 = np.percentile(lal_mass2, 95)

pycbc_chi_eff_low90 = np.percentile(pycbc_chi_eff, 5)
pycbc_chi_eff_up90 = np.percentile(pycbc_chi_eff, 95)
lal_chi_eff_low90 = np.percentile(lal_chi_eff, 5)
lal_chi_eff_up90 = np.percentile(lal_chi_eff, 95)

pycbc_q_low90 = np.percentile(pycbc_q, 5)
pycbc_q_up90 = np.percentile(pycbc_q, 95)
lal_q_low90 = np.percentile(lal_q, 5)
lal_q_up90 = np.percentile(lal_q, 95)

pycbc_mc_low90 = np.percentile(pycbc_mc, 5)
pycbc_mc_up90 = np.percentile(pycbc_mc, 95)
lal_mc_low90 = np.percentile(lal_mc, 5)
lal_mc_up90 = np.percentile(lal_mc, 95)


pycbc_inc_low90 = np.percentile(pycbc_inc, 5)
pycbc_inc_up90 = np.percentile(pycbc_inc, 95)
lal_inc_low90 = np.percentile(lal_inc, 5)
lal_inc_up90 = np.percentile(lal_inc, 95)


"""
##plotting histograms for posterior distributions for each parameter
plt.figure(1)
plt.grid()
plt.hist(pycbc_chi_p,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_chi_p,50, normed=True, color='b', alpha=0.7, label = 'LAL')
plt.axvline(x= inj_vals[2], linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_chi_p_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_chi_p_up90 , linewidth=2,color='y')
plt.axvline(x= lal_chi_p_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_chi_p_up90 , linewidth=2,color='k')
plt.xlabel(r'$\chi_p$')
plt.ylabel('probability density')
plt.legend(loc='upper right', fontsize= 7)


plt.figure(2)
plt.grid()
plt.hist(pycbc_mass1,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_mass1,50, normed=True, color='b', alpha=0.7, label = 'LAL')
plt.axvline(x= inj_vals[0], linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_mass1_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_mass1_up90 , linewidth=2,color='y')
plt.axvline(x= lal_mass1_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_mass1_up90 , linewidth=2,color='k')
plt.xlabel('mass1')
plt.ylabel('probability density')
plt.legend(loc='upper right' , fontsize = 7)

plt.figure(3)
plt.grid()
plt.hist(pycbc_mass2,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_mass2,50, normed=True, color='b', alpha=0.7, label = 'LAL')
plt.axvline(x= inj_vals[1], linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_mass2_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_mass2_up90 , linewidth=2,color='y')
plt.axvline(x= lal_mass2_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_mass2_up90 , linewidth=2,color='k')
plt.xlabel('mass2')
plt.ylabel('probability density')
plt.legend(loc='upper right', fontsize = 7)


plt.figure(4)
plt.grid()
plt.hist(pycbc_chi_eff,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_chi_eff,50, normed=True, color='b', alpha=0.7, label = 'LAL')
plt.axvline(x= inj_vals[3] , linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_chi_eff_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_chi_eff_up90 , linewidth=2,color='y')
plt.axvline(x= lal_chi_eff_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_chi_eff_up90 , linewidth=2,color='k')
plt.xlabel(r'$\chi_eff$')
plt.ylabel('probability density')
plt.legend(loc='upper right', fontsize= 7)

plt.figure(5)
plt.grid()
plt.hist(pycbc_q,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_q,50, normed=True, color='b', alpha=0.7, label = 'LAL')
plt.axvline(x= inj_vals[4], linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_q_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_q_up90 , linewidth=2,color='y')
plt.axvline(x= lal_q_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_q_up90 , linewidth=2,color='k')
plt.xlabel('q')
plt.ylabel('probability density')
plt.legend(loc='upper right' , fontsize = 7)

plt.figure(6)
plt.grid()
plt.hist(pycbc_mc,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_mc,50, normed=True, color='b', alpha=0.4, label = 'LAL')
plt.axvline(x= inj_vals[5], linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_mc_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_mc_up90 , linewidth=2,color='y')
plt.axvline(x= lal_mc_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_mc_up90 , linewidth=2,color='k')
plt.xlabel('chirp Mass')
plt.ylabel('probability density')
plt.legend(loc='upper left' , fontsize = 6)

plt.figure(7)
plt.grid()
plt.hist(pycbc_inc,50, normed=True, color='r',alpha=0.7, label = 'PyCBC')
plt.hist(lal_inc,50, normed=True, color='b', alpha=0.7, label = 'LAL')
plt.axvline(x=inj_vals[6] , linewidth=2,linestyle='dashed',color='k' , label = 'Injected value')
plt.axvline(x= pycbc_inc_low90 , linewidth=2,color='y' , label = ' PyCBC 90% confidence intervals')
plt.axvline(x= pycbc_inc_up90 , linewidth=2,color='y')
plt.axvline(x= lal_inc_low90 , linewidth=2,color='k' , label = ' LAL 90% confidence intervals')
plt.axvline(x= lal_inc_up90 , linewidth=2,color='k')
plt.xlabel('inc')
plt.ylabel('probability density')
plt.legend(loc='upper right' , fontsize = 7)
"""
# loading in mean values and condfidence intervals
lal_data = (np.average(lal_mass1), np.average(lal_mass2),np.average(lal_chi_p), np.average(lal_chi_eff), np.average(lal_q), np.average(lal_mc))
lal_conf_low = (lal_mass1_low90, lal_mass2_low90, lal_chi_p_low90, lal_chi_eff_low90, lal_q_up90, lal_mc_up90)
lal_conf_up = (lal_mass1_up90, lal_mass2_up90, lal_chi_p_up90, lal_chi_eff_up90, lal_q_up90, lal_mc_up90)
pycbc_data = (np.average(pycbc_mass1), np.average(pycbc_mass2),np.average(pycbc_chi_p), np.average(pycbc_chi_eff), np.average(pycbc_q), np.average(pycbc_mc))
pycbc_conf_low = (pycbc_mass1_low90, pycbc_mass2_low90, pycbc_chi_p_low90, pycbc_chi_eff_low90, pycbc_q_up90, pycbc_mc_up90)
pycbc_conf_up = (pycbc_mass1_up90, pycbc_mass2_up90, pycbc_chi_p_up90, pycbc_chi_eff_up90, pycbc_q_up90, pycbc_mc_up90)


lal_errors=[]
lal_conf_low90=[]
lal_conf_up90 =[]
pycbc_errors = []
pycbc_conf_low90=[]
pycbc_conf_up90 =[]
#loop through values comparing to injected values to give percentage errors
for i in range(0,len(inj_vals)):
    lal_error = float((abs(lal_data[i] - inj_vals[i])/inj_vals[i])*100)
    lal_up_90 = float((abs(lal_conf_up[i] - inj_vals[i])/inj_vals[i])*100)
    lal_low_90 = float((abs(lal_conf_low[i] - inj_vals[i])/inj_vals[i])*100)
    pycbc_error = float((abs(pycbc_data[i] - inj_vals[i])/inj_vals[i] * 100))
    pycbc_up_90 = float((abs(pycbc_conf_up[i] - inj_vals[i])/inj_vals[i])*100)
    pycbc_low_90 = float((abs(pycbc_conf_low[i] - inj_vals[i])/inj_vals[i])*100)
    lal_errors.append(lal_error)
    lal_conf_low90.append(lal_low_90)
    lal_conf_up90.append(lal_up_90)
    pycbc_errors.append(pycbc_error)
    pycbc_conf_low90.append(pycbc_low_90)
    pycbc_conf_up90.append(pycbc_up_90)

lal_conf = (lal_conf_low90, lal_conf_up90)
pycbc_conf = (pycbc_conf_low90, pycbc_conf_up90)

#plot bar chart to compare
N=6
ind = np.arange(N)    # the x locations for the groups
width = 0.4
fig, ax = plt.subplots()
#lal = ax.bar(ind, lal_mass1 , width, color='r')   
#inj = ax.bar(ind+ 2*width, inj_mass1, width, color ='b')                            #actual value
lal = ax.bar(ind, lal_errors,width, color='b', label = 'LAL')                  #percentage error
#pycbc = ax.bar(ind + width, pycbc_mass1 , width, color='y')                           #actual values
pycbc = ax.bar(ind + width, pycbc_errors, width, color='r', label = 'PyCBC')      #percentage errors
ax.set_ylabel('percentage error')
ax.set_xlabel('parameters')
ax.set_title('pycbc v lal percentage errors')
ax.set_xticks(ind + width)
ax.set_xticklabels (param)
plt.legend()
