import astropy.units as u
from sunpy.net import Fido, attrs as a
import glob
import sunpy.map
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

# %%
aia_files = sorted(glob.glob('data/AIA/*image_lev1.fits'))
m_aia = sunpy.map.Map(aia_files)
# %%
# Tx_list,Ty_list
Tx_list = []
Ty_list = []
for aia_map in m_aia:
    Tx_list.append(aia_map.center.Tx.value)
    Ty_list.append(aia_map.center.Ty.value)

# regular expression
strings = aia_files

time_pattern = r'\d{2}_\d{2}_\d{2}_\d{2}'
time = []  # hh_mm_ss_ms     ms: 231 ms -> 23
for string in strings:
    match = re.search(time_pattern, string)
    if match:
        # print(match.group(0))
        time.append(match.group(0))

data = {
    "alpha_list": Tx_list,
    "beta_list": Ty_list,
    "time": time
}
frame = pd.DataFrame(data)

# %%
