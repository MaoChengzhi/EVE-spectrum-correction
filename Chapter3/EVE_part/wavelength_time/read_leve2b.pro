EVE_path="data/level2B/EVS_L2B_2011027_007_02.fit.gz"
eve_data = eve_read_whole_fits(EVE_path)
meta=eve_data.SPECTRUMMETA
wavelength=meta.wavelength  ;

data=eve_data.SPECTRUM
sod_time=data.sod           ;seconds  UT day
irradiance=data.irradiance  ;
sc_flags=data.sc_flags      ;0=good  other value indicates events


SAVE,wavelength,sod_time,irradiance,sc_flags,FILENAME="data/level2B/EVS_L2B_2011027_007_02.sav"

end
