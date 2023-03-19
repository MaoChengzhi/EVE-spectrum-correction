import numpy as np
import time
from multiprocessing import Pool

# from calculating_DN_2048 import calculate_DN_alpha, calculate_DN_beta
# from calculating_DN_2048 import angle_point_num_alpha, angle_point_num_beta
from calculating_DN_4096 import calculate_DN_alpha, calculate_DN_beta
from calculating_DN_4096 import angle_point_num_alpha, angle_point_num_beta

# %%
start = time.time()
with Pool(processes=13) as p:  # CPU on my laptop with 14 cores
    DN_alpha = np.array(
        p.map(calculate_DN_alpha, range(angle_point_num_alpha)))
    DN_beta = np.array(
        p.map(calculate_DN_beta, range(angle_point_num_beta)))

# np.savez("DN_alpha_2048.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)

np.savez("output_DN/_4096/DN__4096.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)
end = time.time()
totol_time = end - start
print(totol_time)

# Process=12, run for 1h on Feb 14th    4096
# March 8 th    2048  10min
