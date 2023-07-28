# image-difference
Python program that converts 2 images into a tensor and finds the difference between them by subtracting them. Useful for before and after photos. The difference is calculated via a number scale, where "0" means there is no difference between the 2 images. 

To run the program, make sure you have streamlit installed on a python environment. Then, in that environment in a terminal, type "streamlit run imgDiff.py". This will bring up a new tab in your default browser and will show you a dataframe/table of each image pair and its difference scale number. 

In the images folder, each folder has a pair of images. These images are refered to as "pre" and "post". The difference between the two images is calculated by taking the "pre" image and subtracting it from the "post" image. 

There are some example images in the program, but you can you use your own. All you need to do is get your "pre" and "post" images. Then, name the files "pre" and "post" accordingly. Finally, put both of the images in a new folder in "images". The folder should be named "img_pair_#", where # is the index. Everytime you add a new image, make sure folder names start from 1 and so on.

Make sure that the "pre" and "post" images are the same resolution. It is recommended to have both images at a lower resolution than normal for a more generalized difference number (but not too low!)
