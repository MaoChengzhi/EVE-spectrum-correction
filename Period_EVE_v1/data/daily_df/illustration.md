These files have delete the data during solar eclipse



~~~
    fit_df['amplitude']=np.where(fit_df['eclipse_flag'].values==0,fit_df['amplitude'].values,np.nan)
    fit_df['mean']=np.where(fit_df['eclipse_flag'].values==0,fit_df['mean'].values,np.nan)
    fit_df['stddev']=np.where(fit_df['eclipse_flag'].values==0,fit_df['stddev'].values,np.nan)
~~~

