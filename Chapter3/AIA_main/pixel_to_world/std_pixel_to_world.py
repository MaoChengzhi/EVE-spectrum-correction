import sunpy.map
import astropy.units as u
import math
from aiapy.calibrate import register, update_pointing, normalize_exposure

AIA_filename = "../data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits"
m_aia = sunpy.map.Map(AIA_filename)
m_normalized = normalize_exposure(register(update_pointing(m_aia)))
# %%


def std_pixel_to_world(pixel_x, pixel_y):
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
    point = m_normalized.pixel_to_world(pixel_x * u.pixel, pixel_y * u.pixel)

# =============================================================================
#     # This step takes up 80% of the time
#     Tx, Ty = point.to_string().split()
#     Tx, Ty = float(Tx), float(Ty)  # degree
# =============================================================================

    Tx, Ty = point.Tx.value, point.Ty.value  # arcsec
    Tx, Ty = Tx*math.pi/(180*3600), Ty*math.pi/(180*3600)  # radian
    return Tx, Ty
