result = vso_search('2011-01-01 0:00', '2011-01-02 0:00', inst='eve', level=2)
log = vso_get(result, out_dir='data/EVE', filenames=fnames, /nodownload)

; Extract URLs
; Initialize url_list as a string array
url_list = strarr(n_elements(log))   
for i = 0, n_elements(log) - 1 do begin
  url_list[i] = log[i].url
endfor

; Initialize LUN variable
lun = 6   
; Save the URL list into a text file
openw, lun, 'data/url_list_day.txt'
for i = 0, n_elements(url_list) - 1 do begin
  printf, lun, url_list[i]
endfor
free_lun, lun
end


