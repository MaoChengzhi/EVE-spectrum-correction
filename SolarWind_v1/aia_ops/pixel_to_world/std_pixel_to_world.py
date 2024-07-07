import sunpy.map
import astropy.units as u
import math
from aiapy.calibrate import register, update_pointing, normalize_exposure


# %%


def std_pixel_to_world(aia_map,pixel_x, pixel_y):
    """
    GenericMap.pixel_to_world in this function is extremly slow. 

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
    point = aia_map.pixel_to_world(pixel_x * u.pixel, pixel_y * u.pixel)
    Tx, Ty = point.Tx.value, point.Ty.value  # arcsec
    Tx, Ty = Tx*math.pi/(180*3600), Ty*math.pi/(180*3600)  # radian
    return Tx, Ty
