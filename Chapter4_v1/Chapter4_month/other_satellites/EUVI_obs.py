import matplotlib.pyplot as plt
import glob
from datetime import datetime

import numpy as np

import astropy.units as u
from astropy.coordinates import SkyCoord

from my_reproject import reproject_to_aia, plot_reproject
import sunpy.map
# %%
out_shape = (2048, 2048)
aia_path = 'data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits'
map_aia = sunpy.map.Map(aia_path)
map_aia = map_aia.resample(out_shape * u.pix)
# %%
stereo_files = sorted(glob.glob('data/SECCHI/201101*.fts'))
maps = sunpy.map.Map(stereo_files)
maps_stereo_a = [m for m in maps if m.meta['obsrvtry'] == 'STEREO_A']
maps_stereo_b = [m for m in maps if m.meta['obsrvtry'] == 'STEREO_B']
# %%
date_obs_a = []
for m in maps_stereo_a:
    date_obs_a.append(
        datetime.strptime(m.meta['date-obs'], '%Y-%m-%dT%H:%M:%S.%f').minute)

date_obs_b = []
for m in maps_stereo_b:
    date_obs_b.append(
        datetime.strptime(m.meta['date-obs'], '%Y-%m-%dT%H:%M:%S.%f').minute)
# %% time-consuming
irradiance_a = np.zeros(len(maps_stereo_a))
outmap_a = []
for i in range(len(maps_stereo_a)):
    outmap = reproject_to_aia(map_aia, maps_stereo_a[i], out_shape)
    outmap_a.append(outmap)
    irradiance_a[i] = np.nansum(outmap.data)

outmap_b = []
irradiance_b = np.zeros(len(maps_stereo_b))
for i in range(len(maps_stereo_b)):
    outmap = reproject_to_aia(map_aia, maps_stereo_b[i], out_shape)
    outmap_b.append(outmap)
    irradiance_b[i] = np.nansum(outmap.data)

# %%
fig, ax = plt.subplots()
ax.scatter(date_obs_a, irradiance_a, c='r', label='STEREO A')

ax.scatter(date_obs_b, irradiance_b, c='g', label='STEREO B')
ax.legend()
# %%
fig = plt.figure()
ax = fig.add_subplot(121, projection=map_aia)
outmap_a[0].plot(axes=ax, title='EUVI image as seen from SDO')
ax = fig.add_subplot(122, projection=map_aia)
outmap_a[1].plot(axes=ax, title='EUVI image as seen from SDO')

# %%
fig, axs = plt.subplots(4, 6, figsize=(
    12, 12), subplot_kw={'projection': map_aia})

# Plot the SunPy maps on each subplot
for i in range(22):
    row = i // 6
    col = i % 6
    ax = axs[row, col]
    outmap_a[i].plot(axes=ax, title="16:"+str(date_obs_a[i]))
    ax.set_xticks([])
    ax.set_yticks([])


fig, axs = plt.subplots(2, 3, figsize=(
    12, 12), subplot_kw={'projection': map_aia})
# Plot the SunPy maps on each subplot
for i in range(6):
    row = i // 3
    col = i % 3
    ax = axs[row, col]
    outmap_b[i].plot(axes=ax, title="16:"+str(date_obs_b[i]))
    ax.set_xticks([])
    ax.set_yticks([])
# %%  sloar disk visualization
map_euvi = maps_stereo_a[0]
fig = plt.figure()

ax1 = fig.add_subplot(121, projection=map_aia)
map_aia.plot(axes=ax1)
map_aia.draw_limb(axes=ax1, color='white')
map_euvi.draw_limb(axes=ax1, color='red')

ax2 = fig.add_subplot(122, projection=map_euvi)
map_euvi.plot(axes=ax2)
limb_aia = map_aia.draw_limb(axes=ax2, color='white')
limb_euvi = map_euvi.draw_limb(axes=ax2, color='red')

plt.legend([limb_aia[0], limb_euvi[0]],
           ['Limb as seen by AIA', 'Limb as seen by EUVI A'])

# %% irradiance visualization
fig,ax = plt.subplots()
ax.scatter(date_obs_a,irradiance_a,label="STEREO A")

ax.scatter(date_obs_b,irradiance_b,label="STEREO B")
ax.set_xlabel("time (min) since 16:00")
ax.set_ylim(0,)
ax.legend()