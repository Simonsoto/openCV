###########
## load the images

import argparse
import cv2

#Construct the argument parser and parse the arguments

ap = argparse.ArgumentParser(description = 'Load an image and display it')

ap.add_argument('-i', '--image', required = True, 
	help = 'path to input image')
args = vars(ap.parse_args())



## Load the image from the disk via "cv2.imread()" and then grab
## the spatial dimensions. Including width, height, number of channels.

image  = cv2.imread(args['image'])
(h,w,c) = image.shape[:3]

#display the information about the picture

print("widht: {} pixels,\n height: {} pixels, \n channels:{}".format(w,h,c))

# show the image and wait for a keypress
cv2.imshow('Image', image)
cv2.waitKey(0)

# Save the image again in the disk

cv2.imwrite('newimage.jpg', image)