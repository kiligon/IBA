from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, diameter, high):
        self.h = high
        self.dia = diameter
        self.__area = self.make_area(self.dia, self.h)

    def __setattr__(self, attr, value):
        if attr in ('dia', 'h', '_Cylinder__area'):
            if attr == '_Cylinder__area':
                self.__dict__[attr] = self.make_area(self.dia, self.h)
            else:
                self.__dict__[attr] = value
                if 'dia' in self.__dict__.keys() and 'h' in self.__dict__.keys():
                    self.__dict__['_Cylinder__area'] = self.make_area(self.dia, self.h)
        else:
            raise AttributeError
