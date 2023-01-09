import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    disp = stdio.readAllStrings()
    total = 0
    CONVERSION = 0.175e-6
    n = len(disp)
    for i in range(n):
        total += (float(disp[i]) * CONVERSION) ** 2
    var = total / (2 * n)
    eta = 9.135e-4
    rho = 0.5e-6
    T = 297
    R = 8.31457
    k = (6 * math.pi * var * eta * rho) / T
    N_A = R / k
    stdio.writef('Boltzman = %e\n', k)
    stdio.writef('Avogadro = %e\n', N_A)


if __name__ == '__main__':
    main()
