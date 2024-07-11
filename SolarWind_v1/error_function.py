import pandas as pd
import datetime
from aia_ops.get_aia_simu import get_aia_simu
from aia_ops.gaussian_fit_aia import gaussian_fit_aia
import os
import matplotlib.pyplot as plt
import numpy as np


def error_function(coeff,selected_aia_df,wavelength_list_aia,aia_initial_guess,accurate_wavelength, selected_eve_df):
    '''
    
    input coeff,temp_aia_df
    '''
    

    aia_simu_df=get_aia_simu(coeff,selected_aia_df,wavelength_list_aia)

    for i in aia_simu_df.index:
        popt, pcov=gaussian_fit_aia(wavelength_list_aia,aia_simu_df.loc[i,'aia_simu'],aia_initial_guess)

        aia_simu_df.loc[i,'simu_mean']=popt[1]+accurate_wavelength


    combined_df=pd.merge(aia_simu_df,selected_eve_df,how='left',on='date')


    combined_df['error']=combined_df['simu_mean']-combined_df['median_of_mean']

    # I naturally take the square of the deviation as the error. I know an absolute error is also possible.
    error=(combined_df['error']**2).sum()

    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(combined_df['date'],combined_df['line_center'],label='AIA Simulation: line_center',color='C0')
    ax.plot(combined_df['date'],combined_df['median_of_mean'],label='EVE observation: median_of_mean',color='C1')
    ax.hlines(accurate_wavelength,combined_df['date'].iloc[0],combined_df['date'].iloc[-1],
                        label='accurate_wavelength',linestyles='dashed',color='C2')

    ax.legend()
    ax.set_xlabel('date')
    ax.set_ylabel('line center (nm)')
    ax.set_title('a='+str(coeff[0])+' b='+str(coeff[1])+' c='+str(coeff[2])+' d='+str(coeff[3])+' e='+str(coeff[4])+' error='+str(error))

    filename='a='+str(coeff[0])+'_b='+str(coeff[1])+'_c='+str(coeff[2])+'_d='+str(coeff[3])+'_e='+str(coeff[4])+'.png'
    # save the figure, by joining the filename with the path
    fig.savefig(os.path.join('output','parameter_trial',filename))
    plt.close(fig)



            
    return error



    
def get_df_to_plot(coeff,selected_aia_df,wavelength_list_aia,aia_initial_guess,accurate_wavelength, selected_eve_df):
    '''
    
    input coeff,temp_aia_df
    '''
    

    aia_simu_df=get_aia_simu(coeff,selected_aia_df,wavelength_list_aia)

    for i in aia_simu_df.index:
        popt, pcov=gaussian_fit_aia(wavelength_list_aia,aia_simu_df.loc[i,'aia_simu'],aia_initial_guess)

        aia_simu_df.loc[i,'simu_amplitude']=popt[0]
        aia_simu_df.loc[i,'simu_mean']=popt[1]+accurate_wavelength
        aia_simu_df.loc[i,'simu_stddev']=popt[2]


    combined_df=pd.merge(aia_simu_df,selected_eve_df,how='left',on='date')


    # combined_df['error']=combined_df['simu_mean']-combined_df['median_of_mean']

    

            
    return combined_df