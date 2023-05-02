result=vso_search('2012-03-26','2013-03-26 0:00',inst='eve',level=2)
;result=vso_search('2010-10-29 0:00','2011-03-03 0:00',inst='eve',level=2)
log=vso_get(result,out_dir='data/EVE',filenames=fnames)

end

;print,transpose(fnames)    ,sample=3600,
;
;result=vso_search(2011-01-01 1:00','2011-01-01 1:59',inst='aia')
;result=vso_search('2012-01-01 1:00','2012-01-01 6:00',inst='eve',level=2)
;result=vso_search('2011-01-27 1:00','2011-\01-27 6:00',inst='eve',level=2)

