import numpy as np
from ..segmentation.threshold import ThresholdSegmentation

import matplotlib.pyplot as plt
img = (np.random.rand(100,100) * 255).astype(np.uint8) 
ts = ThresholdSegmentation(img, 128)
seg_img, _ = ts.segment_image()    

plt.figure('ThresholdSegmentation Example')
plt.subplot(1, 2, 1)
plt.imshow(img, interpolation='none')
plt.subplot(1, 2, 2)
plt.imshow(seg_img, interpolation='none')
plt.colorbar()