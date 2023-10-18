#!/usr/bin/python3
"""
My square File
"""


class Square():
    """ Class Square """

    def __init__(self, width=0, height=0):
        """ Initial Function """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("width most be an integer")

        if value <= 0:
            raise ValueError("width most be greater than 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for width """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("height most be an integer")

        if value <= 0:
            raise ValueError("height most be greater than 0")

        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return (self.__width * self.__height)

    def permiter_of_my_square(self):
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
