import numpy as np
import matplotlib.pyplot as plt
import math
import time
from calculating_irradiance import calculating_irradiance

#%%
start=time.time()

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

for i in range(angle_point_num_alpha):
    irradiance_alpha[i]=calculating_irradiance(wavelength_list,offaxis_angle_x_alpha[i],
                                          offaxis_angle_y_alpha[i])

for j in range(angle_point_num_beta):
    irradiance_beta[j]=calculating_irradiance(wavelength_list,offaxis_angle_x_beta[j],
                                          offaxis_angle_y_beta[j])
    
    
np.savez("irradiance.npz",irradiance_alpha=irradiance_alpha,
          irradiance_beta=irradiance_beta)


end=time.time() 
totol_time=end-start
print(totol_time)


#%%
wavelength_point_num=15
wavelength_list=np.linspace(-0.1,0.15,wavelength_point_num)
irradiance_alpha=calculating_irradiance(wavelength_list,0,
                                      0)





