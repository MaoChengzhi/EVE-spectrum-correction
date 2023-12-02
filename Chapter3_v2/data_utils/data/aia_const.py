import numpy as np
import cupy as cp

# SDO/AIA response to coronal hole, quiet Sun, active region and flare plasma
#这个绝对量其实不重要
wavelength_chianti = 30.3783

#AIA模拟计算只用这个
wavelength_list_aia_relative_Single_A = np.linspace(start=30.27,stop=30.57,num=16)    - wavelength_chianti

wavelength_list_aia_absolute = np.linspace(start=30.27,stop=30.57,num=16)