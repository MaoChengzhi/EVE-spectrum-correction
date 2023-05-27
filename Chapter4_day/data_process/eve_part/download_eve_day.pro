result = vso_search('2011-01-11 0:00', '2011-01-12 0:00', inst='eve', level=2)
log = vso_get(result, out_dir='data/EVE', filenames=fnames, /nodownload)

; Extract URLs
url_list = strarr(n_elements(log))   ; Initialize url_list as a string array
for i = 0, n_elements(log) - 1 do begin
    url_list[i] = log[i].url
endfor

lun = 6   ; Initialize LUN variable
; Save the URL list into a text file
openw, lun, 'url_list.txt'
for i = 0, n_elements(url_list) - 1 do begin
    printf, lun, url_list[i]
endfor
free_lun, lun

end