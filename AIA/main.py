# This file aims to get DN.npz which contains all data during a cruciform scan
import numpy as np
import math
import time
from calculating_DN import calculating_DN

#%%
start=time.time()

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

for i in range(angle_point_num_alpha):
    DN_alpha[i]=calculating_DN(wavelength_list,offaxis_angle_x_alpha[i],
                                          offaxis_angle_y_alpha[i])

for j in range(angle_point_num_beta):
    DN_beta[j]=calculating_DN(wavelength_list,offaxis_angle_x_beta[j],
                                          offaxis_angle_y_beta[j])
    
    
np.savez("DN.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)


end=time.time() 
totol_time=end-start
print(totol_time)








