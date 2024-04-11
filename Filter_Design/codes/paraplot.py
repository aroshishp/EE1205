def add(x, y):
    """
    This function adds two polynomials defined by vectors x and y.
    :param x: List representing the first polynomial coefficients
    :param y: List representing the second polynomial coefficients
    :return: List representing the sum of the two polynomials
    """
    m = len(x)
    n = len(y)

    if m == n:
        z = [a + b for a, b in zip(x, y)]
    elif m > n:
        z = [a + b for a, b in zip(x, [0] * (m - n) + y)]
    else:
        z = [a + b for a, b in zip([0] * (n - m) + x, y)]

    return z

import numpy as np

def polypower(v, N):
    """
    This function raises a polynomial defined by coefficients v to the power of N.
    :param v: List representing the polynomial coefficients
    :param N: Integer representing the power to which the polynomial is raised
    :return: List representing the coefficients of the resulting polynomial
    """
    y = [1]

    if N > 0:
        for i in range(N):
            y = np.convolve(y, v).tolist()

    return y

def bilin(p, om):
    """
    This function transforms the stable bandpass filter obtained
    from the Chebyschev approximation to the equivalent bandpass
    digital filter using the bilinear transformation.
    """
    N = len(p)
    const = [-1, 1]
    v = [1]

    if N > 2:
        for i in range(N - 1):
            v = np.convolve(v, const).tolist()
            v = add(v, np.array(p[i+1]) * np.array(polypower([1, 1], i)))

        digden = v

    elif N == 2:
        M = len(v)
        v[M - 1] = v[M - 1] + p[N - 1]
        v[M] = v[M] + p[N - 1]
        digden = v

    else:
        digden = p

    dignum = polypower([-1, 0, 1], (N - 1) // 2)
    G_bp = np.abs(np.polyval(digden, np.exp(-1j * om)) / np.polyval(dignum, np.exp(-1j * om)))

    return dignum, digden, G_bp