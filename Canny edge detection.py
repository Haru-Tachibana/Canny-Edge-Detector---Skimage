import matplotlib.pyplot as plt
import numpy as np 

from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray
from skimage.exposure import histogram, cumulative_distribution
from skimage.filters import threshold_otsu
from skimage import feature

import os


my_path = os.path.abspath('/Users/yangyangxiayule/Documents/GitHub/Canny-Edge-Detector---Skimage/Output figures')

leaf1 = imread('/Users/yangyangxiayule/Documents/GitHub/Canny-Edge-Detector---Skimage/Input figures/leaf1.jpg', mode='L')
leaf2 = imread('/Users/yangyangxiayule/Documents/GitHub/Canny-Edge-Detector---Skimage/Input figures/leaf2.jpg', mode='L')

edges1_leaf1 = feature.canny(leaf1)
edges2_leaf1 = feature.canny(leaf1, sigma=3)

edges1_leaf2 = feature.canny(leaf2)
edges2_leaf2 = feature.canny(leaf2, sigma=3)

#leaf1
fig1, ax1 = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax1[0].imshow(leaf1, cmap='gray')
ax1[0].set_title('Leaf1 Gray Image', fontsize=10)
ax1[1].imshow(edges1_leaf1, cmap='gray')
ax1[1].set_title(r'Canny filter, $\sigma=1$', fontsize=10)
ax1[2].imshow(edges2_leaf1, cmap='gray')
ax1[2].set_title(r'Canny filter, $\sigma=3$', fontsize=10)

#leaf2
fig2, ax2 = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax2[0].imshow(leaf2, cmap='gray')
ax2[0].set_title('Leaf2 Gray Image', fontsize=10)
ax2[1].imshow(edges1_leaf2, cmap='gray')
ax2[1].set_title(r'Canny filter, $\sigma=1$', fontsize=10)
ax2[2].imshow(edges2_leaf2, cmap='gray')
ax2[2].set_title(r'Canny filter, $\sigma=3$', fontsize=10)


for a in ax1:
    a.axis('off')

for a in ax2:
    a.axis('off')


fig1.tight_layout()
fig2.tight_layout()

#optional show plots
fig1.show()
fig2.show()

fig1.savefig(my_path + '/leaf1-Canny_Edge_detection.png')
fig2.savefig(my_path + '/leaf2-Canny_Edge_detection.png')