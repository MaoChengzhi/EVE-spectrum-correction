| Parameter | Y-axis Label                 | Percentile Range for ylim | ylim Calculation                                             |
| --------- | ---------------------------- | ------------------------- | ------------------------------------------------------------ |
| Amplitude | Amplitude (W m^{-2} nm^{-1}) | 0.0 to 99.9               | ylim = (0, 1.2 * upper_percentile)                           |
| Mean      | Mean (nm)                    | 0.1 to 99.8               | ylim = (lower_percentile, upper_percentile + 0.1 * (upper_percentile - lower_percentile)) |
| FWHM      | FWHM (nm)                    | 0.05 to 99.95             | ylim = (lower_percentile, upper_percentile)                  |

这个数字就是看着波段大概选的