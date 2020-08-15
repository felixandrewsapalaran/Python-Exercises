def factorial(n):
    if n < 2:
        print("The factorial of 1 is 1")
        return 1
    result  = n * factorial(n - 1)
    print(f"The factorial of {n} is {result}")
    return result

print(factorial(5))