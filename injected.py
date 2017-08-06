#! /usr/bin/env python
import h5py
import copy
import argparse
from pycbc import DYN_RANGE_FAC, pnutils
from pycbc.io import InferenceFile
from pycbc.inference import option_utils
from pycbc.types import TimeSeries, FrequencySeries
from pycbc import strain as pystrain
from pycbc.waveform import generator
from pycbc.filter import highpass_fir, matched_filter
import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from pycbc.filter import match


def get_ylim(data, times, tmin, tmax):
    selected = data[(times >= tmin) & (times < tmax)]
    return 1.1*selected.min(), 1.1*selected.max()


parser = argparse.ArgumentParser()
option_utils.add_inference_results_option_group(parser)
parser.add_argument('--injection-file')
parser.add_argument('--plot-map-waveforms', action='store_true', default=False)
parser.add_argument('--output-file', required=True)
parser.add_argument('--min-xlim')
opts = parser.parse_args()
fp, parameters, _, samples = option_utils.results_from_cli(opts)

## Extract file location from argument
directorys=opts.output_file
folder=directorys[:21]
print folder

tc_inj= 1126259462.0 
mass1_inj = 80. 
mass2_inj = 10. 
ra_inj = 2.21535724066 
dec_inj = -1.23649695537 
inclination_inj = 1.047197551 
coa_phase_inj = 0.0 
polarization_inj = 0.8 
theta_JN_inj = 2.7 
distance_inj = 500000

spin1_a_inj = 0.75 
spin1_azimuthal_inj = 0.0
spin1_polar_inj =0.0
spin2_a_inj = 0.0 
spin2_azimuthal_inj = 0.0
spin2_polar_inj =0.0

injvals=[tc_inj,mass1_inj,mass2_inj,spin1_a_inj,spin1_azimuthal_inj,spin1_polar_inj,spin2_a_inj,spin2_azimuthal_inj, spin2_polar_inj, distance_inj, coa_phase_inj, inclination_inj, polarization_inj, ra_inj, dec_inj ]

snr_list=[]

fig = pyplot.figure()
ii = 0
colors = {'H1': 'r', 'L1': 'g'}
for ifo in ['H1', 'L1']:
    ii += 1
    ax = fig.add_subplot(int('21{}'.format(ii)))
    print ifo
    # get the psd
    print "loading psd"
    psd = FrequencySeries(fp['{}/psds/0'.format(ifo)][:],
        delta_f=fp['{}/psds/0'.format(ifo)].attrs['delta_f'])\
        /DYN_RANGE_FAC**2

    asd = FrequencySeries(numpy.sqrt(psd.numpy()), delta_f=psd.delta_f)
    # get the strain
    print "loading strain"
    stilde = FrequencySeries(fp['{}/stilde'.format(ifo)][:],
        delta_f=fp['{}/stilde'.format(ifo)].attrs['delta_f'],
        epoch=fp['{}/stilde'.format(ifo)].attrs['epoch'])

    print "whitening"
    wh_stilde = FrequencySeries(stilde / asd, delta_f=stilde.delta_f,
                                 epoch=stilde.epoch)
    wh_strain = wh_stilde.to_timeseries()

    print "generating injected waveforms"

    genclass = generator.select_waveform_generator(fp.static_args['approximant'])
    gen = generator.FDomainDetFrameGenerator(
        genclass,
        detectors=['H1', 'L1'], epoch=stilde.epoch,
        variable_args=varargs,
        **sargs)
    fis= gen.generate(tc=injvals[0], mass1= injvals[1], mass2=injvals[2], spin1_a= injvals[3], spin1_azimuthal= injvals[4], spin1_polar=injvals[5], spin2_a=injvals[6],spin2_azimuthal= injvals[7], spin2_polar=injvals[8], distance=injvals[9], coa_phase=injvals[10], inclination=injvals[11],polarization=injvals[12], ra=injvals[13], dec=injvals[14])[ifo]
    if len(fis) < len(psd):
        fis.resize(len(psd))
    elif len(psd) < len(fis):
        fis = fis[:len(psd)]
    fis /= asd
    ins = fis.to_timeseries()

    print "plotting"

    try:
        gps_time = sargs['tc']
    except KeyError:
        gps_time = map_values['tc']
    xmin = float(opts.min_xlim)
    xmax = 0.05

    # whitened strain
    x = wh_strain.sample_times.numpy()-gps_time
    y = wh_strain
    ax.plot(x, y, colors[ifo], lw=1.5, zorder=1)
    ylim = get_ylim(y, x, xmin, xmax)

    if opts.injection_file:
        # get the injection values
        from pycbc import inject, io
        injf = inject.InjectionSet(opts.injection_file)
        ti = injf.make_strain_from_inj_object(injf.table[0], wh_strain.delta_t, ifo, f_lower=gen.current_params['f_lower'])
        fi = ti.to_frequencyseries(delta_f=gen.current_params['delta_f'])
        if len(fi) < len(psd):
            fi.resize(len(psd))
        elif len(psd) < len(fi):
            fi = fi[:len(psd)]
        fi /= asd
        ti = fi.to_timeseries()
        ax.plot(ti.sample_times.numpy()-gps_time, ti.data, 'b-', lw=2, zorder=2)
    #m, i = match(ti, ts, psd=psd, low_frequency_cutoff=gen.current_params['f_lower'])
    #print "Match between map and injected is %.2f" % m
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ylim)
    ax.text(xmin, ylim[0], 'Match=%.2f' % m, ha='left', va='bottom', fontsize=12)
    ax.set_ylabel('{} whitened strain'.format(ifo))
    if ii == 2:
        ax.set_xlabel('GPS time - {} (s)'.format(gps_time))

    ## Find and save SNR
    snr = matched_filter(ti, y, psd=psd, low_frequency_cutoff=20.0) ## Should be SNR between injected waveform and whitened data
    snr_map=matched_filter(ts, y, psd=psd, low_frequency_cutoff=20.0) ## SNR between MAP waveform and whitened data

fp.close()
fig.savefig(opts.output_file, dpi=200, bbox_inches='tight')
