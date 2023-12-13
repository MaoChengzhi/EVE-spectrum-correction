cd, 'D:\py_repo\EVE-spectrum-correction\Chapter4_year\data_process\eve_part'
dir = 'data/EVE/'
pattern = 'EVS_L2_*.fit.gz'

; Get a list of all files matching the pattern in the directory
files_list = file_search(dir + pattern)
print,'good search: '


for i = 0, N_ELEMENTS(files_list) - 1 do begin

;test_start=5000
;test_end=test_start+100
;for i = test_start, test_end - 1 do begin



  ;file   is like     'data\EVE\EVS_L2_2011062_00_007_02.fit.gz'
  file = files_list[i]  
  
  ; i expect new file to be 'data/EVE_sav/EVS_L2_*.sav'
  new_filename = 'data/EVE_sav_full/' + strmid(file, strlen(dir), strlen(file)-strlen(dir)-7) + '.sav'

  ; Check if the file exists
   
   
  exists = FILE_TEST(new_filename, /regular)
  IF exists THEN BEGIN
    print,'File already exists:',new_filename
    
      continue
  endif
  
  
  catch, error
  IF error NE 0 THEN BEGIN
    PRINT, 'Error while processing:', file
    PRINT, 'Error message:', !ERROR_STATE.MSG
    ; Log the error to a file or designated location if desired
    continue
  ENDIF
  eve_data = eve_read_whole_fits(file)
  print,'good: ',file
  
  ;save the data needed into sav
  meta = eve_data.SPECTRUMMETA
  wavelength = meta.wavelength
  data = eve_data.SPECTRUM
  sod_time = data.sod           ; seconds UT day
  irradiance = data.irradiance ;[1363:1374]
  sc_flags = data.sc_flags      ; 0=good, other value indicates events
  flags = data.flags
  yyyydoy = data.yyyydoy

  SAVE, wavelength, sod_time, irradiance, sc_flags, flags, yyyydoy, FILENAME=new_filename
  
  
endfor
end

