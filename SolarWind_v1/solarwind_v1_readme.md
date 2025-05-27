# SolarWind_v1

This folder contains scripts and notebooks for cross-calibrating AIA images and EVE spectral data over 1000 days, focusing on a single EVE spectral line.

Inspired by the first phase of this research, this project applies a pixel-by-pixel correction method using AIA images to reconstruct more accurate EVE spectral line signals. For each AIA image pixel, a Gaussian curve is constructed:

$$
f(\lambda) = A \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(\lambda-\mu)^2}{2\sigma^2}}
$$

where:
- **Center wavelength $\mu$**: Corrected as $\mu(T_x, T_y) \approx C_1 T_x^2 + C_2 T_x + C_3 T_y^2 + C_4 T_y + C_5$, with $T_x, T_y$ as pixel angles and $C_i$ as fit coefficients.
- **Area $A$**: Given by the AIA pixel DN (Digital Number) value.
- **FWHM**: Treated as a constant.

The constant term represents the 'true' line center offset from the CHIANTI database value (assuming zero-point calibration is sufficiently accurate, though this assumption is quite debatable).

The main intended workflow includes, though it has not been implemented:
- Collecting 1000 days of AIA images and EVE spectra for one line.
- Fitting the model to determine the correction coefficients.
- Comparing and analyzing the reconstructed EVE line profiles.

Only a little effort has been devoted to this section.