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
#create array of real values starting from real part of top_left to bottom_right
    real_values = np.arange(top_left.real, bottom_right.imag, step)
#create array of imaginary values starting from imaginary part of top_left to bottom_right (reversed so order is top to bottom still)
    imaginary_values = np.arange(top_left.real, bottom_right.imag, step[::-1])
# generate 2D grid
    complex_grid = np.array([[r + 1j * i for r in real_values] for i in imaginary_values])
    return complex_grid
