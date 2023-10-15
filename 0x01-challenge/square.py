#!/usr/bin/python3

""" My square File """


class Square():
    """ Class Square """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ Initial Function """
        self.__width = width
        self.__height = height

    def area_of_my_square(self):
        """ Area of the square """
        return (self.__width * self.__height)

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ String Function """
        return ("{}/{}".format(self.__width, self.__height))


if __name__ == "__main__":
    """ Create Square """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
