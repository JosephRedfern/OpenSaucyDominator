# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:59:39 2016

@author: kaelon
"""
import numpy as np
import cv2
import sys

class ThresholdSegmentation():

    THRESHOLD_TYPES = (None,
                       'GRAYSCALE',)

    def __init__(self, image, threshold, thresh_type=None):
        ''' The ThresholdSegmentation class is used to remove all pixels
        within an image that fall below a specified threshold'''
        assert image.dtype == np.uint8, "Expected uint8, m8!, you gave us {0}".format(image.dtype)
        assert type(threshold) is int
        assert thresh_type in ThresholdSegmentation.THRESHOLD_TYPES

        self.threshold_type = thresh_type
        self.image = image
        self.threshold = threshold

        self.preprocess_image()

    def preprocess_image(self):
        if self.threshold_type == 'GRAYSCALE':
            assert self.image.ndim == 3
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def segment_image(self):
        ''' Segments an image using a thresholding appraoch'''
        binary = self.binary_mask()
        
        seg_img = self.image.copy()
        seg_img[binary == 0] = 0 
        
        return seg_img, binary
    
    def binary_mask(self):
        ''' Obtains a binary mask using a thresholding approach'''
        binary = self.image.copy()
        binary[binary < self.threshold] = 0
        binary[binary != 0] = 1
        
        return binary 
        
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1])
    else:
        img = (np.random.rand(100,100, 3) * 255).astype(np.uint8)

    ts = ThresholdSegmentation(img, 128, thresh_type='GRAYSCALE')
    seg_img, _ = ts.segment_image()    
    
    plt.figure('ThresholdSegmentation Example')
    plt.subplot(1, 2, 1)
    plt.imshow(img, interpolation='none')
    plt.subplot(1, 2, 2)
    plt.imshow(seg_img, interpolation='none')
    plt.colorbar()

    plt.show()
