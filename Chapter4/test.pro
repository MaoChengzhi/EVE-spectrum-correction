result=vso_search('2011-01-01 1:00','2011-01-01 3:00',inst='eve',sample=3600) 

log=vso_get(result,out_dir='data_IDL',filenames=fnames) 
print,transpose(fnames)
end