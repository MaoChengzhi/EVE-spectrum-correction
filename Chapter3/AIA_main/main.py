import numpy as np
import time
from multiprocessing import Pool
import multiprocessing
from calculating_DN_2048 import calculate_DN_alpha, calculate_DN_beta
from calculating_DN_2048 import angle_point_num_alpha, angle_point_num_beta, wavelength_point_num
# from calculating_DN_4096 import calculate_DN_alpha, calculate_DN_beta
# from calculating_DN_4096 import angle_point_num_alpha, angle_point_num_beta, wavelength_point_num

# =============================================================================
# # %%
# if __name__ == '__main__':
#     start = time.time()
#
#     with Pool(processes=12) as p:  # CPU on my laptop with 14 cores
#         DN_alpha = np.array(
#             p.map(calculate_DN_alpha, range(angle_point_num_alpha)))
#         DN_beta = np.array(
#             p.map(calculate_DN_beta, range(angle_point_num_beta)))
#
#     np.savez("output_DN/_2048/vector_test",
#              DN_alpha=DN_alpha, DN_beta=DN_beta)
#     end = time.time()
#     totol_time = end - start
#     print(totol_time)
#     # np.savez("DN_alpha_2048.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)
# =============================================================================

# %%
start = time.time()
DN_alpha = np.zeros((angle_point_num_alpha, wavelength_point_num))

for i in range(angle_point_num_alpha):
    DN_alpha[i] = calculate_DN_alpha(i)

DN_beta = np.zeros((angle_point_num_beta, wavelength_point_num))
for i in range(angle_point_num_beta):
    DN_beta[i] = calculate_DN_beta(i)

np.savez("output_DN/_2048/disk",
         DN_alpha=DN_alpha, DN_beta=DN_beta)

end = time.time()
totol_time = end - start
print(totol_time)
