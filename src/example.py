def is_triangle(a, b, c):
    return a + b > c and \
        c + b > a and \
        a + c > b
