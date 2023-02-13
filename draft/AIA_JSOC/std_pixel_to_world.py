import sunpy.map
import astropy.units as u
import math

AIA_filename="data/AIA/Web_JSOC/_1p5/rebin/aia.lev1.2011-01-27T225858Z.304.image_lev1p5.fits"

m_aia=sunpy.map.Map(AIA_filename)
#%%
def std_pixel_to_world(pixel_x,pixel_y):
    """
    

    Parameters
    ----------
    pixel_x : The X component of the pixel position in the image
    
    pixel_y : The Y component of the pixel position in the image
            Image size: 4096*4096
            
    Returns
    -------
    Coordinates in the Helioprojective Cartesian (HPC) in rad
        using sunpy.map.sources.sdo.AIAMap.pixel_to_world method :
    
    Tx :  angle relative to the plane containing the Sun-observer line 
        and the Sun’s rotation axis, 
        with positive values in the direction of the Sun’s west limb.
        
    Ty : angle relative to the Sun’s equatorial plane, 
        with positive values in the direction of the Sun’s north pole.

    """
    point = m_aia.pixel_to_world(pixel_x * u.pixel, pixel_y * u.pixel)
    ## this step takes up 80% of the time
    Tx,Ty=point.to_string().split()
    Tx,Ty=float(Tx),float(Ty) #degree
    Tx,Ty=Tx*math.pi/180,Ty*math.pi/180
    return Tx,Ty
