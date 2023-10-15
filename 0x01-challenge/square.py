#!/usr/bin/python3

""" My square File """


class Square():
    """ Class Square """

    def __init__(self, width=0, height=0):
        """ Initial Function """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.height)

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ String Function """
        return ("{}/{}".format(self.width, self.height))


if __name__ == "__main__":
    """ Create Square """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
