## original
$$
g\left(A, \mu, \sigma^2\right)(x)=\int_{-\infty}^{\infty}\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu_i\right)^2}{2 \sigma_i^2}}\right]^2 d x
$$


## partial difference

$$
\frac{\partial g}{\partial A}=\int_{-\infty}^{\infty}2\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu\right)^2}{2 \sigma_i^2}}\right] \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}d x
$$

$$
\frac{\partial g}{\partial \mu}=\int_{-\infty}^{\infty}2\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu\right)^2}{2\sigma_i^2}}\right] \frac{A}{\sqrt{2 \pi \sigma^2}}  
(-\frac{\left(x-\mu\right)}{ \sigma^2}) e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}d x
$$

$$
\frac{\partial g}{\partial \sigma}=\int_{-\infty}^{\infty} 2\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n  \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu\right)^2}{2 \sigma_i^2}}\right] A
\left[ -\frac{1}{\sqrt{2 \pi} \sigma^2} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}+\frac{1}{\sqrt{2 \pi \sigma^2}} \frac{(x-\mu)^2}{\sigma^3} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}} \right]d x
$$




化简
$$
\int_{-\infty}^{\infty}\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu\right)^2}{2 \sigma_i^2}}\right]  e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}d x=0
$$

$$
\int_{-\infty}^{\infty}\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu\right)^2}{2 \sigma_i^2}}\right]  e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}(x-\mu)d x=0
$$

$$
\int_{-\infty}^{\infty}\left[\frac{A}{\sqrt{2 \pi \sigma^2}} e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}-\sum_{i=1}^n \frac{A_i}{\sqrt{2 \pi \sigma_i^2}} e^{-\frac{\left(x- \mu\right)^2}{2 \sigma_i^2}}\right]  e^{-\frac{\left(x-\mu\right)^2}{2 \sigma^2}}(x-\mu)^2 d x=0
$$

## solutions

### 1 1

$$
\begin{aligned}
& \int_{-\infty}^{+\infty} N\left(\mu, \sigma^2\right) N\left(\mu, \sigma^{2}\right)d x \\
& =\frac{1}{2\sqrt{\pi}\sigma}
\end{aligned}
$$

### 1 2

$$
\begin{aligned}
& \int_{-\infty}^{+\infty} N\left(\mu_i, \sigma_i^2\right) N\left(\mu, \sigma^{2}\right)(x-\mu)^2 d x\\
& =\frac{1}       
{      \sqrt{2 \pi  (\sigma^2+\sigma_i^2)}}
\exp\left(-{\frac{({\mu}-{\mu_i})^2}{2 \left(\sigma^2+\sigma_i^2\right)}}      \right)
\end{aligned}
$$



### 2 

$$
\begin{aligned}
& \int_{-\infty}^{+\infty} N\left(\mu, \sigma^2\right) N\left(\mu, \sigma^{2}\right)(x-\mu) d x \\
& =\frac{({\mu}-{\mu_i})\sigma^2}       
{      \sqrt{2 \pi  }(\sigma^2+\sigma_i^2)^{\frac{3}{2}}}

\exp\left({-\frac{({\mu}-{\mu_i})^2}{2 \left(\sigma^2+\sigma_i^2\right)}}      \right)
\end{aligned}
$$





### 3 1

$$
\begin{aligned}
& \int_{-\infty}^{+\infty} N\left(\mu, \sigma^2\right) N\left(\mu, \sigma^{2}\right)(x-\mu)^2 d x \\
& =\frac{\sigma}{4\sqrt{\pi}}
\end{aligned}
$$



### 3 2

$$
\begin{aligned}
& \int_{-\infty}^{+\infty} N\left(\mu_i, \sigma_i^2\right) N\left(\mu, \sigma^{2}\right)(x-\mu)^2 d x \\
& =\frac{\sigma^2\left[\left(\mu_i-\mu\right)^2 \sigma^2+\sigma^2 \sigma_i^2+\sigma_i^4\right] \exp \left[-\frac{\left(\mu_i-\mu\right)^2}{2\left(\sigma_i^2+\sigma^2\right)}\right]}{ \sqrt{2\pi}\left[\sigma^2+\sigma_i^2\right]^{5 / 2}}
\end{aligned}
$$



## equation

unknown variable:
$$
A    \\
\sigma  \\
\mu
$$


### 1

$$
A\frac{1}{2\sqrt{\pi}\sigma}-\sum_{i=1}^n A_i \frac{1}       
{      \sqrt{2 \pi  (\sigma^2+\sigma_i^2)}}
\exp\left[ {\frac{-({\mu}-{\mu_i})^2}{2 \left(\sigma^2+\sigma_i^2\right)}}      \right]=0
$$

### 2

$$
\sum_{i=1}^n A_i  \ \frac{({\mu}-{\mu_i})\sigma^2}       
{      \sqrt{2 \pi  }(\sigma^2+\sigma_i^2)^{\frac{3}{2}}}

\exp\left[{\frac{-({\mu}-{\mu_i})^2}{2 \left(\sigma^2+\sigma_i^2\right)}}      \right]=0
$$





### 3

$$
A \frac{\sigma}{4\sqrt{\pi}}- \sum_{i=1}^n A_i \ \frac{\sigma^2\left[\left(\mu_i-\mu\right)^2 \sigma^2+\sigma^2 \sigma_i^2+\sigma_i^4\right] }{ \sqrt{2\pi}\left[\sigma^2+\sigma_i^2\right]^{5 / 2}}\exp \left[-\frac{\left(\mu_i-\mu\right)^2}{2\left(\sigma_i^2+\sigma^2\right)}\right]=0
$$

