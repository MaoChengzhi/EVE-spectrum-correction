
EVE_path="data/EVE_Fido/eve_l2_spectra_2011027_20.fits"
eve_data = eve_read_whole_fits(EVE_path)

meta=eve_data.SPECTRUMMETA
wavelength=meta.wavelength  ;

data=eve_data.SPECTRUM
sod_time=data.sod           ;seconds  UT day
irradiance=data.irradiance  ;
sc_flags=data.sc_flags      ;0=good  other value indicates events


SAVE,wavelength,sod_time,irradiance,sc_flags,FILENAME="data/test/test.sav"

end

