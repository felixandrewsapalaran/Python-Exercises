
def sum_positive_numbers(n):
    # base case is n being smaller than 1
    if n < 1:
        return 0

    # the recursive case is adding this number to 
    # the sum of the numbers smaller than this one
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3) # should return 6
print(sum_positive_numbers(5)) # should return 15

