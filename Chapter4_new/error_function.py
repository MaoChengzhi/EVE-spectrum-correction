import json
from get_aia_simu import get_aia_simu
# %%

with open('mean_dict.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    eve_data = json.load(f)

eve_obs = {}
for key, value in eve_data.items():
    eve_obs[int(key)] = float(value)


def error_function(x):

    a, b, c, d, e = x
    error = 0
    aia_simu = get_aia_simu(a, b, c, d, e)
    for key in aia_simu.keys():
        if key in eve_obs.keys():
            error += (aia_simu[key]-eve_obs[key])**2

    return error
