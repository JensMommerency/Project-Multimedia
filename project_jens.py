"""
Author: Jens Mommerency
        Pieter Gillis
Year: 2018
Project Multimedia
"""

import cv2
import numpy as np

print("test")
#----------------------FUNCTIONS-----------------------------------------------#
def get_hog(image):
    # winSize = (64,64)
    winSize = (image.shape[1], image.shape[0])
    blockSize = (8,8)
    # blockSize = (16,16)
    blockStride = (8,8)
    cellSize = (8,8)
    nbins = 9
    derivAperture = 1
    winSigma = 4.
    histogramNormType = 0
    L2HysThreshold = 2.0000000000000001e-01
    gammaCorrection = 0
    nlevels = 64
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
                            histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
    #compute(img[, winStride[, padding[, locations]]]) -> descriptors
    winStride = (8,8)
    padding = (8,8)
    locations = [] # (10, 10)# ((10,20),)
    hist = hog.compute(image,winStride,padding,locations)
    print(hist.shape)

#------------------------------------------------------------------------------#
