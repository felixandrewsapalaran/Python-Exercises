
"""
Alternative 1: A simple approach would be to iterate over the list
and use each distinct element of the list as a key of dictionary and
store the corresponding count of that key as values.
"""

# count the frequency elements in a list using dictionary
def count_frequency(list_num):
    
    # create an empty dictionary
    # that would our frequencies
    frequency = {}
    
    # iterate over the list of numbers
    for item in list_num:
        
        # check if the item is in
        # our dictionary 
        if item in frequency:
            # if it exist then 
            # increment the value of of its key
            frequency[item] += 1
        else:
            # if it doesn't exist then 
            # set the key value to 1
            frequency[item] = 1
    
    # display the key and number of times it appears
    for key, value in frequency.items():
        print(f"Key: {key} | Value: {value}")
        
# Driver function
if __name__ == "__main__":
    array = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    
    # calling the function
    count_frequency(array)




"""
Alternative 2: another approach can be to use the list.count() method.
This makes the program much more compact without affecting the run time.
"""

# count the frequency elements in a list using a dictionary
def count_frequency(array):
    
    # this hold our frequencies
    frequency = {}
    
    for item in array:
        
        # by using the count function it would
        # count the number of time it appears
        # then store it to frequency dict
        frequency[item] = array.count(item)
        
    # diplay the result
    for key, value in frequency.items():
            print(f"Key: {key} | Value: {value}")
            

# Driver function
if __name__ == "__main__":
    array = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    
    # firing the function
    count_frequency(array)
    
