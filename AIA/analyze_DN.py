#This file aims to draw conclusion from DN.npz
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import math

DN=np.load("DN.npz")

#Initialize
wavelength_point_num=15
wavelength_list=np.linspace(-0.1,0.15,wavelength_point_num)

#Cruciformscan in alpha direction
angle_point_num_alpha=61
DN_alpha=np.zeros((angle_point_num_alpha,wavelength_point_num))
offaxis_angle_x_alpha=np.linspace(-math.pi/360,math.pi/360,angle_point_num_alpha)
offaxis_angle_y_alpha=np.zeros(angle_point_num_alpha)

#Cruciformscan in beta direction
angle_point_num_beta=61   
DN_beta=np.zeros((angle_point_num_beta,wavelength_point_num))
offaxis_angle_x_beta=np.zeros(angle_point_num_beta)
offaxis_angle_y_beta=np.linspace(-math.pi/360,math.pi/360,angle_point_num_beta)

#%%
# Offaxis angle during cruciformscan
fig = plt.figure()
ax=fig.add_subplot()
ax.plot(range(angle_point_num_alpha),offaxis_angle_x_alpha)

ax.plot(range(angle_point_num_alpha),offaxis_angle_y_alpha)
ax.legend(["alpha","beta"])

# fig, ax = plt.subplots()
# ax.plot(range(angle_point_num_beta),offaxis_angle_x_beta)
# ax.plot(range(angle_point_num_beta),offaxis_angle_y_beta)
#%%
# Profiles during cruciformscan
fig, ax = plt.subplots()
# Profiles during cruciformscan in alpha direction
for i in range(angle_point_num_alpha):
    ax.plot(wavelength_list, DN['DN_alpha'][i], label='linear') 
     
# Profiles during cruciformscan in beta direction
fig, ax = plt.subplots()
for j in range(angle_point_num_beta):
    ax.plot(wavelength_list, DN['DN_beta'][j], label='linear') 

#%%
# Fit data in DN
wavelength_shift_alpha=np.zeros(angle_point_num_alpha)
fit_alpha=[]
for i in range(angle_point_num_alpha):
    g_init = models.Gaussian1D(amplitude=3E9, mean=0.05, stddev=0.0424) 
    #initial value for fitting
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g( g_init  , wavelength_list, DN['DN_alpha'][i])
    wavelength_shift_alpha[i]=g.mean.value
    fit_alpha.append(g)


wavelength_shift_beta=np.zeros(angle_point_num_beta)
fit_beta=[]
for j in range(angle_point_num_beta):
    g_init = models.Gaussian1D(amplitude=3E9, mean=0.05, stddev=0.0424)
    #initial value for fitting
    fit_g = fitting.LevMarLSQFitter()
    g = fit_g( g_init  , wavelength_list, DN['DN_beta'][j])
    wavelength_shift_beta[j]=g.mean.value
    fit_beta.append(g)

#%%
# Central wavelength shift 
fig,ax = plt.subplots()
ax.plot(offaxis_angle_x_alpha,wavelength_shift_alpha)

fig, ax = plt.subplots()
ax.plot(offaxis_angle_y_beta,wavelength_shift_beta)
#%%
# Central wavelength shift 
fig, ax = plt.subplots()
ax.plot(offaxis_angle_x_alpha,wavelength_shift_alpha-\
         wavelength_shift_alpha[int(angle_point_num_alpha/2)])
ax.set_ylabel('Wavelength shift (nm)')
ax.set_xlabel("Alpha Offset (rad)")

fig, ax = plt.subplots()
ax.plot(offaxis_angle_y_beta,wavelength_shift_beta-\
         wavelength_shift_beta[int(angle_point_num_beta/2)])
ax.set_ylabel('Wavelength shift (nm)')
ax.set_xlabel("Beta Offset (rad)")
#%%
# Fitted profiles during cruciformscan
fig, ax = plt.subplots()
wavelength_densed_list=np.linspace(-0.1,0.15,10*wavelength_point_num)
# Profiles during cruciformscan in alpha direction
for i in range(angle_point_num_alpha):
    ax.plot(wavelength_densed_list, fit_alpha[i](wavelength_densed_list), label='linear') 

ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel("Digital Number per nm (?)")     
# Profiles during cruciformscan in beta direction
fig, ax = plt.subplots()
for j in range(angle_point_num_beta):
    ax.plot(wavelength_densed_list, fit_beta[j](wavelength_densed_list), label='linear')
    
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel("Digital Number per nm (?)")  