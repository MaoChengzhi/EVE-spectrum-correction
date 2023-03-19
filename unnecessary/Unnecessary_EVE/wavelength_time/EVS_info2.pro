
  ; specify the path to your FITS file
  fits_path = 'data/EVE/EVS_L2_2011027_20_007_02.fit.gz'
  
  ; read in the FITS file using the procedure
  eve_data = eve_read_whole_fits(fits_path)
  meta=eve_data.SPECTRUMMETA
  wavelength=meta.wavelength
  ; from 3 to 106  step:5200
  accuracy=meta.accuracy
  
  
  
  data=eve_data.SPECTRUM
  
  tai=data.tai
  ;seconds  since Jan 1,1958
  
  yyyydoy=data.yyyydoy 
  ;4 digits year + 3 digits year
  
  sod_time=data.sod
  ;seconds  UT day
  
  flags=data.flags
  ;0=good
  
  sc_flags=data.sc_flags
  ;0=good  other value indicates events 
  
  int_time=data.int_time
  ;duration of the exposure    :10s
  
  irradiance=data.irradiance
  ;W m^-2 nm^-1
  ;size(irradiance)
  ;2    5200   360   4  1872000
  
  SAVE,sod_time,irradiance,wavelength,FILENAME='IDL_vars.sav'
end