"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
Author: Mahesh Venkitachalam
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Cleared off the code

ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def update(grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    # create a 2D array of indices to compute neighbors
    # using numpy.roll to handle toroidal boundary conditions
    indices = np.arange(N)
    ii, jj = np.meshgrid(indices, indices, indexing="ij")
    neighbor_sum = (
        # I had an issue in this, it was a nightmare to debug :'(
        np.roll(grid, 1, axis=0)
        + np.roll(grid, -1, axis=0)
        + np.roll(grid, 1, axis=1)
        + np.roll(grid, -1, axis=1)
        + np.roll(np.roll(grid, 1, axis=0), 1, axis=1)
        + np.roll(np.roll(grid, -1, axis=0), 1, axis=1)
        + np.roll(np.roll(grid, 1, axis=0), -1, axis=1)
        + np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    )
    # compute neighbor_sum on toroidal surface
    total = (
        neighbor_sum[ii, (jj - 1) % N]
        + neighbor_sum[ii, (jj + 1) % N]
        + neighbor_sum[(ii - 1) % N, jj]
        + neighbor_sum[(ii + 1) % N, jj]
        + neighbor_sum[(ii - 1) % N, (jj - 1) % N]
        + neighbor_sum[(ii - 1) % N, (jj + 1) % N]
        + neighbor_sum[(ii + 1) % N, (jj - 1) % N]
        + neighbor_sum[(ii + 1) % N, (jj + 1) % N]
    )
    # apply Conway's rules
    newGrid[(grid == ON) & ((total < 2) | (total > 3))] = OFF
    newGrid[(grid == OFF) & (total == 3)] = ON
    grid[:] = newGrid[:]
    return grid


def old_update(grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int(
                (
                    grid[i, (j - 1) % N]
                    + grid[i, (j + 1) % N]
                    + grid[(i - 1) % N, j]
                    + grid[(i + 1) % N, j]
                    + grid[(i - 1) % N, (j - 1) % N]
                    + grid[(i - 1) % N, (j + 1) % N]
                    + grid[(i + 1) % N, (j - 1) % N]
                    + grid[(i + 1) % N, (j + 1) % N]
                )
                / 255
            )
            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    grid[:] = newGrid[:]
    return grid


# main() function


def run_N_times(numIter, grid, grid_size):
    """Run the simulation for N iterations for this grid size"""
    for _ in range(numIter):
        grid = update(grid, grid_size)


def main():

    # fixed number of iterations
    numIter = 1000
    gridSize = 10
    # I am just always gonna use a random grid
    times = []
    import time

    # run it until 640x640
    gridSizes = []
    while gridSize < 321:
        gridSize = gridSize * 2
        gridSizes.append(gridSize)
        print("Grid Size: ", gridSize)
        grid = randomGrid(gridSize)
        start = time.time()
        run_N_times(numIter, grid, gridSize)
        end = time.time()
        times.append(end - start)
        print("Grid Size: ", gridSize, "Time: ", end - start)
    import matplotlib.pyplot as plt

    plt.plot(gridSizes, times, label="Numpy")
    plt.xlabel("N-Board Size")
    plt.ylabel("Time")
    plt.title("Time Complexity of Conway's Game of Life")
    plt.legend()
    plt.savefig("conwayNumpy.png")


# call main
if __name__ == "__main__":
    main()
