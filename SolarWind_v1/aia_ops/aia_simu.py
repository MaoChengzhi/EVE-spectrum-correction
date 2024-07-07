from .calculating_DN import calculating_DN
from .gaussian_fit_aia import gaussian_fit_aia
from .data.aia_const import wavelength_list_aia_relative, wavelength_list_aia_absolute

import numpy as np
import cupy as cp
import os
import pandas as pd
import importlib


import aia_ops
importlib.reload(aia_ops.calculating_DN)

def get_aia_simu(aia_df,t0,t1):
    #%%
    # Get the path of the current Python file
    current_py_file = os.path.abspath(__file__)
    #load in "D:\py_repo\EVE-spectrum-correction\Chapter4_v2\basic_ops\aia_ops\data\aia.pkl" load in file every time????
    aia_pkl = pd.read_pickle(os.path.join(os.path.dirname(current_py_file), 'data/aia.pkl'))

    time_list = []
    amplitude_list =[]
    mean_list = []
    stddev_list = []

    df=aia_df[(aia_df['time']>=t0)&(aia_df['time']<=t1)]
    for i in range(len(df)):
        time=df.iloc[i]['time'].date()

        irradiance=aia_ops.calculating_DN.calculating_DN(df.iloc[i]['image'],wavelength_list_aia_relative)
        amplitude,mean,stddev=gaussian_fit_aia(wavelength_list_aia_absolute,irradiance)
    
        time_list.append(time)
        amplitude_list.append(amplitude)
        mean_list.append(mean)
        stddev_list.append(stddev)


    # the output df with col time, amplitude ,mean, stddev
    output_df={
        'time':time_list,
        'amplitude':amplitude_list,
        'mean':mean_list,
        'stddev':stddev_list
    }
    output_df=pd.DataFrame(output_df)

    return output_df



