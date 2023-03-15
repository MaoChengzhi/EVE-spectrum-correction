;read_sdo,'aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits',aia_data
;fnames='aia_lev1_304a_2011_01_27t22_58_56_12z_image_lev1.fits'
;read_sdo,fnames,index,data
fnames="AIA20110127_225856_0304.fits"
aia_prep,fnames,-1,out_index,out_data
save,out_data,filename='IDL_data.sav'
end
