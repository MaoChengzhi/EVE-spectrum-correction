dir = 'data/EVE/'
pattern = 'EVS_L2_*.fit.gz'

; Get a list of all files matching the pattern in the directory
files_list = file_search(dir + pattern)
print, 'good search: '
for i = 0, N_ELEMENTS(files_list) - 1 do begin
  file = files_list[i]

  ; i expect new file to be 'data/EVE_sav/EVS_L2_*.hdf5'
  new_filename = 'data/EVE_sav_full/' + strmid(file, strlen(dir), strlen(file) - strlen(dir) - 7) + '.hdf5'

  ; Check if the file exists
  exists = FILE_TEST(new_filename, /regular)
  IF exists THEN BEGIN
    print, 'File already exists:', new_filename
    continue
  endif

  catch, error
  IF error NE 0 THEN BEGIN
    PRINT, 'Error while processing:', file
    PRINT, 'Error message:', !ERROR_STATE.MSG
    continue
  ENDIF

  eve_data = eve_read_whole_fits(file)
  print, 'good: ', file

  ; Create an HDF5 file
  hdf5_file = H5F_CREATE(new_filename)

  ; Extract and write the data needed into the HDF5 file
  meta = eve_data.SPECTRUMMETA
  wavelength = meta.wavelength
  data = eve_data.SPECTRUM
  sod_time = data.sod           ; seconds UT day
  irradiance = data.irradiance ; [1363:1374]
  sc_flags = data.sc_flags      ; 0=good, other value indicates events
  flags = data.flags
  yyyydoy = data.yyyydoy

  ; Create datasets in the HDF5 file for each variable
  H5D_CREATE, hdf5_file, 'wavelength', wavelength
  H5D_CREATE, hdf5_file, 'sod_time', sod_time
  H5D_CREATE, hdf5_file, 'irradiance', irradiance
  H5D_CREATE, hdf5_file, 'sc_flags', sc_flags
  H5D_CREATE, hdf5_file, 'flags', flags
  H5D_CREATE, hdf5_file, 'yyyydoy', yyyydoy

  ; Close the HDF5 file
  H5F_CLOSE, hdf5_file
endfor
end