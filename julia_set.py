def get_julia_color_arr(c: complex, x_min: float, x_max: float, y_min: float, y_max: float, width: int, height: int, max_iterations: int = 256):
    ''' collects escape data for the filled in Julia set for a given 
    complex number and converts it to a color.'''
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    escape_iterations = np.zeros(Z.shape, dtype=int)


    for i in range(max_iterations):
        Z = Z**2 + c
        mask = np.abs(Z) > max(abs(c), 2)
        escape_iterations[mask] = i + 1
        Z[mask] = np.nan


   
