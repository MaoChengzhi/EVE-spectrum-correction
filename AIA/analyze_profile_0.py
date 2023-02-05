import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math

irradiance=np.load("irradiance.npz")

#Initialize
wavelength_point_num=15
wavelength_list=np.linspace(-0.1,0.15,wavelength_point_num)

#Cruciformscan in alpha direction
angle_point_num_alpha=61
irradiance_alpha=np.zeros((angle_point_num_alpha,wavelength_point_num))
offaxis_angle_x_alpha=np.linspace(-math.pi/360,math.pi/360,angle_point_num_alpha)
offaxis_angle_y_alpha=np.zeros(angle_point_num_alpha)

#Cruciformscan in beta direction
angle_point_num_beta=61   
irradiance_beta=np.zeros((angle_point_num_beta,wavelength_point_num))
offaxis_angle_x_beta=np.zeros(angle_point_num_beta)
offaxis_angle_y_beta=np.linspace(-math.pi/360,math.pi/360,angle_point_num_beta)
irradiance_beta=np.zeros((angle_point_num_beta,wavelength_point_num))

#%%
fig, ax = plt.subplots()
for i in range(angle_point_num_alpha):
    
    ax.plot(wavelength_list, irradiance['irradiance_alpha'][i], label='linear') 
     

fig, ax = plt.subplots()
for j in range(angle_point_num_alpha):
    
    ax.plot(wavelength_list, irradiance['irradiance_beta'][j], label='linear') 


#%%
wavelength_shift_alpha=np.zeros(angle_point_num_alpha)
for i in range(angle_point_num_alpha):
    g_init = models.Gaussian1D(amplitude=3E9, mean=0.05, stddev=0.0424)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g( g_init  , wavelength_list, irradiance['irradiance_alpha'][i])
    wavelength_shift_alpha[i]=g.mean.value

wavelength_shift_beta=np.zeros(angle_point_num_beta)
for j in range(angle_point_num_beta):
    g_init = models.Gaussian1D(amplitude=3E9, mean=0.05, stddev=0.0424)
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g( g_init  , wavelength_list, irradiance['irradiance_beta'][j])
    wavelength_shift_beta[j]=g.mean.value


#%%

plt.plot(offaxis_angle_x_alpha,wavelength_shift_alpha)
plt.plot(offaxis_angle_y_beta,wavelength_shift_beta)
#%%
plt.plot(offaxis_angle_x_alpha,wavelength_shift_alpha-\
         wavelength_shift_alpha[int(angle_point_num_alpha/2)])
plt.plot(offaxis_angle_y_beta,wavelength_shift_beta-\
         wavelength_shift_beta[int(angle_point_num_beta/2)])

#%%
#check fitting
fig, ax = plt.subplots()
wavelength_list_simulation=np.linspace(-0.1,0.15,10*wavelength_point_num)
ax.plot(wavelength_list_simulation, g(wavelength_list_simulation), label='linear') 
# ax.plot(wavelength_list, irradiance['irradiance_alpha'][0], label='linear') 
