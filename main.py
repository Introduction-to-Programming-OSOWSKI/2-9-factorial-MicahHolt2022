def factorial(x):
    y = 1
    for i in range(0, x):
        y = y * (x - i)
    return y

print(factorial(5))