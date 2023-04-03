import numpy as np
import time
from multiprocessing import Pool
from functools import partial
import math

from calculating_DN_2048 import calculate_DN_alpha
from calculating_DN_2048 import angle_point_num_alpha


# %%
a_num = 26

transunit = (180*3600/(974.634085*math.pi))**2 / 1000
a_list = np.linspace(0*transunit, 50*transunit, a_num)
DN_alpha_list = []

# %%
if __name__ == '__main__':
    start = time.time()
    for a in a_list:
        with Pool(processes=10) as p:  # 14 CPUs on my laptop.
            DN_alpha_list.append(
                p.map(partial(calculate_DN_alpha, a), range(angle_point_num_alpha)))

    np.savez("output_DN/DN_2048_0to50.npz",
             DN_alpha_list=DN_alpha_list, a_list=a_list)
