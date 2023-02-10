# time the dft funcion witth different input sizes from 8 to 1024 elemens and plot it

import numpy as np
import matplotlib.pyplot as plt
import time
import dft

def time_dft(array_size):
    inner_times = []
    start = time.time()
    # call dft function with the correct parameters
    """
        Parameters:
    xr: real part of input
    xi: imaginary part of input
    Xr_o: real part of output
    Xi_o: imaginary part of output
    N: length of input"""
    dft.dft(np.random.rand(array_size), np.random.rand(array_size), np.random.rand(array_size), np.random.rand(array_size), array_size)
    end = time.time()
    inner_times.append(end - start)
    #print("Numpy time: ", end - start)
    
    return inner_times

def main():
    array_sizes = np.arange(8, 1024, 8)
    times = []
    for array_size in array_sizes:
        times.append(time_dft(array_size))

    plt.plot(array_sizes, times)
    plt.xlabel("Array size")
    plt.ylabel("Time")
    # save the plot as a png file
    plt.savefig("dft_time.png")

if __name__ == "__main__":
    main()

