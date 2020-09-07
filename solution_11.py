def factorial(number):
    # counter
    result = 1
    
    for i in range(number):
        # example 4
        # init result = 1
        # 0 += 1 * 0
        # 1 += 1 * 1
        # result = 2
        # 2 += 2 * 2
        # result = 6
        # 6 += 6 * 3
        # result = 24
        result += result * i
    return result

print(factorial(4)) # this returns 24
print(factorial(5)) # this returns 120
