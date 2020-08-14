def square(n):
    return n * n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

# Should return 285
print(sum_squares(10))