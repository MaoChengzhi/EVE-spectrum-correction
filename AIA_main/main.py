import numpy as np
import time
from multiprocessing import Pool

from calculating_DN_2048 import calculate_DN_alpha, calculate_DN_beta
from calculating_DN_2048 import angle_point_num_alpha, angle_point_num_beta
# from calculating_DN_4096 import calculate_DN_alpha, calculate_DN_beta
# from calculating_DN_4096 import angle_point_num_alpha, angle_point_num_beta

# %%
start = time.time()
with Pool(processes=12) as p:  # CPU on my laptop with 14 cores
    DN_alpha = np.array(
        p.map(calculate_DN_alpha, range(angle_point_num_alpha)))
    DN_beta = np.array(
        p.map(calculate_DN_beta, range(angle_point_num_beta)))

np.savez("output_DN/_2048/DN_2048_normalized",
         DN_alpha=DN_alpha, DN_beta=DN_beta)
end = time.time()
totol_time = end - start
print(totol_time)
# np.savez("DN_alpha_2048.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)
