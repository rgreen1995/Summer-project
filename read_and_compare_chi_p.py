from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#open file from which we want to read data
#for this to work, we must have our python file saved in the same directory as the data file of interest
parameter= open('parameters_87.txt', 'r')

parameters = []

for line in parameter:
        parameters.append(line.split()) 

runs = [np.loadtxt("cory_run_%d.txt" % i ) for i in range(84, 99)]
#np.loadtxt('cory_run_97.txt')



# will make it this once we get data run_84= runs[0]
run_84 = runs[0]
run_85 = runs[1]
run_86 = runs[2]
run_87= runs[3]
run_88 = runs[4]
run_89 = runs[5]
run_90 = runs[6]
run_91 = runs[7]
run_92 = runs[8]
run_93 = runs[9]
run_94 = runs[10]
run_95 = runs[11]
run_96= runs[12]
run_97 = runs[13]
run_98 = runs[12]

chi_p_84=[]
chi_p_85 =[]
chi_p_86=[]
chi_p_87=[]
chi_p_88=[]
chi_p_89=[]
chi_p_90=[]
chi_p_91=[]
chi_p_92=[]
chi_p_93=[]
chi_p_94=[]
chi_p_95 =[]
chi_p_96 =[]
chi_p_97 =[]
chi_p_98 =[]

#chi_p = x[52]

for i in range(0,len(run_84)):
   chi_p_84.append(run_84[i,52])

#for i in range(0,len(run_85)):
#   chi_p_85.append(run_85[i,52])

for i in range(0,len(run_86)):
   chi_p_86.append(run_86[i,52])
   
for i in range(0,len(run_87)):
   chi_p_87.append(run_87[i,52])
    
for i in range(0,len(run_88)):
    chi_p_88.append(run_88[i,52])

for i in range(0,len(run_89)):
    chi_p_89.append(run_89[i,52]) 
    
for i in range(0,len(run_90)):
    chi_p_90.append(run_90[i,52])

for i in range(0,len(run_91)):
    chi_p_91.append(run_91[i,52])    

for i in range(0,len(run_92)):
    chi_p_92.append(run_92[i,52])

for i in range(0,len(run_93)):
    chi_p_93.append(run_93[i,52])

for i in range(0,len(run_94)):
    chi_p_94.append(run_94[i,52])  

#for i in range(0,len(run_95)):
#    chi_p_95.append(run_95[i,52])  

for i in range(0,len(run_96)):
    chi_p_96.append(run_96[i,52])  

for i in range(0,len(run_97)):
   chi_p_97.append(run_97[i,52])  

for i in range(0,len(run_98)):
   chi_p_98.append(run_98[i,52])  
    
    
    
inj_chi_p=0.5
error_chi_p_84 = abs(((np.average(chi_p_84) - inj_chi_p))/inj_chi_p)*100 
chi_p_84_up_90 = abs((np.percentile(chi_p_84, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_84_low_90 = abs((np.percentile(chi_p_84, 5) - inj_chi_p)/inj_chi_p)*100

error_chi_p_85 = abs(((np.average(chi_p_85) - inj_chi_p))/inj_chi_p)*100 
#chi_p_85_up_90 = abs((np.percentile(chi_p_85, 95) - inj_chi_p)/inj_chi_p)*100
#chi_p_85_low_90 = abs((np.percentile(chi_p_85, 5) - inj_chi_p)/inj_chi_p)*100

error_chi_p_86 = abs(((np.average(chi_p_86) - inj_chi_p))/inj_chi_p)*100
chi_p_86_up_90 = abs((np.percentile(chi_p_86, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_86_low_90 = abs((np.percentile(chi_p_86, 5) - inj_chi_p)/inj_chi_p)*100
 
error_chi_p_87 = abs(((np.average(chi_p_87) - inj_chi_p))/inj_chi_p)*100 
chi_p_87_up_90 = abs((np.percentile(chi_p_87, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_87_low_90 = abs((np.percentile(chi_p_87, 5) - inj_chi_p)/inj_chi_p)*100

error_chi_p_88 = abs(((np.average(chi_p_88) - inj_chi_p))/inj_chi_p)*100 
chi_p_88_up_90 = abs((np.percentile(chi_p_88, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_88_low_90 = abs((np.percentile(chi_p_88, 5) - inj_chi_p)/inj_chi_p)*100

error_chi_p_89 = abs(((np.average(chi_p_89) - inj_chi_p))/inj_chi_p)*100
chi_p_89_up_90 = abs((np.percentile(chi_p_89, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_89_low_90 = abs((np.percentile(chi_p_89, 5) - inj_chi_p)/inj_chi_p)*100
 
error_chi_p_90 = abs(((np.average(chi_p_90) - inj_chi_p))/inj_chi_p)*100  
chi_p_90_up_90 = abs((np.percentile(chi_p_90, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_90_low_90 = abs((np.percentile(chi_p_90, 5) - inj_chi_p)/inj_chi_p)*100   
    
error_chi_p_91 = abs(((np.average(chi_p_91) - inj_chi_p))/inj_chi_p)*100
chi_p_91_up_90 = abs((np.percentile(chi_p_91, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_91_low_90 = abs((np.percentile(chi_p_91, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_92 = abs(((np.average(chi_p_92) - inj_chi_p))/inj_chi_p)*100 
chi_p_92_up_90 = abs((np.percentile(chi_p_92, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_92_low_90 = abs((np.percentile(chi_p_92, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_93 =abs(((np.average(chi_p_93) - inj_chi_p))/inj_chi_p)*100 
chi_p_93_up_90 = abs((np.percentile(chi_p_93, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_93_low_90 = abs((np.percentile(chi_p_93, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_94 =abs(((np.average(chi_p_94) - inj_chi_p))/inj_chi_p)*100 
chi_p_94_up_90 = abs((np.percentile(chi_p_94, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_94_low_90 = abs((np.percentile(chi_p_94, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_95 =abs(((np.average(chi_p_95) - inj_chi_p))/inj_chi_p)*100 
#chi_p_95_up_90 = abs((np.percentile(chi_p_95, 95) - inj_chi_p)/inj_chi_p)*100
#chi_p_95_low_90 = abs((np.percentile(chi_p_95, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_96 =abs(((np.average(chi_p_96) - inj_chi_p))/inj_chi_p)*100 
chi_p_96_up_90 = abs((np.percentile(chi_p_96, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_96_low_90 = abs((np.percentile(chi_p_96, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_97 =abs(((np.average(chi_p_97) - inj_chi_p))/inj_chi_p)*100 
chi_p_97_up_90 = abs((np.percentile(chi_p_97, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_97_low_90 = abs((np.percentile(chi_p_97, 5) - inj_chi_p)/inj_chi_p)*100  

error_chi_p_98 =abs(((np.average(chi_p_98) - inj_chi_p))/inj_chi_p)*100 
chi_p_98_up_90 = abs((np.percentile(chi_p_98, 95) - inj_chi_p)/inj_chi_p)*100
chi_p_98_low_90 = abs((np.percentile(chi_p_98, 5) - inj_chi_p)/inj_chi_p)*100  




#mean_chi_p_95 = np.average(chi_p_95)
plt.figure()
plt.hist(chi_p_87,50, normed = True, color = 'b',alpha=0.7, label = 'M70_q6_inclination = pi/3')
plt.hist(chi_p_90,50, normed = True, color = 'r',alpha=0.6, label = 'M70_q6_inclination = pi/4')
plt.hist(chi_p_93,50, normed = True, color = 'c',alpha=0.5, label = 'M70_q6_inclination = pi/6')
plt.hist(chi_p_96,50, normed = True, color = 'y',alpha=0.4, label = 'M70_q6_inclination = pi/8')
plt.hist(chi_p_84,50, normed = True, color = 'k',alpha=0.3, label = 'M70_q6_inclination = 0')
plt.xlabel(r'$\chi_p$')
plt.ylabel('probability density')
plt.legend(loc='best', fontsize = 8)

M70_q6 = (error_chi_p_87, error_chi_p_90,error_chi_p_93, error_chi_p_96, error_chi_p_84)
M70_q6_conf = ((chi_p_87_low_90,chi_p_90_low_90, chi_p_93_low_90 , chi_p_96_low_90 ,chi_p_84_low_90),(chi_p_87_up_90,chi_p_90_up_90, chi_p_93_up_90 , chi_p_96_up_90 ,chi_p_84_up_90))
M80_q7 = (error_chi_p_88, error_chi_p_91, error_chi_p_94, error_chi_p_97, error_chi_p_85)
#M80_q7_conf = ((chi_p_88_low_90,chi_p_91_low_90, chi_p_94_low_90 , chi_p_97_low_90 ,chi_p_85_low_90),(chi_p_88_up_90,chi_p_91_up_90, chi_p_94_up_90 , chi_p_97_up_90 ,chi_p_85_up_90))
M90_q8 = (error_chi_p_89, error_chi_p_92, error_chi_p_95, error_chi_p_98, error_chi_p_86)
#M90_q8_conf = ((chi_p_89_low_90,chi_p_92_low_90, chi_p_95_low_90 , chi_p_98_low_90 ,chi_p_86_low_90),(chi_p_89_up_90,chi_p_92_up_90, chi_p_95_up_90 , chi_p_98_up_90 ,chi_p_86_up_90))

inclination = [60, 45, 30,22,0 ]
plt.figure()
plt.grid()
#plt.errorbar(inclination, M70_q6, yerr= M70_q6_conf ,color = 'b',label = 'M70_q6')
plt.plot(inclination, M70_q6 ,color = 'b',label = 'M70_q6')
#plt.plot(inclination, M80_q7, yerr= M80_q7_conf ,color = 'r',label = 'M80_q7')
#plt.plot(inclination, M90_q8, yerr= M90_q8_conf ,color = 'y', label = 'M90_q8')
plt.ylabel('percentage error in ' r'$\chi_p$')
plt.xlabel('inclination (in degrees)')
plt.legend(loc='upper left', fontsize=10.5)
