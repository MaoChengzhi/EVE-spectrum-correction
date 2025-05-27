# Chapter 4 v2

This folder contains scripts and notebooks for the analysis of AIA and EVE He II spectral line data, based on results processed in v1.

- Completed long-term monitoring of three parameters (amplitude, center, FWHM) for the EVE He II line.
- Explored mapping AIA images to EVE spectral parameters using gradient descent, but I started to ponder and doubt approach reliability and physical mechanism.
- 
- The mapping from AIA to EVE parameters is modeled as:
  
  $$
  f(\lambda)=A \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(\lambda-\mu)^2}{2\sigma^2}}
  $$
  where:
  - Center $\mu$ is corrected as $\mu=\mu(T_x,T_y) \approx C_1 T_x^2+ C_2 T_x +C_3 T_y+C_4$, with $T_x, T_y$ as pixel angles and $C_i$ as fit coefficients.
  - Area $A$ is represented by the AIA pixel DN value.
  - FWHM is set as a constant.

