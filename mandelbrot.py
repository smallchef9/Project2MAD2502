def get_escape_time(c: complex, max_iterations: int) -> int | None:
    z = 0 + 0j 
    for k in range(max_iterations):
        z = z ** 2 + c
        if abs(z) > 2:
            return k
    return None








