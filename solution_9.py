def sum_divisor(n):
    sum = 0
    x = 1

    while x < n:
        if n % x == 0:
            sum += x
        x += 1
    
    # return  the sum of all divisors of 
    # n , not including n
    return sum

print(sum_divisor(0)) # 0
print(sum_divisor(3)) # Should sum of 1
print(sum_divisor(36)) # Should sum of 1+2+3+4+6+9+12+18
print(sum_divisor(102)) # Should sum of 2+3+6+17+34+51

