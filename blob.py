import stdio
import math
import sys


class Blob:
    """
    Represents a blob.
    """

    def __init__(self):
        """
        Constructs an empty blob.
        """
        self._P = 0
        self._x = 0.0
        self._y = 0.0

    def add(self, i, j):
        """
        Adds pixel (i, j) to this blob.
        """
        if self._P == 0:
            self._x = i
            self._y = j
            self._P += 1
        else:
            cal = (self._x * (self._P))
            xa = (cal + i)/(self._P+1)
            self._x = xa
            ya = ((self._y * (self._P)) + j)/(self._P+1)
            self._y = ya
            self._P += 1

    def mass(self):
        """
        Returns the number of pixels added to this blob, ie, its mass.
        """

        return self._P

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between the center of mass of this blob
        and the center of mass of other blob.
        """

        cal1 = (self._x - other._x) ** 2
        cal2 = (self._y - other._y) ** 2
        total = cal1 + cal2
        d = math.sqrt(total)
        return d

    def __str__(self):
        """
        Returns a string representation of this blob.
        """

        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)


def _main():
    blob = Blob()
    blob.add(0, 1)
    blob.add(1, 1)
    blob.add(2, 2)
    print(str(blob))


if __name__ == '__main__':
    _main()
