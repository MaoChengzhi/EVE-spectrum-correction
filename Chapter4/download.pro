;result=vso_search('2011-01-27 16:00','2011-02-29 18:00',inst='eve',level=2,sample=3600000)
result=vso_search('2011-01-01 1:00','2011-01-01 1:51',inst='aia',wave=171,sample=600)
;log=vso_get(result,out_dir='data_IDL',filenames=fnames)

end

;print,transpose(fnames)    ,sample=3600,
;
;result=vso_search(2011-01-01 1:00','2011-01-01 1:59',inst='aia')
;result=vso_search('2012-01-01 1:00','2012-01-01 6:00',inst='eve',level=2)
;result=vso_search('2011-01-27 1:00','2011-01-27 6:00',inst='eve',level=2)

