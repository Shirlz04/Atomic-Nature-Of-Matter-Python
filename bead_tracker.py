import stdio
import sys
from blob_finder import BlobFinder
import contextlib
with contextlib.redirect_stdout(None):  # noqa
    import pygame
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).

def main():
    P, tau, delta = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    closest = delta + 1
    answers = []
    find = BlobFinder(Picture(sys.argv[4]), tau)
    prevBeads = find.getBeads(P)
    for i in sys.argv[5:]:
        find1 = BlobFinder(Picture(i), tau)
        currBeads = find1.getBeads(P)
        for c in range(len(currBeads)):
            for a in prevBeads:
                cal = currBeads[c].distanceTo(a)
                if cal <= delta and cal < closest:
                    closest = round(cal, 4)
            if closest != delta + 1:
                stdio.writef('%.4f\n', closest)
            closest = delta + 1
        prevBeads = currBeads
        stdio.writeln()


if __name__ == '__main__':
    main()
