# %%     std_pixel_to_world            VS          my_pixel_to_world
from std_pixel_to_world import std_pixel_to_world
from my_pixel_to_world import my_pixel_to_world
import random
import math
import matplotlib.pyplot as plt
import numpy as np


# %%
test_num = 100
std_Tx, std_Ty, my_Tx, my_Ty = np.zeros((test_num,)), np.zeros(
    (test_num,)), np.zeros((test_num,)), np.zeros((test_num,))
pixel_x, pixel_y = np.zeros((test_num,)), np.zeros((test_num,))
error = 0
for i in range(test_num):
    pixel_x[i] = random.randrange(0, 4096)
    pixel_y[i] = random.randrange(0, 4096)
    std_Tx[i], std_Ty[i] = std_pixel_to_world(pixel_x[i], pixel_y[i])
    my_Tx[i], my_Ty[i] = my_pixel_to_world(pixel_x[i], pixel_y[i])
    # print(abs(1-my_Tx/std_Tx), abs(1-my_Ty/std_Ty))
    if max(abs(1-my_Tx[i]/std_Tx[i]), abs(1-my_Ty[i]/std_Ty[i])) > error:
        error = max(abs(1-my_Tx[i]/std_Tx[i]), abs(1-my_Ty[i]/std_Ty[i]))
print(error)


# %%
fig1 = plt.figure()
ax1 = plt.axes(projection='3d')
ax1.scatter(pixel_x, pixel_y, std_Tx, color="red", marker='o', s=100)
ax1.scatter(pixel_x, pixel_y, my_Tx, color="blue", marker='+', s=500)

fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.scatter(pixel_x, pixel_y, std_Ty, color="red", marker='o', s=100)
ax2.scatter(pixel_x, pixel_y, my_Ty, color="blue", marker='+', s=500)
