def factorial(x):
    y = 1
    for i in range(1, x):
        y = y * (x - i)
    return y
