import numpy as np
import cupy as cp

# SDO/AIA response to coronal hole, quiet Sun, active region and flare plasma
#这个绝对量其实不重要
wavelength_chianti = 30.3783

#AIA模拟计算只用这个
wavelength_list_aia_relative_Single_A = np.array([30.27, 30.29, 30.31, 30.33, 30.35, 30.37,
                                30.39, 30.41, 30.43, 30.45, 30.47, 30.49])\
    - wavelength_chianti

wavelength_list_aia_absolute = np.array([30.27, 30.29, 30.31, 30.33, 30.35, 30.37,
                                30.39, 30.41, 30.43, 30.45, 30.47, 30.49])