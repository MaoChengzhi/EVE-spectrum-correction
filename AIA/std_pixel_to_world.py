import sunpy.map
import astropy.units as u
import math

AIA_filename="data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits"
m_aia=sunpy.map.Map(AIA_filename)
#%%
def std_pixel_to_world(pixel_x,pixel_y):
    """
    

    Parameters
    ----------
    pixel_x : TYPE
        DESCRIPTION.
    pixel_y : TYPE
        DESCRIPTION.

    Returns
    -------
    Tx : TYPE
        DESCRIPTION.
    Ty : TYPE
        DESCRIPTION.

    """
    point = m_aia.pixel_to_world(pixel_x * u.pixel, pixel_y * u.pixel)
    ## this step takes up 80% of the time
    Tx,Ty=point.to_string().split()
    Tx,Ty=float(Tx),float(Ty) #degree
    Tx,Ty=Tx*math.pi/180,Ty*math.pi/180
    return Tx,Ty
