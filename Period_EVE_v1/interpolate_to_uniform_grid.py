import numpy as np
from scipy.interpolate import griddata

def interpolate_to_uniform_grid(x=np.array([]), y=np.array([]), z=np.array([]), scale_factor_x=1,scale_factor_y=1,method='linear'):
    

    if not z.size:
        raise ValueError('z must be a 2D array')
    
    if not x.size:
        x=np.arange(z.shape[0]) 

    if not y.size:
        y=np.arange(z.shape[1])

        
    print("intput shape:x:",x.shape,"y:",y.shape,"z:",z.shape)

    # Create a meshgrid from the non-uniform x, y data
    X, Y = np.meshgrid(x, y,indexing='xy')
    
    # Flatten the meshgrid and data for interpolation
    X_flat = X.flatten()
    Y_flat = Y.flatten()
    z_flat = z.flatten()

    x_num=x.size*scale_factor_x
    y_num=y.size*scale_factor_y

    # Define the uniform grid
    xi = np.linspace(np.min(x), np.max(x), x_num)
    yi = np.linspace(np.min(y), np.max(y), y_num)
    xi, yi = np.meshgrid(xi, yi)



    # Interpolate the data onto the uniform grid
    zi = griddata((X_flat, Y_flat), z_flat, (xi, yi), method=method)
    
    print("output shape:xi:",xi.shape,"yi:",yi.shape,"zi:",zi.shape)
    return xi, yi, zi