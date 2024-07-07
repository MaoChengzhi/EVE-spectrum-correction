version 2

使用v1处理好的 AIA与EVE He 谱线数据

完成了对EVE HE2 谱线三个参数的长期观测

尝试了寻找从 一个AIA图片到 -> EVE谱线参数的映射

但是感觉不太靠谱

 





version 4



$f(\lambda)=A \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(\lambda-\mu)^2}{2\sigma^2}}$，其中各参数如下：

- 中心波长 $\mu$ : 使用公式 $\mu=\mu(T_x,T_y) \approx C_1 T_x^2+ C_2 T_x +C_3 T_y+C_4$ 进行修正，其中$T_x, \ T_y$代表像素在视野中的角度，$C_1,C_2,C_3,C_4$ 为代拟合参数
- 积分面积 A：以AIA图像每个像素观测值DN( Digital Number）表示
- 半高全宽 FWHM: 设置成 const