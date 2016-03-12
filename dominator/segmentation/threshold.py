# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:59:39 2016

@author: kaelon
"""
import numpy as np
import cv2
class ThresholdSegmentation():
 
    
    def __init__(self, image, threshold):
        ''' The ThresholdSegmentation class is used to remove all pixels
        within an image that fall below a specified threshold'''
        assert image.dtype == np.uint8, "Expected uint8, m8!, you gave us {0}".format(image.dtype)
        assert type(threshold) is int
        
        self.image = image
        self.threshold = threshold
        
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
    img = cv2.cvtColor(cv2.imread('potato.jpg'), cv2.COLOR_BGR2RGB)
    ts = ThresholdSegmentation(img, 128)
    seg_img, _ = ts.segment_image()    
    
    plt.figure('ThresholdSegmentation Example')
    plt.subplot(1, 2, 1)
    plt.imshow(img, interpolation='none')
    plt.subplot(1, 2, 2)
    plt.imshow(seg_img, interpolation='none')
    plt.colorbar()