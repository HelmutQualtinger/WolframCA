""" The Wolfram one dimensional cellular automaton rule 30
    with colorization according to the number of neighbors in the previous line"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numba  # just in time compiler only works with python 3.11
import time


# calculate the whole screen
@numba.njit
def wolfram_CA(rule_number, size, steps):
    """_Calculate the whole cellular automaton array with the specified rule for the first 
    steps generations 
    Dont loop over the cells in Python use numpy vectorization and numba just in time compiler

    Args:
        rule_number (int): the wolfram rule number specifying which neighborhoods 
        give a live cell in the next generation
        size (_int_): _length of the one dimensional universe_
        steps ( int): number of generations remembered
    Returns:
        np.array: the cellular automaton array generated with the specified rule
    """
    # Initialize the cellular automaton array with a single live cell in the middle
    ca = np.zeros((steps, size), dtype=np.bool_)
    ca[0, size // 2] = True
    # Generate subsequent generations based on the specified rule
    for i in range(1, steps):
        can = np.zeros((size), dtype=np.bool_)   # create a new line as vector
        can[1:size-1] = (1 << (ca[i-1, 0:size-2] + (ca[i-1, 1:size-1] << 1)
                               + ((ca[i-1, 2:size] << 2)))) & rule_number
        ca[i] = can
    return ca


@numba.njit
def wolfram_CA_last_line(ca, rule_number, size, steps):
    """_summary_
    same as wolfram_CA but only calculates a new last line for interactive update of the image


    Args:
        ca ( np two dimensional array): input array, will be shifted up by one line last line will be overwritten with new values
        rule_number (int): Wolfram rule number
        size (_type_): _length of one dimensional universe
        steps (int): steps to remember

    Returns:
        np.arra(size,steps)_: updated cellular automaton array
    """
    ca[0:steps-1, :] = ca[1:, :]  # shift up by one line
    for i in range(steps-1, steps):  # only last line
        can = np.zeros((size), dtype=np.bool_)   # create a new line as vector
        can[1:size-1] = (1 << (ca[i-1, 0:size-2] + (ca[i-1, 1:size-1] << 1)
                         + ((ca[i-1, 2:size] << 2)))) & rule_number
        ca[i] = can
    return ca


@numba.njit
def color_wolfram_CA(ca):
    """_summary_
    Colorise the cellular automaton array according to the number of neighbors 
    to give prettier output

    Args:
        ca (ndarry (size,steps) :int8): array of the cellular automaton
    Returns:
       (ndarry (size,steps) :int64): array of the cellular automaton colorized according to the number of neighbors
    """
    # colorise according to neighbors, return colorized array
    cca = np.zeros((ca.shape[0], ca.shape[1]), dtype=np.int64)
    # Generate subsequent generations based on the specified rule
    for i in range(1, steps-1):
        for j in range(1, size - 1):
            cca[i, j] = np.sum(ca[i-1:i+2, j-1:j+2])
    return cca


@numba.njit
def color_wolfram_CA_last_line(ca, cca):
    """same as color_wolfram_CA but only calculates the last line used for interactive 
    update of the image

    Args:
        ca (ndarry (size,steps) :int64): array of the cellular automaton
    Returns:
       (ndarry (size,steps) :int64): array of the cellular automaton colorized according to the number of neighbors
    """
    # Colorise the cellular automaton array with the last line updated only
    cca[0:steps-1, :] = cca[1:, :]  # shift up by one line
    # Generate subsequent generations based on the specified rule
    for i in range(steps-3, steps):
        for j in range(1, size - 1):
            cca[i, j] = np.sum(ca[i-1:i+2, j-1:j+2])
    return cca


def update(frame):
    """ background update function for matplotlib calculating and showing the next generations ever so many millisecs

    Args:
        frame (_type_): _needs to be there for matplotlib FuncAnimation

    Returns:
       img: matplotlib image object
    """
    # coroutine executed in the mainloop of plt.show()

    # global variables are ugly but don't want to pass them around

    global img, ca, cca, rule_number, size, steps, fig, ax, generation

    # new generation with last line updated
    start_time = time.time()
    for i in range(10):   # go 5 generations at a time so that the animation is not too slow
        ca = wolfram_CA_last_line(ca, rule_number, size, steps)
    # recolorize according to neighbors
        cca = color_wolfram_CA_last_line(ca, cca)

        generation += 1
        print(generation)

    # update the image for matplotlib
    end_time = time.time()

    img.set_array(cca)
    ax.set_title(
        f"Rule {bin(rule_number)} Generation {generation} Time: {end_time-start_time:2.5f}")
    return img, ax


# Set the rule number (0 to 255) and other parameters

rule_number = 82
size = 401
steps = 200
generation = 1


fig, ax = plt.subplots(figsize=(12, 8))
plt.tight_layout()

# Generate and plot the complete cellular automaton om the whole screen
ca = wolfram_CA(rule_number, size, steps)
cca = color_wolfram_CA(ca)  # colorise according to number of neighbours
img = ax.imshow(cca, cmap="jet",  vmin=0, vmax=9)
ax.set_title(f'Rule {bin(rule_number)}')
ax.set_axis_off()

# start updating in the background
ani = animation.FuncAnimation(
    fig, update, interval=10, cache_frame_data=False)
plt.show()
