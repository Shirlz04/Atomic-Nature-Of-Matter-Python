import luminance
import stdarray
import stdio
import sys
from blob import Blob
import contextlib
with contextlib.redirect_stdout(None):  # noqa
    import pygame
from picture import Picture


class BlobFinder:
    """
    A data type for identifying blobs in a picture.
    """

    def __init__(self, pic, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        # Initialize an empty list for the blobs in pic.
        self._blobs = []
        # Create a 2D list of booleans called marked, having the same
        # dimensions as pic.
        marked = stdarray.create2D(pic.width(), pic.height(), False)
        # Enumerate the pixels of pic, and for each pixel (i, j):
        # 1. Create a Blob object called blob.
        # 2. Call _findBlob() with the right arguments.
        # 3. Add blob to _blobs if it has a non-zero mass.
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, i, j, marked, blob)
                if blob.mass() != 0:
                    self._blobs.append(blob)

    def _findBlob(self, pic, tau, i, j, marked, blob):
        """
        Identifies a blob using depth-first search. The parameters are
        the picture (pic), luminance threshold (tau), pixel column (i),
        pixel row (j), 2D boolean matrix (marked), and the blob being
        identified (blob).
        """
        if i < 0 or i >= pic.width():
            return
        if j < 0 or j >= pic.height():
            return
        if marked[i][j] is True:
            return
        if luminance.luminance(pic.get(i, j)) < tau:
            return
        marked[i][j] = True
        blob.add(i, j)
        self._findBlob(pic, tau, i-1, j, marked, blob)
        self._findBlob(pic, tau, i, j+1, marked, blob)
        self._findBlob(pic, tau, i, j-1, marked, blob)
        self._findBlob(pic, tau, i+1, j, marked, blob)

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """

        a = []
        for b in self._blobs:
            if b.mass() >= P:
                a.append(b)
        return a


# Takes an integer P, a float tau, and the name of a JPEG file as
# command-line arguments; writes out all of the beads with at least P
# pixels; and then writes out all of the blobs (beads with at least 1 pixel).
def _main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    find = BlobFinder(Picture(sys.argv[3]), tau)
    beads = find.getBeads(P)
    beads2 = find.getBeads(1)
    stdio.writeln(str(len(beads)) + ' Beads:')
    for i in beads:
        stdio.writeln(str(i))
    stdio.writeln(str(len(beads2)) + ' Blobs:')
    for b in beads2:
        stdio.writeln(str(b))


if __name__ == '__main__':
    _main()
