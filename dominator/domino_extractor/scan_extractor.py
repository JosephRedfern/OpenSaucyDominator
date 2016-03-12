from dominator.segmentation.threshold import ThresholdSegmentation
import numpy as np
from matplotlib import pyplot as plt
import cv2


class ScanExtractor(object):

    def __init__(self, scene_path):
        self.image = cv2.imread(scene_path)

    def process(self):
        thresholder = ThresholdSegmentation(~self.image, 200, thresh_type='GRAYSCALE')
        image, mask = thresholder.segment_image()

        mask *= 255

        kernel = np.ones((50,50),np.uint8)
        morphed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel=kernel)

        labelCount, labelledMask = cv2.connectedComponents(morphed)

        counts = np.bincount(labelledMask[labelledMask!=0])
        maxIndex = counts.argmax()

        labelledMask[labelledMask!=maxIndex] = 0
        labelledMask[labelledMask==maxIndex] = 255

        labelledMask = labelledMask.astype(np.uint8)

        cv2.imshow('max', cv2.resize(labelledMask.astype(np.uint8), (300, 400)))

        rows = []
        widths = []

        for row in labelledMask:
            res = np.where(row==255)
            leftPos = res[0][0] if len(res[0]) > 1 else res[0] if res[0] != [] else -1
            rightPos = res[0][-1] if len(res[0]) > 1 else res[0] if res[0] != [] else -1

            widths.append(rightPos-leftPos)

            rows.append((leftPos, rightPos))

        hist, _ = np.histogram(widths)

        plt.plot(hist)

        # plt.plot(rows)
        plt.show()

        cv2.waitKey(0)

if __name__ == '__main__':
    ScanExtractor('../tests/data/image/IMG_4584.JPG').process()