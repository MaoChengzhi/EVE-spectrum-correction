import numpy as np
import time
from multiprocessing import Pool

from calculating_DN import calculate_DN_alpha, calculate_DN_beta
from calculating_DN import angle_point_num_alpha, angle_point_num_beta

# %%
start = time.time()
with Pool(processes=12) as p:  # 14 CPUs on my laptop.
    DN_alpha = np.array(
        p.map(calculate_DN_alpha, range(angle_point_num_alpha)))
    DN_beta = np.array(
        p.map(calculate_DN_beta, range(angle_point_num_beta)))

np.savez("DN_above0_fulldisk.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)

end = time.time()
totol_time = end - start
print(totol_time)

# Process=8, run for 7971s  2.2h on Feb 14th
