from dominator.segmentation.threshold import ThresholdSegmentation
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import argrelextrema
import cv2
import math


class ScanExtractor(object):

    def __init__(self, scene_path):
        self.image = cv2.imread(scene_path)

        cv2.imshow('Input Image', cv2.resize(self.image.astype(np.uint8), (450, 600)))

    def process(self):
        thresholder = ThresholdSegmentation(~self.image, 220, thresh_type='GRAYSCALE')
        image, mask = thresholder.segment_image()

        mask *= 255

        kernel = np.ones((80,80),np.uint8)
        morphed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel=kernel)

        labelCount, labelledMask = cv2.connectedComponents(morphed)

        counts = np.bincount(labelledMask[labelledMask!=0])
        maxIndex = counts.argmax()

        labelledMask[labelledMask!=maxIndex] = 0
        labelledMask[labelledMask==maxIndex] = 255

        labelledMask = labelledMask.astype(np.uint8)

        cv2.imshow('max', cv2.resize(labelledMask.astype(np.uint8), (450, 600)))

        rows = []
        widths = []

        for row in labelledMask:
            res = np.where(row==255)
            leftPos = res[0][0] if len(res[0]) > 1 else res[0] if len(res[0]) != 0 else -1
            width = np.where(row[leftPos:] == 0)

            width = width[0][0] if len(width[0]) > 1 else width[0] if len(width[0]) != 0 else -1
            rightPos = leftPos + width
            widths.append(rightPos-leftPos)
            rows.append((leftPos, rightPos))

        hist, bins = np.histogram(widths)
        peaks = argrelextrema(hist, np.greater)

        min_peak = peaks[0][0] if len(peaks[0]) > 1 else peaks[0]
        width = int(round(bins[min_peak]))

        height = width*2

        print "First peak is at: {0}, with value {1}".format(min_peak, bins[min_peak])
        print "Estimated Domino Dimensions: {0}x{1}px".format(width, height)

        annotated = self.image.copy()

        cv2.rectangle(annotated, (0, 0), (width, height), (255, 0, 0), 5)
        cv2.imshow('annotated', cv2.resize(annotated, (450, 600)))

        plt.plot(hist)

        #plt.plot(rows)
        plt.show()

        cv2.waitKey(0)

if __name__ == '__main__':
     ScanExtractor('/Users/joe/Downloads/IMG_4588.JPG').process()
    #ScanExtractor('/Users/joe/Downloads/potato.png').process()