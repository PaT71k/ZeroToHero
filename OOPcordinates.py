class Line(object):

    def __init__(self ,coor1, coor2):
        self.mycoor1= coor1
        self.mycoor2= coor2

    def distance(self):
        x1, y1 = self.mycoor1
        x2, y2 = self.mycoor2
        return ((x2 - x1)**2 - (y2 - y1)**2)**0.5

    def slope(self):
        x1, x2 = self.mycoor1
        y1 , y2 = self.mycoor2
        return float((y2 - y1) / (x2 - x1))

x = 1
coor1 = (6 , 2)
coor2 = (11, 3)
pero = Line(coor1, coor2)
print( pero.distance())
print( pero.slope())



