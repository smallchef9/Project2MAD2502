## Part 2: Defining a Grid (10 points)
def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    ...
#create array of real values starting from real part of top_left to bottom_right
    real_values = np.arrange(top_left[0], bottom_right[0], step)
#create array of imaginary values starting from imaginary part of top_left to bottom_right (reversed so order is top to bottom still)
    imaginary_values = np.arrange(top_left[1], bottom_right[1], step[::1])
# generate 2D grid
    complex_grid = np.array([[r + 1j * i for r in real_values] for i in imaginary_values])
    return complex_grid