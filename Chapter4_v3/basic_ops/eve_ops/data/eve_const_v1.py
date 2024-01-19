import numpy as np

#EVE Level 2 的取点
wavelength_full=np.load('./data/wavelength_full.npz')['wavelength_full']




# Fe93 absolutely unapplicable
# Fe131 unapplicable
# Fe171
index1=np.where((wavelength_full<=17.21)*(wavelength_full>17))[0]
#Fe180
index2=np.where((wavelength_full<=18.15)*(wavelength_full>=17.95))[0]
# Fe195 
index3=np.where((wavelength_full<=19.59)*(wavelength_full>=19.43))[0]
# Fe284
index4=np.where((wavelength_full<=28.53)*(wavelength_full>=28.31))[0]
# He 304
index5=np.where((wavelength_full<=30.49)*(wavelength_full>=30.25))[0]
# Fe335 absolutely unapplicable


# O 6297
index6=np.where((wavelength_full<=63.09)*(wavelength_full>=62.85))[0]
# O 9770
index7=np.where((wavelength_full<=97.85)*(wavelength_full>=97.57))[0]
# O 1032
index8=np.where((wavelength_full<=103.35)*(wavelength_full>=103.05))[0]




# Constants
line_name=['Fe171', 'Fe180', 'Fe195', 'Fe284', 'He304','O630', 'O977', 'O1032']
line_window=[index1,index2,index3,index4,index5,index6,index7,index8]


# Initial guess for the parameters [amplitude, mean, stddev] of each band
# Fe171
initial_guess1=[0.0006, 17.11, 0.0424]
#Fe180
initial_guess2=[0.0006, 18.05, 0.0424]
# Fe195
initial_guess3=[0.0006, 19.51, 0.0424]
# Fe284
initial_guess4=[0.0006, 28.42, 0.0424]
# He 304
initial_guess5=[0.006, 30.37, 0.0424]
# O 630
initial_guess6=[0.0005, 62.97, 0.0424]
# O 977
initial_guess7=[0.0014, 97.71, 0.0424]
# O 1032
initial_guess8=[0.0006, 103.19, 0.0424]

initial_guess=[initial_guess1,initial_guess2,initial_guess3,initial_guess4,initial_guess5,initial_guess6,initial_guess7,initial_guess8]