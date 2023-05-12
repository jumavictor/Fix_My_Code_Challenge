#!/usr/bin/python3

class Square:
    def __init__(self, side=0):
        self.side = side

    def area(self):
        """ Calculate the area of the square """
        return self.side ** 2

    def perimeter(self):
        """ Calculate the perimeter of the square """
        return 4 * self.side

    def __str__(self):
        return "{} x {}".format(self.side, self.side)

if __name__ == "__main__":
    s = Square(side=10)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

