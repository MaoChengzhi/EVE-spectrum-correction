import numpy as np
import time
from multiprocessing import Pool
from functools import partial

from calculating_DN import calculate_DN_alpha
from calculating_DN import angle_point_num_alpha

from iteration import iteration
# %%
start = time.time()
a = [909.2]
new_a = 909.2
for i in range(4):
    with Pool(processes=12) as p:  # 14 CPUs on my laptop.
        DN_alpha = np.array(
            p.map(partial(calculate_DN_alpha, new_a), range(angle_point_num_alpha)))
        new_a = iteration(DN_alpha)
        a.append(new_a)
# np.savez("DN_above0_fulldisk.npz", DN_alpha=DN_alpha, DN_beta=DN_beta)

end = time.time()
totol_time = end - start
print(totol_time)
print(a)
# Process=8, run for 7971s  2.2h on Feb 14th
# %%
np.savez("iteration.npz", iteration=a)
