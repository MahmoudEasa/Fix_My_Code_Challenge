#!/usr/bin/python3

""" My square File """


class Square():
    """ Class Square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        if args:
            self.width = args[0]
            self.height = args[1]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return (self.height * 4)

    def __str__(self):
        """ Str Function """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
