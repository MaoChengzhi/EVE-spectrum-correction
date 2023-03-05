; specify the path to your FITS file
fits_path = 'EVS_L2_2011027_18_007_02.fit.gz'

; read in the FITS file using the procedure
eve_data = eve_read_whole_fits(fits_path)


;Primary
pri=eve_data.primary
print,'PRIMARY'
help,pri,/structure
print

;PRIMARY_HEAD
pri_head=eve_data.primary
print,'PRIMARY_HEAD'
help,pri_head,/structure
print

;SPECTRUMMETA
meta=eve_data.SPECTRUMMETA
print,'SPECTRUMMETA'
help,meta,/structure

;SPECTRUMMETA_HEADER
meta_header=eve_data.SPECTRUMMETA_HEADER
print,'SPECTRUMMETA_HEADER'
help,meta_header,/structure
print

;SPECTRUMUNITS
unit=eve_data.SPECTRUMUNITS
print,'SPECTRUMUNITS'
help,unit,/structure
print

;SPECTRUMUNITS_HEADER
unit_header=eve_data.SPECTRUMUNITS_HEADER
print,"SPECTRUMUNITS_HEADER"
help,unit_header,/structure
print

;SPECTRUM  
spec=eve_data.SPECTRUM
print,"SPECTRUM"
help,spec,/structure
print


;SPECTRUM_HEADER
spec_header=eve_data.SPECTRUM
print,"SPECTRUM_HEADER"
help,spec_header,/structure
print
end