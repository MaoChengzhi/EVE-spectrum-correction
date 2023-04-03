import numpy as np

coeff=np.load("coeff_of_my_pixel_to_world.npz")
coeff_Tx=coeff['coeff_Tx']
coeff_Ty=coeff['coeff_Ty']

def my_pixel_to_world(pixel_x,pixel_y):
    """
    

    Parameters
    ----------
    pixel_x : The X component of the pixel position in the image
    
    pixel_y : The Y component of the pixel position in the image
            Image size: 4096*4096
            
    Returns
    -------
    Coordinates in the Helioprojective Cartesian (HPC), which is observer-based:
        using a linear function to simulate
        
    Tx :  angle relative to the plane containing the Sun-observer line 
        and the Sun’s rotation axis, 
        with positive values in the direction of the Sun’s west limb.
        
    Ty : angle relative to the Sun’s equatorial plane, 
        with positive values in the direction of the Sun’s north pole.

    """
   
    Tx=coeff_Tx[0]*pixel_x+coeff_Tx[1]*pixel_y+coeff_Tx[2]
    Ty=coeff_Ty[0]*pixel_x+coeff_Ty[1]*pixel_y+coeff_Ty[2]

    return Tx,Ty
