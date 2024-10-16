# Canny Edge Detector - Skimage
 - [Scikit-image documentation](https://scikit-image.org/docs/stable/)
 - Using `pip install scikit-image` / `brew install scikit-image` to start
 - If interested can also take a look at opencv-python (OpenCV), however skimage is much lighter and easy to use for relatively simple tasks.
## Input leaf pictures downloaded from Moodle page:
[Link to BIOS3036 Moodle Page](https://moodle.nottingham.ac.uk/mod/resource/view.php?id=7625549)
## Parameters
*Sigma* -> sigma plays the role of a scale parameter for the edges: large values of sigma produce coarser scale edges and small values of sigma produce finer scale edges. Larger values of sigma also result in greater noise suppression.\
\
*Mode* -> add `mode='L'` after import image path to make sure the input image is a single channel image - normally interpreted as greyscale.
## Output: 
![Leaf1](https://github.com/Haru-Tachibana/Canny-Edge-Detector---Skimage/blob/main/Output%20figures/leaf1-Canny_Edge_detection.png)
![Leaf2](https://github.com/Haru-Tachibana/Canny-Edge-Detector---Skimage/blob/main/Output%20figures/leaf2-Canny_Edge_detection.png)
