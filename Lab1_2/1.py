class Rectangle:
    def __init__(self, length_val = 1.0, width_val = 1.0):
        self.length = length_val
        self.width = width_val

    def __str__(self):
        return f'{self.__length} x {self.__width}'

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        if not isinstance(val, int | float):
            raise TypeError('Only types int and float allowed for lenght.')
        if (val <= 0 or val >= 20):
            raise ValueError('Invalid range.')
        self.__length = val

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int | float):
            raise TypeError('Only types int and float allowed for width.')
        if (val <= 0 or val >= 20):
            raise ValueError('Invalid range.')
        self.__width = val

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length + self.__width
