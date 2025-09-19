# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:46:07 2022

@author: Asus
"""

import cv2 as cv
import numpy as np

img = cv.imread("./images/park.jpg")
cv.imshow('Park', img)
print(img.shape)

def threshold_otsu_impl(image , nbins = 0.01):

    if len(image.shape) == 1 and len(image.shape)>2:
        print("coloured image")
        return

    if np.min(image) == np.max(image):
        print("should have multiple colours")
        return

    all_colors = image.flatten()
    total_len = len(all_colors)
    least_variance = -1
    least_variance_threshold = -1
    print(len(image))
    print(total_len)
    color_thresholds = np.arange(np.min(image)+nbins, np.max(image)-nbins, nbins)

    for color_threshold in color_thresholds:
        bg_pixels = all_colors[all_colors < color_threshold]
        weight_bg = len(bg_pixels)/total_len
        variance_bg = np.var(bg_pixels)
        #print(len(bg_pixels), weight_bg, variance_bg)

        fg_pixels = all_colors[all_colors >= color_threshold]
        weight_fg = len(fg_pixels)/total_len
        variance_fg = np.var(fg_pixels)

        within_class_variance = weight_fg*variance_fg + weight_bg*variance_bg
        if least_variance == -1 or least_variance > within_class_variance:
            least_variance = within_class_variance
            least_variance_threshold = color_threshold

        #print("trace:", within_class_variance, color_threshold)

    return least_variance_threshold











# Converting to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

num = threshold_otsu_impl(gray)
print(num)

# Blur image
#blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

# Edge Cascade
#canny = cv.Canny(blur, 125, 175)
#cv.imshow("Edge",canny)

# Dilating the image
#dilated = cv.dilate(canny,(7,7),iterations = 3)
#cv.imshow('Dilated',dilated)

# eroding
#eroded = cv.erode(dilated,(7,7),iterations = 3)
#cv.imshow('Eroded',eroded)

# Resizing the image
#resized = cv.resize(img,(500,500),interpolation = cv.INTER_CUBIC)
#cv.imshow('resized',resized)

# Cropping the image
#cropped = img[50:200, 200:800]
#cv.imshow('cropped',cropped)



cv.waitKey(0)