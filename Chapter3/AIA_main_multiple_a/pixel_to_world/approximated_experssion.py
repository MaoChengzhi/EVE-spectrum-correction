import sunpy.map
import numpy as np
from std_pixel_to_world import std_pixel_to_world
from scipy import optimize
# %%

AIA_filename = "../data/AIA/aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits"
m_aia = sunpy.map.Map(AIA_filename)
image_data = m_aia.data
image_shape_x, image_shape_y = m_aia.data.shape


# =============================================================================
# to determine approximation range:
#
#
# image_shape_x = image_shape_y = 4096
# std_pixel_to_world(2048, 2048) = (0, 0)
# 0.6  arcsec / pix
# 实际十字扫描: solar radius: 16'    alpha offset:30'
# -> approximation angle range: from -46' to  46' = 2760''
# 46*60/0.6 = 4600
# -> approximation pixel range: from 2048-4600 = -2552  to  2048+4600 = 6648
#
# =============================================================================

approximation_points_num = 100
# Initialize arrays
x_pixel_list = np.linspace(-2552, 6648, approximation_points_num)
y_pixel_list = np.linspace(-2552, 6648, approximation_points_num)
standard_Tx_list = np.zeros((approximation_points_num**2, 1))
standard_Ty_list = np.zeros((approximation_points_num**2, 1))


# %%
# Obtain some standard data for approximation
point_list = np.zeros((approximation_points_num**2, 2))
i = 0

for x_pixel in x_pixel_list:
    for y_pixel in y_pixel_list:
        point_list[i] = x_pixel, y_pixel
        standard_Tx_list[i], standard_Ty_list[i] = std_pixel_to_world(
            x_pixel, y_pixel)
        i += 1

# %%


def func_Tx(x, y, p):
    """


    Parameters
    ----------
    x : x pixel list 
    y : y pixel list 
    p : coefficient array that needs to be fitted

    Returns
    -------
    HPC Tx coordinate calculated by current coefficient array

    """
    a, b, c = p
    return a*x+b*y+c


def func_Ty(x, y, p):
    """


    Parameters
    ----------
    x : x pixel list 
    y : y pixel list 
    p : coefficient array that needs to be fitted

    Returns
    -------
    HPC Ty coordinate calculated by current coefficient array

    """
    a, b, c = p
    return a*x+b*y+c


def residuals_Tx(p, Tx, x, y):
    """ 

    Returns
    -------
    Difference between the exact value of Tx(calculated by sunpy.map.sources.sdo.AIAMap.pixel_to_world) 
    and the fitting function with current coefficient array
    """
    return Tx - func_Tx(x, y, p)


def residuals_Ty(p, Ty, x, y):
    """ 

    Returns
    -------
    Difference between the exact value of Ty(calculated by sunpy.map.sources.sdo.AIAMap.pixel_to_world) 
    and the fitting function with current coefficient array
    """
    return Ty - func_Ty(x, y, p)


# %%
# Reorganize arrays for fitting
x = point_list[:, 0]
Tx = standard_Tx_list
Tx = Tx.reshape(approximation_points_num**2, )
y = point_list[:, 1]
Ty = standard_Ty_list
Ty = Ty.reshape(approximation_points_num**2, )

# Least squares fitting
plsq_Tx = optimize.leastsq(residuals_Tx, np.array([0, 0, 0]), args=(Tx, x, y))
plsq_Ty = optimize.leastsq(residuals_Ty, np.array([0, 0, 0]), args=(Ty, x, y))


# %%

np.savez("coeff_of_my_pixel_to_world.npz",
         coeff_Tx=plsq_Tx[0], coeff_Ty=plsq_Ty[0])
