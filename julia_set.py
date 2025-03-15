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
