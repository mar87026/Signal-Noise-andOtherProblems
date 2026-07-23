# Wavelet, DCT

*Reduce the size and Recover losslessly is the topic.*

# Preliminaries

- Nyquist Theorem: Sample frequency must be larger than 2 times of signal frequency. Vice versa, while 2 different sine waves were sampled within same frequency, there’s only way to identify them: at least one is at a frequency below half of sample frequency. so for keeping the detail to identify, down sample pitch should not be less than half of image width/height.

# Wavelet:

![line_based_2d_dwt53_architecture.png](/operational_is_su-fficient/gitlab_stuff/wavelet,_dct/line_based_2d_dwt53_architecture.png)

1. Lifting Scheme: Reported by Wim Sweldens : “The Lifting Scheme: A Construction of Second Generation Wavelets”, All Discrete Wavlet Transforms are made of :
    1. Split → into even ones and odd ones
    2. Predict → predict odd point by nearby even pair of points, get the high frequency components ($d_i = x_{2i+1} - [\frac{x_{2i} + x_{2i+2}} {2}]$ ) that difference of real odd point and predicted odd point.
    3. Update → update low frequency ($s_i = x_{2i} - [\frac{d_{i-1} + d_{i} + 2} {4}]$ ) components within d and even point.