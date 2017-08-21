import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pycbc.io import InferenceFile
import sys
from lalsimulation import SimInspiralTransformPrecessingNewInitialConditions
from pycbc.waveform import get_td_waveform

f = open('test.txt', 'r')

   
#create empty list to store numerics of interest
#parameters = []
data = []

#for line in g: 
#    parameters.append(float(x) for x in line.split())
    
#m1=24th index
#m2 = 27th index    
    
#print parameters    
    #loop over all lines the file and add each column to the list as a tuple
for line in f:
    data.append([float(x) for x in line.split()])
    m1_freq= [ x[24] for x in data]
    m2_freq = [x[27] for x in data ]
#plt.figure(1)
#plt.hist(m1_freq,50, normed=True)
#plt.xlabel('m1')
#plt.ylabel('probability density')

#plt.figure(2)
#plt.hist(m2_freq,50, normed=True)
#plt.xlabel('m2')
#plt.ylabel('probability density')

print "Initialising..."

num_walkers=5000 ## <<<-- MAKE SURE THIS IS CORRECT, HAS TO BE DONE MANUALLY

## Select file
folder=sys.argv[1]
folder=folder+"/"

## Combine inputs to form variables
data_name="output.hdf"

## Determine what parameters to plot
whatdo=raw_input("What parameters do you want to plot? \n")

## List of parameters add in as required
params=np.array(["mass1","mass2",])


def getParameter(parameter):
   ## Prepare to read in parameters
   datafile=folder+data_name
   fp = InferenceFile("%s" % datafile, "r")
   
   ## Take last iteration of each walker
   parameter_values=np.array([])
   for aa in range(num_walkers):
      samples = fp.read_samples("%s" % parameter, walkers=aa)
      temp=getattr(samples,parameter)
      parameter_values=np.append(parameter_values,temp[-1])
   return parameter_values

def plotPosterior(parameter):
    ## Ensure m1>m2 in posteriors
   if parameter=="mass1":
      mass1=getParameter("mass1")
      mass2=getParameter("mass2")
      parameter_values=np.zeros(len(mass1))
      for aa in range(len(mass1)):
         parameter_values[aa]=max(mass1[aa],mass2[aa])
      plt.figure()
      plt.hist(m1_freq,50, normed=True)
      
   ## Ensure m2>m1 in posteriors
   elif parameter=="mass2":
      mass1=getParameter("mass1")
      mass2=getParameter("mass2")
      parameter_values=np.zeros(len(mass1))
      for aa in range(len(mass1)):
         parameter_values[aa]=min(mass1[aa],mass2[aa])
      plt.figure()
      plt.hist(m2_freq,50, normed=True)
      
      
   else:
      parameter_values=getParameter(parameter)
      values=len(parameter_values)
   savename=folder+parameter   
   values=len(parameter_values)
   ## Find confidence intervals
   parameter_values=np.sort(parameter_values)
   lower_90=parameter_values[250]
   upper_90=parameter_values[4749]
   mean_val=np.average(parameter_values)
   
   ## Plot and save
   plt.figure()
   plt.title("%d data points" % (values))
   plt.hist(parameter_values,50, normed=True, alpha=0.9)
 #  plt.axvline(x=lower_90,linewidth=2,linestyle='dashed',color='k')
 # plt.axvline(x=mean_val,linewidth=2, color='k')
 # plt.axvline(x=upper_90,linewidth=2,linestyle='dashed',color='k')
   plt.xlabel("%s" % parameter)
   plt.grid()
   # Removed the priors, add them if you fancy
   ## Plot priors for derived spin parameters
   #if parameter=="chi_p":
      #prior=np.loadtxt("priors/chi_p_prior.txt")
      #plt.hist(prior,50,normed=True,alpha=0.6)
   #elif parameter=="chi_eff":
      #prior=np.loadtxt("priors/chi_eff_prior.txt")
      #plt.hist(prior,50,normed=True,alpha=0.6)
   plt.savefig("%s.png" % savename)
   print "Plot saved as %s.png" % savename


## Execute
if whatdo=="all":
  print "Generating posteriors for all parameters..."
  for aa in range(len(params)):
    plotPosterior(params[aa])
else:
  print "Generating posterior for %s" % whatdo
  plotPosterior(whatdo)

print "DONE"
