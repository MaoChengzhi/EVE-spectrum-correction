import numpy as np
from scipy.optimize import fsolve
import pandas as pd
import math
from math import sqrt 
from math import pi
from math import e
from scipy.optimize import root

import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

#%%
test_A=[1,2]
test_central=[3,2]
test_stddev=[1,2]

wave_list=np.linspace(-7,8,200)
df_test = pd.DataFrame({'amplitude': test_A, 'central_wavelength': test_central, 'stddev': test_stddev, })
df_test
#%%
def equations(p,test_A,test_central,test_stddev):
    mu ,sigma= p

    eq1=0 
    eq2=0
    # print(df)
    # for i in range(pixel_num):            
    for i in range(2):
        
        A_i=test_A[i]
        mu_i=test_central[i]
        sigma_i=test_stddev[i] 
        
        exp_i=e**(  -(mu-mu_i)**2/(2*(sigma**2+sigma_i**2))   ) 
        
        eq1=eq1+A_i* exp_i *(1/sqrt(sigma**2+sigma_i**2)-2*((mu-mu_i)**2+sigma**2*sigma_i**2+sigma_i**4)\
                             /(sigma**2+sigma_i**2)**2.5)
        
        
        eq2=eq2+A_i   *        (mu_i-mu)   *     exp_i \
                /(   (sigma_i**2+sigma**2)**(3/2)  )  # right
          
    print(eq1,eq2)
   
    return [eq1, eq2]

#%%
sol = fsolve(equations,x0=(2.34,1.8),args=(test_A,test_central,test_stddev))
num=2
c=[]
wave_list=np.linspace(-7,8,2000)
for i in range(num):
    c.append(models.Gaussian1D(amplitude=test_A[i], mean=test_central[i], stddev=test_stddev[i]))
    
total=np.zeros_like(c[0](wave_list))

for i in range(num):
    total+=c[i](wave_list)
    
c_init=models.Gaussian1D(amplitude=5, mean=1, stddev=1)
fit_c = fitting.LevMarLSQFitter()
c_fitted=fit_c(c_init,wave_list,total)
c_fitted


fig, ax = plt.subplots()
    
for i in range(num):
    ax.plot(wave_list,c[i](wave_list),label=str(i))
    
ax.plot(wave_list,total,label="sum up")
ax.plot(wave_list,c_fitted(wave_list),label="fit")
# ax.plot(wave_list,models.Gaussian1D(amplitude=A, mean=mu, stddev=sigma)(wave_list),label="mine")

ax.legend()
c_fitted
#%%

# fig, ax = plt.subplots()
num=50
S =np.linspace(1.5,2.,num)
M=np.linspace(2.,2.6,num)
error=np.zeros((num,num))
point=np.zeros((num,num,2))
for i in range(len(S)):
    for j in range(len(M)):
        error[i,j]=sum((models.Gaussian1D(amplitude=2.73541282, mean=M[j], stddev=S[i])(wave_list)-total)**2)
        point[i,j]=[S[i],M[j]]
            
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.scatter3D(point[:,:,0],point[:,:,1],error,zdir='z')
ax.set_xlabel('S')
ax.set_ylabel('central_wave')