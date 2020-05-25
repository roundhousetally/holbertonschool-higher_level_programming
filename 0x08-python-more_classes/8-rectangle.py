#!/usr/bin/python3
""" Full Rectangle """


class Rectangle:
    """ Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ private attribute
        Args:
             width and height of a rect
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """ area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter """
        b = ""
        if self.__width is 0 or self.__height is 0:
            return (b)
        else:
            return((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the rectangle with the largest area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """ to print """
        b = ""
        if self.__width is 0 or self.__height is 0:
            return (b)
        for i in range(self.__height):
            b += str(self.print_symbol) * self.__width
            if i < (self.__height - 1):
                b += "\n"
        return (b)

    def __repr__(self):
        """ string rep of rectangle """
        return ('Rectangle({:d}, {:d})'.format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height var of rect class """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ retreive width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width var of rect class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
