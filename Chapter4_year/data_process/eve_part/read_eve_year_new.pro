dir = 'data/EVE/'
pattern = 'EVS_L2_*.fit.gz'

; Get a list of all files matching the pattern in the directory
files_list = file_search(dir + pattern)
print, 'search complete'

; Create an array to keep track of files with errors
error_files = []

for i = 0, N_ELEMENTS(files_list) - 1 do begin
  file = files_list[i]  ;file is like 'data\EVE\EVS_L2_2011062_00_007_02.fit.gz'
  print, '1', file
  
  ; Check if the current file has already encountered an error
  if where(error_files EQ file, count) NE 0 then begin
    print, 'Skipping file:', file, '- Already encountered an error'
    continue  ; Skip to the next iteration
  endif
  
  ; Attempt to read the file and handle any errors
  catch, error
  begin
    eve_data = eve_read_whole_fits(file, /SILENT, /CONTINUE_ON_ERROR)
  catch, error_message
  end
  
  print, '2   ', i
  
  ; Check if an error occurred
  if keyword_set(error_message) then begin
    ; Handle the error
    print, 'Error reading file:', file
    print, 'Error message:', error_message
    ; Add the file to the error_files array
    error_files = [error_files, file]
    continue  ; Skip to the next iteration
  endif
 endfor
 
end