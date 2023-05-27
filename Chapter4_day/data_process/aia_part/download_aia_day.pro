result = vso_search('2011-01-01 0:00', '2011-01-02 0:00', inst='aia',wave=304)
log = vso_get(result, out_dir='data/AIA', filenames=fnames);, /nodownload)



end

; Extract URLs
;url_list = strarr(n_elements(log))   ; Initialize url_list as a string array
;for i = 0, n_elements(log) - 1 do begin
 ; url_list[i] = log[i].url
;endfor

;lun = 6   ; Initialize LUN variable
; Save the URL list into a text file
;openw, lun, 'data/url_aia_day.txt'
;for i = 0, n_elements(url_list) - 1 do begin
;  printf, lun, url_list[i]
;endfor
;free_lun, lun