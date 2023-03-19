data=eve_read_whole_fits('data/EVE/EVS_L2_2011027_20_007_02.fit.gz')

wg=where(data.spectrum[0].irradiance gt 0)
plot_io,data.spectrummeta[wg].wavelength,data.spectrum[0].irradiance[wg],xtitle="Wavelength(nm)",ytitle="Irradiance(W/m!U2!N/nm)"
end