cd, 'D:\py_repo\EVE-spectrum-correction\Chapter4_v1\data_process\eve_part'
dir = 'data/EVE/'
pattern = 'EVS_L2_*.fit.gz'

; Get a list of all files matching the pattern in the directory
files_list = file_search(dir + pattern)
print,'good search: '




i=100

;file   is like     'data\EVE\EVS_L2_2011062_00_007_02.fit.gz'
file = files_list[i]

; i expect new file to be 'data/EVE_sav/EVS_L2_*.sav'
new_filename = 'data/EVE_sav_full/' + strmid(file, strlen(dir), strlen(file)-strlen(dir)-7) + '.sav'

; Check if the file exists

exists = FILE_TEST(new_filename, /regular)
IF exists THEN BEGIN
  print,'File already exists:',new_filename

endif


catch, error
IF error NE 0 THEN BEGIN
  PRINT, 'Error while processing:', file
  PRINT, 'Error message:', !ERROR_STATE.MSG
  ; Log the error to a file or designated location if desired
ENDIF
eve_data = eve_read_whole_fits(file)
print,'good: ',file

;save the data needed into sav
meta = eve_data.SPECTRUMMETA
wavelength = meta.wavelength
data = eve_data.SPECTRUM
sod_time = data.sod           ; seconds UT day
irradiance = data.irradiance ;
sc_flags = data.sc_flags      ; 0=good, other value indicates events
flags = data.flags
yyyydoy = data.yyyydoy


end