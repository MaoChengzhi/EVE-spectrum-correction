import astropy.units as u
from astropy.constants import au,R_sun

R_sun=700000e3
au=150e9
4.3*au/R_sun
19.8*    (au/R_sun)**2  * (3.14/(180*60))**2
4.3*   (au/R_sun)*(3.14/(180*60))
#%%
print(19.8*(au/R_sun)**2  /1000)
print(4.3*(au/R_sun)/1000)
#%%
4096**2/200**2    *100  /3600