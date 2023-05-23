dir = 'data/EVE/'
pattern = 'EVS_L2_*.fit.gz'

; Get a list of all files matching the pattern in the directory
files_list = file_search(dir + pattern)
print,'good search: '
for i = 0, N_ELEMENTS(files_list) - 1 do begin
  file = files_list[i]  ;file   is like     'data\EVE\EVS_L2_2011062_00_007_02.fit.gz'
  
  print,i
  ; Attempt to read the file and handle any errors
  ;catch, error
  ;begin
    eve_data = eve_read_whole_fits(file, /SILENT, /CONTINUE_ON_ERROR)
    ;catch, error_message
  ;end 
  
   
  print,'good: ',file
  meta = eve_data.SPECTRUMMETA
  wavelength = meta.wavelength
  
  data = eve_data.SPECTRUM
  sod_time = data.sod           ; seconds UT day
  irradiance = data.irradiance[1363:1374]
  sc_flags = data.sc_flags      ; 0=good, other value indicates events
  flags = data.flags
  yyyydoy = data.yyyydoy

  new_filename = 'data/EVE_sav/' + strmid(file, strlen(dir), strlen(file)-strlen(dir)-7) + '.sav'
  ; i expect new file to be 'data/EVE_sav/EVS_L2_*.sav'
  SAVE, wavelength, sod_time, irradiance, sc_flags, flags, yyyydoy, FILENAME=new_filename
  
endfor
end

