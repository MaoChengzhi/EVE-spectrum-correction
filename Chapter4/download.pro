; Load the VSO library
;vso_init

; Define the start and end times of the data you want to retrieve
start_time = '2012-07-07T00:00:00'
end_time = '2012-07-07T01:00:00'

; Define the parameters of the data you want to retrieve
wavelength_min = 5.0
wavelength_max = 40.0
level = 2
source = 'sdo'
instrument = 'eve'

; Use the VSO API to search for the data
results = vso_search(start_time, end_time, wavelength_min, wavelength_max, /level, source=source, instrument=instrument)

; Download the data
vso_get(results)

end