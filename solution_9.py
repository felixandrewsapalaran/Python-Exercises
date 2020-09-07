def sum_divisor(given_num):
    
    # keep track of the sum
    sum = 0
    
    # counter
    x = 1
    
    # keep looping as long as the counter is 
    # less than the given number
    while x < given_num:
        # check if the number divide by x
        # return a 0 remainder
        if given_num % x == 0:
            # if so take the value of counter 
            # add it to our sum
            sum += x
        
        # increment the counter by 1s
        x  += 1
    
    # return total sum of all divisor 
    # of given number not including the given number
    return  sum


print(sum_divisor(0)) # 0   Total = 0
print(sum_divisor(3)) # Should sum of 1   Total = 1
print(sum_divisor(36)) # Should sum of 1+2+3+4+6+9+12+18   Total = 55
print(sum_divisor(102)) # Should sum of 2+3+6+17+34+51            Total =  114
            
    
    
