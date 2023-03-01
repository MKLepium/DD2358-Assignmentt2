import time
import array
import numpy as np
from pyrsistent import s


def stream_python_list(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = [1.0] * STREAM_ARRAY_SIZE
    b = [2.0] * STREAM_ARRAY_SIZE
    c = [0.0] * STREAM_ARRAY_SIZE
    scalar = 2.0

    times = [0.0] * 4

    # copy
    times[0] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = time.time() - times[0]

    # scale
    times[1] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = time.time() - times[1]

    # sum
    times[2] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = time.time() - times[2]

    # triad
    times[3] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = time.time() - times[3]

    return times


def stream_array(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = array.array(STREAM_ARRAY_TYPE, [1.0] * STREAM_ARRAY_SIZE)
    b = array.array(STREAM_ARRAY_TYPE, [2.0] * STREAM_ARRAY_SIZE)
    c = array.array(STREAM_ARRAY_TYPE, [0.0] * STREAM_ARRAY_SIZE)
    scalar = 2.0

    times = [0.0] * 4

    # copy
    times[0] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]
    times[0] = time.time() - times[0]

    # scale
    times[1] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        b[j] = scalar*c[j]
    times[1] = time.time() - times[1]

    # sum
    times[2] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        c[j] = a[j]+b[j]
    times[2] = time.time() - times[2]

    # triad
    times[3] = time.time()
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = b[j]+scalar*c[j]
    times[3] = time.time() - times[3]

    return times


def stream_numpy(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    a = np.ones(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    b = np.ones(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE) * 2
    c = np.zeros(STREAM_ARRAY_SIZE, dtype=STREAM_ARRAY_TYPE)
    scalar = 2.0

    times = [0.0] * 4

    # copy
    times[0] = time.time()
    c = a.copy()
    times[0] = time.time() - times[0]

    # scale
    times[1] = time.time()
    b = scalar * c
    times[1] = time.time() - times[1]

    # sum
    times[2] = time.time()
    c = a + b
    times[2] = time.time() - times[2]

    # triad
    times[3] = time.time()
    a = b + scalar * c
    times[3] = time.time() - times[3]

    return times


def main(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE):
    times_python_list = stream_python_list(
        STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)
    times_array = stream_array(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)
    times_numpy = stream_numpy(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)

    print("Python list: ", times_python_list)
    print("Array: ", times_array)
    print("Numpy: ", times_numpy)
    return (times_python_list, times_array, times_numpy)


# Without Cython:
#  real    0m10.768s
#  user    0m10.276s
#  sys     0m2.168s
# With Cython (no type declarations):
#  real    0m9.435s
#  user    0m9.118s
#  sys     0m1.736s


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    labels = ["copy", "scale", "sum", "triad"]
    bandwith_copy_python_list = []
    bandwith_scale_python_list = []
    bandwith_sum_python_list = []
    bandwith_triad_python_list = []
    bandwith_copy_array = []
    bandwith_scale_array = []
    bandwith_sum_array = []
    bandwith_triad_array = []
    bandwith_copy_numpy = []
    bandwith_scale_numpy = []
    bandwith_sum_numpy = []
    bandwith_triad_numpy = []
    STREAM_ARRAY_SIZE = 10000
    STREAM_ARRAY_TYPE = 'd'

    while STREAM_ARRAY_SIZE < 100000000:
        times = main(STREAM_ARRAY_TYPE, STREAM_ARRAY_SIZE)
    # 
        c = STREAM_ARRAY_SIZE
        # calculate MB/s for each operation
        array_types = [list, array.array, np.ndarray]
        d = 1
        import sys
        for t in times:
            for i in range(len(t)):
                t[i] = (2 * sys.getsizeof(array_types[d]) * STREAM_ARRAY_SIZE / 2**20) / t[i]
        # plot
        for index, t in enumerate(times):
            if index == 0:
                bandwith_copy_python_list.append(t[0])
                bandwith_scale_python_list.append(t[1])
                bandwith_sum_python_list.append(t[2])
                bandwith_triad_python_list.append(t[3])
            elif index == 1:
                bandwith_copy_array.append(t[0])
                bandwith_scale_array.append(t[1])
                bandwith_sum_array.append(t[2])
                bandwith_triad_array.append(t[3])
            else:
                bandwith_copy_numpy.append(t[0])
                bandwith_scale_numpy.append(t[1])
                bandwith_sum_numpy.append(t[2])
                bandwith_triad_numpy.append(t[3])
        print("STREAM_ARRAY_SIZE: ", STREAM_ARRAY_SIZE)
        STREAM_ARRAY_SIZE *= 10
        
    # plot by different implementations
    plt.plot(bandwith_copy_python_list, label="copy_python_list")
    plt.plot(bandwith_scale_python_list, label="scale_python_list")
    plt.plot(bandwith_sum_python_list, label="sum_python_list")
    plt.plot(bandwith_triad_python_list, label="triad_python_list")
    # add labels
    plt.xlabel("STREAM_ARRAY_SIZE, 10^8")
    plt.ylabel("Bandwith (MB/s)")
    plt.title("Bandwith Python list")
    plt.legend()
    plt.savefig("bandwith_Python_list.png")
    plt.clf()

    # plot by different operations
    plt.plot(bandwith_copy_array, label="copy_array")
    plt.plot(bandwith_scale_array, label="scale_array")
    plt.plot(bandwith_sum_array, label="sum_array")
    plt.plot(bandwith_triad_array, label="triad_array")
    plt.xlabel("STREAM_ARRAY_SIZE, 10^8")
    plt.ylabel("Bandwith (MB/s)")
    plt.title("Bandwith Python array")
    plt.legend()
    plt.savefig("bandwith_python_array.png")
    plt.clf()



    plt.plot(bandwith_copy_numpy, label="copy_numpy")
    plt.plot(bandwith_scale_numpy, label="scale_numpy")
    plt.plot(bandwith_sum_numpy, label="sum_numpy")
    plt.plot(bandwith_triad_numpy, label="triad_numpy")
    plt.xlabel("STREAM_ARRAY_SIZE, 10^8")
    plt.ylabel("Bandwith (MB/s)")
    plt.title("Bandwith Numpy")
    plt.legend()
    plt.savefig("bandwith_numpy.png")
    plt.clf()



# Plot the bandwidth results varying the arrays' size. Answer the question: how does the bandwidth measured with Cython code compare to bandwidth obtained in Assignment II.
# 