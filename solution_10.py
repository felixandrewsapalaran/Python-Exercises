# this calcualtes the square 
# of numbers
def squares(number):
    return number * number

# this returns the sum of 
# square of all number
def sum_squares(length):
    
    # keep track of the summation
    sum = 0
    
    for num in range(length):
        
        # calling square function and pass
        # every index value of lenght
        # add the squared numbers into sum variable
        sum += squares(num)
        
    # return the total sum
    return sum

# should return 285
print(sum_squares(10))
