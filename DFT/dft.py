"""DFT is a method to compute the Discrete Fourier Transform (DFT)
which converts a finite sequence of function samples (typically real numbers)
into samples of the discrete-time Fourier transform (DTF),
which is a complex-valued function of frequency.
"""


import math
import logging
logging.basicConfig(level=logging.INFO)
import numpy as np
@profile
def dft(x_r, x_i, xr_o, xi_o, n_n):
    """
    Discrete Fourier Transform

    Parameters:
    xr: real part of input
    xi: imaginary part of input
    Xr_o: real part of output
    Xi_o: imaginary part of output
    N: length of input
    """
    pi_2 = math.pi * 2
    #logging.info("Calculating DFT of {x_r}, {x_i}".format(x_r=x_r, x_i=x_i))
    for k in range(n_n):
        for j in range(n_n):
            xr_o[k] += x_r[j] * \
                math.cos(j * k * pi_2 / n_n) + x_i[j] * math.sin(j * k * pi_2 / n_n)
            xi_o[k] += -x_r[j] * \
                math.sin(j * k * pi_2 / n_n) + x_i[j] * math.cos(j * k * pi_2 / n_n)
    #logging.info("Result is {xr_o}, {xi_o}".format(xr_o=xr_o, xi_o=xi_o))


def test_DFT():
    array_size = 1024
    dft(np.random.rand(array_size), np.random.rand(array_size), np.random.rand(array_size), np.random.rand(array_size), array_size)

def main():
    test_DFT()

if __name__ == "__main__":
    main()

# 