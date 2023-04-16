EVE_path = ['data/EVE/EVS_L2_2011027_14_007_02.fit.gz', $
            'data/EVE/EVS_L2_2011027_16_007_02.fit.gz', $
            'data/EVE/EVS_L2_2011027_18_007_02.fit.gz', $
            'data/EVE/EVS_L2_2011027_20_007_02.fit.gz', $
            'data/EVE/EVS_L2_2011027_22_007_02.fit.gz', $
            'data/EVE/EVS_L2_2011027_23_007_02.fit.gz']

EVE_data_14 = eve_read_whole_fits(EVE_path[0])
EVE_data_16 = eve_read_whole_fits(EVE_path[1])
EVE_data_18 = eve_read_whole_fits(EVE_path[2])
EVE_data_20 = eve_read_whole_fits(EVE_path[3])
EVE_data_22 = eve_read_whole_fits(EVE_path[4])
EVE_data_23 = eve_read_whole_fits(EVE_path[5])


;meta=eve_data.SPECTRUMMETA
;wavelength=meta.wavelength
;sod_time=data.sod


FOR i=0,5 DO BEGIN
  eve_data = eve_read_whole_fits(EVE_path[i])
  meta=eve_data.SPECTRUMMETA
  wavelength=meta.wavelength  ;
  
  data=eve_data.SPECTRUM
  sod_time=data.sod           ;seconds  UT day
  irradiance=data.irradiance  ;
  sc_flags=data.sc_flags      ;0=good  other value indicates events

  filename="data/EVE_sav/EVS"+STRTRIM(i,1)+".sav"
  SAVE,wavelength,sod_time,irradiance,sc_flags,FILENAME="data/EVE_sav/EVS"+STRTRIM(i,1)+".sav"

ENDFOR  

end
