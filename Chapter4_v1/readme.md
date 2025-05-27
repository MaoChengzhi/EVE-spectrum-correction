# Chapter 4 v1

This folder contains scripts and notebooks for reading and processing EVE data.


- In Python, process level 2 eve data and get He 304 parameters using Gaussian fitting.

EVE data at all levels are available in IDL/SSW, but not in python.


- Attempted to use the optical correction formula from the cross-scan method for long-term correction, but the results were not satisfactory, which is expected.
- Adjusted coefficients so that AIA images, combined with correction factors, could reproduce the EVE 304 line parameters for a given day. Noted that Hudson has done similar work, but their interpretation of the linear term as purely Doppler shift is likely incomplete due to instrumental effects.
- Tried using gradient descent to map AIA images to EVE 304 line parameters, but this approach did not work well.
