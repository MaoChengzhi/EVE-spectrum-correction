give me  1000days of AIA images , EVE spectrum data for one line.



fit the get the coeff



受到本研究第一阶段工作的启发，我采用了基于AIA图像的逐像素修正方法，以期获取更准确的EVE谱线信号。对AIA图像的每一个像素构造一个高斯曲线$f(\lambda)=A \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(\lambda-\mu)^2}{2\sigma^2}}$，其中各参数如下：

- 中心波长 $\mu$ : 使用公式 $\mu=\mu(T_x,T_y) \approx C_1 T_x^2+ C_2 T_x +C_3 T_y^2+C_4 T_y+C_5$ 进行修正，其中$T_x, \ T_y$代表像素在视野中的角度，$C_1,C_2,C_3,C_4$ 为代拟合参数
- 积分面积 A：以AIA图像每个像素观测值DN( Digital Number）表示
- 半高全宽 FWHM:







and the constant term represent the 'true' line central away from chianti database. ( Assuming the zero point calibration is done good enough) (But I strongly disagrees with this assumption irrationally)