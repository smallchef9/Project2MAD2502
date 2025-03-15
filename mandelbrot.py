import numpy as np
def get_escape_time(c: complex, max_iterations: int) -> int | None:
    ''' 
    Computes the escpate time of a complex value.
    Parameters are c: complex, and max_iterations: int
    Returns the number of iterations c passes before it escapes. 
    '''
    z = 0 + 0j 
    for k in range(max_iterations):
        z = z ** 2 + c
        if abs(z) > 2:
            return k
    return max_iterations


def get_escape_time_color_arr(
        c_arr: np.ndarray,
        max_iterations: int
) -> np.ndarray:
    """
    Computes the escape time color array for the given complex values.

    Parameters:
    c_arr (np.ndarray): A NumPy array of complex numbers representing the grid.
    max_iterations (int): The maximum number of iterations for the escape time calculation.

    Returns:
    np.ndarray: A NumPy array of the same shape as c_arr with color values in [0,1].
    """
    # Initialize an array to store the color values
    color_arr = np.zeros(c_arr.shape, dtype=np.float64)

    # Iterate through each element in the array
    for i in range(c_arr.shape[0]):
        for j in range(c_arr.shape[1]):
            escape_time = get_escape_time(c_arr[i, j], max_iterations)
            color_arr[i, j] = (max_iterations - escape_time + 1) / (max_iterations + 1)

    return color_arr


def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    ...

#calculate both components
    real_start = top_left.real
    real_end = bottom_right.real
    imag_start = top_left.imag
    imag_end = bottom_right.imag

# create arrays for real and imaginary parts
    real_values = np.arange(real_start, real_end, step)
    imag_values = np.arange(imag_start, imag_end, -step)

#grid dimensions
    rows = len(imag_values)
    cols = len(real_values)

#creating empty grip
    complex_grid = np.zeros((rows, cols), dtype=complex)

#create grid of real and image values
    complex_grid = real_grid + 1j * imag_grid

 #FILL IN GRID
    for i in range(rows):
        for j in range(cols):
            complex_grid[i, j] = real_values[j] + 1j * imag_values[i]

    return complex_grid
def get_julia_color_arr(grid, c, max_iterations=256):
    '''Generate a Julia set color array for a given complex constant.'''
    escape_iterations = np.zeros(grid.shape, dtype=int)

    Z = grid.copy()
    for i in range(max_iterations):
        Z = Z ** 2 + c
        mask = np.abs(Z) > 2  
        escape_iterations[mask] = i + 1
        Z[mask] = np.nan  
    escape_iterations = np.clip(escape_iterations, 1, max_iterations)

    color_arr = np.uint8(255 * escape_iterations / max_iterations)

    return color_arr
