import sunpy.map
import matplotlib.pyplot as plt
import astropy.units as u

# %%


def reproject_to_aia(map_aia, map_euvi, out_shape):
    out_header = sunpy.map.make_fitswcs_header(
        out_shape,
        map_aia.reference_coordinate.replicate(
            rsun=map_euvi.reference_coordinate.rsun),
        scale=u.Quantity(map_aia.scale),
        instrument="EUVI",
        observatory="AIA Observer",
        wavelength=map_euvi.wavelength)

    outmap = map_euvi.reproject_to(out_header)
    return outmap


def plot_reproject(map_aia, map_euvi, outmap):
    fig = plt.figure()
    # ax1 = fig.add_subplot(121, projection=map_aia)
    # map_aia.plot(axes=ax1)

    # ax2 = fig.add_subplot(122, projection=outmap)
    # outmap.plot(axes=ax2, title='EUVI image as seen from SDO')
    # map_euvi.draw_limb(color='blue')

    ax2 = fig.add_subplot(111, projection=outmap)
    outmap.plot(axes=ax2, title='EUVI image as seen from SDO')
    map_euvi.draw_limb(color='blue')
    # Set the HPC grid color to black as the background is white
    ax2.coords[0].grid_lines_kwargs['edgecolor'] = 'k'
    ax2.coords[1].grid_lines_kwargs['edgecolor'] = 'k'
