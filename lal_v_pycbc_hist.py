import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pycbc.io import InferenceFile
import sys
from lalsimulation import SimInspiralTransformPrecessingNewInitialConditions
from pycbc.waveform import get_td_waveform

print "Initialising..."

num_walkers=5000 ## <<<-- MAKE SURE THIS IS CORRECT, HAS TO BE DONE MANUALLY

## Select file
folder=sys.argv[1]
folder=folder+"/"

## Combine inputs to form variables
data_name="output.hdf"

## Determine what parameters to plot
whatdo=raw_input("What parameters do you want to plot? \n")

param=mass1


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
