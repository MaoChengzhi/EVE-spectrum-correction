import numpy as np
import time
from multiprocessing import Pool
from functools import partial

from calculating_DN_2048 import calculate_DN_alpha
from calculating_DN_2048 import angle_point_num_alpha


from astropy.constants import au, R_sun
# %%
a_num = 16

transunit = ((au/R_sun).value)**2 / 1000
a_list = np.linspace(20.5*transunit, 20.65*transunit, a_num)
DN_alpha_list = []

# %%
start = time.time()
for a in a_list:
    with Pool(processes=13) as p:  # 14 CPUs on my laptop.
        DN_alpha_list.append(
            p.map(partial(calculate_DN_alpha, a), range(angle_point_num_alpha)))

np.savez("output_DN/DN_my_range_2048.npz",
         DN_alpha_list=DN_alpha_list, a_list=a_list)


# %%
a_num = 17

transunit = ((au/R_sun).value)**2 / 1000
a_list = np.linspace(18.5*transunit, 18.82*transunit, a_num)
DN_alpha_list = []

# %%
for a in a_list:
    with Pool(processes=13) as p:  # 14 CPUs on my laptop.
        DN_alpha_list.append(
            p.map(partial(calculate_DN_alpha, a), range(angle_point_num_alpha)))

np.savez("output_DN/DN_his_range_2048.npz",
         DN_alpha_list=DN_alpha_list, a_list=a_list)

end = time.time()
totol_time = end - start
print(totol_time)
