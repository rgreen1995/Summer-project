#!/bin/bash

#Specific run we're looking at
RUN=$1

python injected.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -2.5 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/injected_plot25

python injected.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -1.5 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/injected_plot15

python injected.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -1.0 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/injected_plot10

python injected.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -0.5 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/injected_plot05

python injected.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -0.2 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/injected_plot02

# Rename dictionary
#mv ${RUN}/strain_plot_dic.npy final/${RUN}/mapDic.npy
