
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
def CountFrequency(my_list):

    frequency = {}

    for items in my_list:
        frequency[items] = my_list.count(items)

    for key, value in frequency.items():
        print(f"Key: {key} | Value: {value}")

# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    CountFrequency(my_list)


