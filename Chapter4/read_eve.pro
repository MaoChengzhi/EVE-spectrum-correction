eve_data = eve_read_whole_fits( 'data/test/EVS_L2_2011034_00_007_02.fit.gz' )
;help,data,/structures

meta=eve_data.SPECTRUMMETA
wavelength=meta.wavelength  ;

data=eve_data.SPECTRUM
sod_time=data.sod           ;seconds  UT day
irradiance=data.irradiance  ;
sc_flags=data.sc_flags      ;0=good  other value indicates events
flags=data.flags

filename="data/test/EVS.sav"
SAVE,wavelength,sod_time,irradiance,sc_flags,flags,FILENAME=filename

;plot, eve_data.spectrummeta.wavelength , eve_data.spectrum[310].irradiance, YRANGE=[1.0e-6, 1.0e-2], /YLOG, charsize = 1.5, xtitle = "Wavelength (nm)", ytitle = "Irradiance (W/m^2/nm)"


;result=vso_search('2011-02-03 0:00','2011-02-04 00:00',inst='eve') 
;help,result
;help,result,/structures

;log=vso_get(result,out_dir='data',filenames=fnames,/rice)
;
;
;
;
;start_time = '2010-01-01T00:00:00'
;end_time = '2010-01-01T00:05:00'
;inst = 'EVE'
;series = 'L2CSPECTRUM'
;q = vso_search(start_time, end_time, instrument=inst,series)

end