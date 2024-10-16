#Canny edge detection
import matplotlib.pyplot as plt
import numpy as np 
import os

from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray
from skimage.exposure import histogram, cumulative_distribution
from skimage.filters import threshold_otsu

from scipy import ndimage as ndi 
from skimage.util import random_noise
from skimage import feature

my_path = os.path.abspath('/Users/yangyangxiayule/Documents/GitHub/Computer-Modelling-Y3/Lab3-Figures') 
leaf2 = imread('/Users/yangyangxiayule/Documents/GitHub/Computer-Modelling-Y3/images-lab3/leaf2.jpg', mode='L')

edges1 = feature.canny(leaf2)
edges2 = feature.canny(leaf2, sigma=3)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(leaf2, cmap='gray')
ax[0].set_title('Leaf2 Gray Image', fontsize=10)
ax[1].imshow(edges1, cmap='gray')
ax[1].set_title(r'Canny filter, $\sigma=1$', fontsize=10)
ax[2].imshow(edges2, cmap='gray')
ax[2].set_title(r'Canny filter, $\sigma=3$', fontsize=10)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
fig.savefig(my_path + '/leaf2-Canny_Edge_detection.png')