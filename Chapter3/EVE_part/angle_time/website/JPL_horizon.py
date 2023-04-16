import pandas as pd

filename = 'horizon_data.txt'

# load data into DataFrame
df = pd.read_csv(filename, names=['JDTDB', 'Calendar Date (TDB)', 'EC', 'QR',
                 'IN', 'OM', 'W', 'Tp', 'N', 'MA', 'TA', 'A', 'AD', 'PR'],  engine='python')

# print the DataFrame
print(df)
# %%

filename = 'horizon_data.txt'

# Read the data into a pandas dataframe
df = pd.read_csv(filename, delimiter=',\s+', header=None,
                 names=['JDTDB', 'Calendar Date (TDB)', 'EC', 'QR', 'IN',
                        'OM', 'W', 'Tp', 'N', 'MA', 'TA', 'A', 'AD', 'PR'],
                 index_col='Calendar Date (TDB)')

# Print the dataframe
print(df)

# %%

filename = 'horizon_data.txt'

# read the data into a dataframe, skip the first row and set the index column
df = pd.read_csv(filename, delimiter=',\s+',
                 names=['Date (TDB)', 'Orbital Eccentricity (EC)', 'Perihelion Distance (QR)', 'Inclination (IN)', 'Longitude of Ascending Node (OM)',
                        'Argument of Perihelion (W)', 'Time of Perihelion Passage (Tp)', 'Mean Anomaly (MA)', 'True Anomaly (TA)', 'Semi-Major Axis (A)',
                        'Apohelion Distance (AD)', 'Orbital Period (PR)'])
