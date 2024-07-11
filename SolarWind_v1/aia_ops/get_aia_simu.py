import glob
import sunpy.map
import numpy as np
import pandas as pd
from .calculate_DN import calculate_DN_cp
# relative import, use a dot to indicate the current package
# from aia_ops.calculate_DN import calculate_DN_cp        also works
import datetime
import time
import cupy as cp
import os


from .gaussian_fit_aia import gaussian_fit_aia

# %%
# module_dir = os.path.dirname(os.path.abspath(__file__))
# data_dir = os.path.join(module_dir, 'data', 'AIA')

# aia_adjusted_files = sorted(glob.glob(os.path.join(data_dir, '*adjusted.fits')))

# if not aia_adjusted_files:
#     raise ValueError(
#         "No files found with the pattern 'data/AIA/*adjusted.fits'")


# aia_adjusted_maps = sunpy.map.Map(aia_adjusted_files)
# irradiance = cp.zeros((len(aia_adjusted_maps), len(wavelength_list_aia)))
# wavelength_correction = cp.zeros(len(aia_adjusted_maps))
# %%


def get_aia_simu(coeff,selected_aia_df,wavelength_list_aia):
    
    '''
    
    a * Tx**2 + b * Tx + c*Ty**2 + d * Ty+e
    
    '''
    # work out wavelength_correction
    # for i in range(len(aia_adjusted_maps)):
    #     irradiance[i] = calculate_DN_5(aia_adjusted_maps[i],a,b,c,d,e)
    #     wavelength_correction[i] = gaussian_fit_aia(wavelength_list_aia,
    #                                                 irradiance[i].get())

    irradiance_list=[]

    for i in selected_aia_df.index:
        irradiance = calculate_DN_cp(selected_aia_df.loc[i,'image'],wavelength_list_aia,coeff)# irradiance is actually a np.array itself

        irradiance_list.append(irradiance)

    # create a new dataframe of only two col: date and aia_simu
    aia_simu_df=pd.DataFrame()
    aia_simu_df['date']=selected_aia_df['date']
    aia_simu_df['aia_simu']=irradiance_list

    return aia_simu_df

    # # work out time_list
    # time_list = []
    # for aia_adjusted_map in aia_adjusted_maps:
    #     dt = datetime.datetime.strptime(aia_adjusted_map.meta['t_obs'],
    #                            '%Y-%m-%dT%H:%M:%S.%fZ')

    #     time_list.append(datetime.datetime.combine(dt.date(), datetime.time.min))

    # # Combine time_list and wavelength_correction
    # aia_simu = dict(zip(time_list, wavelength_correction.get()))

    


