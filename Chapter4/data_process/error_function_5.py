import pandas as pd
import datetime
from .aia_part.get_aia_simu_5 import get_aia_simu_5
import os

def error_function_5(temp_array):
    a,b,c,d,e=temp_array
    #%%
    module_dir = os.path.dirname(os.path.abspath(__file__))
    eve_file=os.path.join(module_dir,'eve_part','data','daily_date.csv')
    
    eve_frame=pd.read_csv(eve_file)
    
    date=[]
    for i in eve_frame['date']:
        date.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
        
    eve_frame['date']=date
    eve_frame=eve_frame.set_index('date')
    
    #%%
    temp=get_aia_simu_5(a,b,c,d,e)
    
    aia_simu_data={
                   'date':list(temp.keys()),
                   'daily_mean':list(temp.values()),
                    }
    
    aia_frame=pd.DataFrame(aia_simu_data)
    aia_frame=aia_frame.set_index('date')
    #%%
    
    error=0
    for index in aia_frame.index:
        if index in eve_frame.index:
            error+=(aia_frame.loc[index]['daily_mean']-
                    eve_frame.loc[index]['daily_mean']+ 30.3781)**2
            

    return error
