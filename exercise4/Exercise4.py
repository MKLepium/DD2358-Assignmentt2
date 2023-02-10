import numpy as np
import time

DGEMM_ARRAY_TYPE = 'd'

def dgemm_numpy(DGEMM_ARRAY_SIZE):
    a = np.ones((DGEMM_ARRAY_SIZE, DGEMM_ARRAY_SIZE), dtype=DGEMM_ARRAY_TYPE)
    b = np.ones((DGEMM_ARRAY_SIZE, DGEMM_ARRAY_SIZE), dtype=DGEMM_ARRAY_TYPE) * 2
    c = a.dot(b)

    return c

def dgemm_array(DGEMM_ARRAY_SIZE):
    import array
    a = array.array(DGEMM_ARRAY_TYPE, [1.0] * DGEMM_ARRAY_SIZE * DGEMM_ARRAY_SIZE)
    b = array.array(DGEMM_ARRAY_TYPE, [2.0] * DGEMM_ARRAY_SIZE * DGEMM_ARRAY_SIZE)
    c = array.array(DGEMM_ARRAY_TYPE, [0.0] * DGEMM_ARRAY_SIZE * DGEMM_ARRAY_SIZE)

    for i in range(DGEMM_ARRAY_SIZE):
        for j in range(DGEMM_ARRAY_SIZE):
            for k in range(DGEMM_ARRAY_SIZE):
                c[i*DGEMM_ARRAY_SIZE+j] += a[i*DGEMM_ARRAY_SIZE+k] * b[k*DGEMM_ARRAY_SIZE+j]

    return c



def dgemm_list(DGEMM_ARRAY_SIZE):
    a = [[1.0] * DGEMM_ARRAY_SIZE for i in range(DGEMM_ARRAY_SIZE)]
    b = [[2.0] * DGEMM_ARRAY_SIZE for i in range(DGEMM_ARRAY_SIZE)]
    c = [[0.0] * DGEMM_ARRAY_SIZE for i in range(DGEMM_ARRAY_SIZE)]

    for i in range(DGEMM_ARRAY_SIZE):
        for j in range(DGEMM_ARRAY_SIZE):
            for k in range(DGEMM_ARRAY_SIZE):
                c[i][j] += a[i][k] * b[k][j]

    return c


def time_dgemm(array_size):
    inner_times = []
    start = time.time()
    dgemm_numpy(array_size)
    end = time.time()
    inner_times.append(end - start)
    #print("Numpy time: ", end - start)
    

    start = time.time()
    dgemm_list(array_size)
    end = time.time()
    inner_times.append(end - start)
    #print("List time: ", end - start)

    start = time.time()
    dgemm_array(array_size)
    end = time.time()
    inner_times.append(end - start)
    #print("Array time: ", end - start)
    return inner_times

def main():

    array_size = 50
    for i in range(4):
        times = []
        for j in range(10):
            times.append(time_dgemm(array_size))
        print("Average time for array size: ", array_size)
        print("Numpy average time: ", sum(times[0])/len(times[0]))
        print("List average time: ", sum(times[1])/len(times[1]))
        print("Array average time: ", sum(times[2])/len(times[2]))
        print("Numpy standard deviation: ", np.std(times[0]))
        print("List standard deviation: ", np.std(times[1]))
        print("Array standard deviation: ", np.std(times[2]))
        array_size += 50


    

if __name__ == "__main__":
    main()
