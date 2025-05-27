# EVE Spectrum Correction

This project focuses on verifying and extending the results from **“基于 SDO/EVE 光谱观测对太阳大气等离子体运动的研究”** (Cheng et al., 2021).  
The primary goals are

* to calibrate EVE spectral data (with special attention to the cruciform-scan optics),
* to analyse long-term spectral behaviour,
* and to explore how AIA images can be mapped to EVE spectral parameters.

---

## Project Structure

| Chapter / Folder      | Objective                                                    | Key Files                                                    |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Chapter 3**         | Cruciform-scan calibration; verify solar-plasma-motion study | `AIA_main/`, `data_frame.pkl`, `Func_Performance_Analysis.ipynb`, `结构.xmind` |
| **Chapter 4 v1**      | First full-pipeline test of EVE L2 processing                | `combine_basic.ipynb`, `constant.py`                         |
| **Chapter 4 v2**      | Refined mapping of AIA ➔ EVE (He II 304 Å)                   | `basic_ops/`                                                 |
| **Chapter 4 v3**      | Four-year temporal scan of 46 EVE lines                      | `basic_ops/`, `新建文件夹/`                                  |
| **Period_EVE_v1**     | Global periodicity search with wavelets                      | `daily_plot.ipynb`, `do_wavelet.py`                          |
| **Flare Spectrum v1** | Response of EVE lines to solar flares                        | `FirstGlance_Flare.ipynb`, `data/`                           |
| **SolarWind v1**      | 1000-day cross-calibration of AIA & EVE                      | `combine_basic.ipynb`, `error_function.py`                   |

---

## Chapter 3  — Cruciform-Scan Calibration

### 3.1  Input Data for the Cruciform Scan  

The Chamberlin (2016) relation is adopted as the sole external input:

$$
\Delta\lambda = 19.8\sin^{2}\phi \;+\; 4.3\sin\theta
$$



---

### 3.2  Central-Wavelength Shift versus Incident Angles (α, β)

<div align="center">

| Simulation (this work, 2048² resolution)                     | From Cheng et al. (2021)                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="./README_Chinese.assets/image-20230311161350913.png" alt="My simulation (blue) vs. paper (orange)" style="zoom:25%;"> | <img src="./README_Chinese.assets/image-20230311161545859.png" alt="Paper figure: simulated (red) vs. observed (black dashed)" style="zoom:67%;"> |

</div>

*My correction (blue) yields a positive-going shift, whereas the paper’s correction yields a negative-going shift.*

---

### 3.3  Why Does the β-Scan Curve Flatten?

Solar irradiance was nearly constant during the scan, implying occultation by the entrance slit.  
Yet the sudden dip in panel (c) below remains unexplained:

<img src="./README_Chinese.assets/image-20230602120901238.png" alt="Beta-scan brightness drop" style="zoom:50%;">

Because the detailed slit geometry is unavailable, we diverted to long-term Doppler analysis:

| STEREO-A field brightness                                    | STEREO-B field brightness                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="./README_Chinese.assets/image-20230416143802583-1681642430415-4.png" alt="STEREO A" style="zoom:15%;"> | <img src="./README_Chinese.assets/image-20230416143755917.png" alt="STEREO B" style="zoom:25%;"> |

No appreciable change was found in the EUVI 30.4 nm band throughout the β-scan:

<img src="./README_Chinese.assets/image-20230416145804719.png" alt="STEREO EUVI brightness trend" style="zoom:50%;">

---

## Chapter 4  — EVE Spectral Analysis

### 4.1  Expected Optical-Correction Trend

Corrected line-centre should be flat (dashed reference):

<img src="./README_Chinese.assets/image-20230416183316726.png" alt="Expected horizontal correction" style="zoom:150%;">

---

### 4.2  Overview of EVE L2 Data

<img src="./README_Chinese.assets/image-20230602120427014.png" alt="EVE L2 overview" style="zoom:50%;">

Daily statistics (8640 points day⁻¹) with ±3 σ shading:

![newplot](./README_Chinese.assets/newplot-1686219087659-1.png)

---

### 4.3  AIA Simulation vs. EVE Observation

| Constant FWHM assumption                                     | Variable FWHM                                           |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| ![newplot (1)](./README_Chinese.assets/newplot_(1)-1686219585220-3.png) | ![newplot (2)](./README_Chinese.assets/newplot_(2).png) |

---

### 4.4  Long-Term Monitoring of He II 304 Å

*Amplitude, centre, and FWHM have been tracked continuously since 2010-05-01.*

Wavelet transform of the line-centre parameter:

![He II 304_wavelet](./README_Chinese.assets/He_II_304_wavelet.png)

Peak periods across 46 lines versus formation temperature:

![{D32AE566-380B-4B46-A4D6-BD5D6EAC465E}](./README_Chinese.assets/{D32AE566-380B-4B46-A4D6-BD5D6EAC465E}.png)

No single global periodicity emerges, although individual lines show strong 27-day and 13-day signatures.

---

## Chapter 5  Solar Flares

During several M- and X-class flares the He II 304 Å FWHM narrows, while amplitude spikes and line centre blueshifts by ≈ 20 km s⁻¹.  
Data for 50+ flares have been collected for statistical study (see *Flare Spectrum v1*).

---

## Chapter 6  Cross-Calibration with Solar Wind

A 1000-day pixel-wise correction scheme links AIA EUV images to synthetic EVE spectra.  
Gaussian models for 12 strong lines are fitted, but full propagation of AIA errors is pending.

---

## Summary

This repository delivers

1. **A reproducible cruciform-scan calibration** that exposes a sign error in the published correction curve.  
2. **A four-year archive of EVE He II 304 Å diagnostics** with daily wavelet analysis, revealing persistent rotational periodicities but no multi-line global mode.  
3. **Preliminary flare and solar-wind cross-calibrations** laying the groundwork for future automated prediction of EVE spectra from AIA images.

Further work will refine the pixel-by-pixel AIA➔EVE mapping, incorporate slit-diffraction modelling, and extend the flare database to Solar Cycle 25.

---
