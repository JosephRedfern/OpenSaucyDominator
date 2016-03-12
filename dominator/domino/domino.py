# -*- coding: utf-8 -*-
"""
This class stores data regarding the type of domino used in game
"""

class Domino():

    def __init__(self, width, height):
        self.height = height
        self.width = width
    
        self.computeRatio()
        
        
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def computeRatio(self):
        self.ratio = float(self.height) / self.width
    
    def getWidthHeightRatio(self):
        return 1 / self.ratio

    def getHeightWidthRatio(self):
        return self.ratio        
    
    def getWidthFromHeight(self, height):
        return self.getWidthHeightRatio() * height

    def getHeightFromWidth(self, width):
        return self.getHeightWidthRatio() * width


if __name__ == '__main__':
    dom = Domino(10, 5)
    dom.computeRatio()

    print "The width is {0}".format(dom.width)    
    print "The height is {0}".format(dom.height)
    
    print "The height to width ratio is {0}".format(dom.getHeightWidthRatio())
    print "The width to height ratio is {0}".format(dom.getWidthHeightRatio())

    data = [[10, 5],
            [20, 10]]    
    
    for d in data:
        
        print "Given width of {0}, the calculated height is {1}".format(d[0], dom.getHeightFromWidth(d[0]))
        print "Given height of {0}, the calculated width is {1}".format(d[1], dom.getWidthFromHeight(d[1]))
        
    