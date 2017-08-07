#!/bin/bash

#Specific run we're looking at
RUN=$1

python waveform.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -2.5 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/waveform_plot25

python waveform.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -1.5 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/waveform_plot15

python waveform.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -1.0 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/waveform_plot10

python waveform.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -0.5 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/waveform_plot05

python waveform.py --input-file ${RUN}/output.hdf \
                   --plot-map-waveforms \
                   --min-xlim -0.2 \
                   --injection-file ${RUN}/injection.xml.gz \
                   --output-file ${RUN}/waveform_plot02

# Rename dictionary
#mv ${RUN}/strain_plot_dic.npy final/${RUN}/mapDic.npy
