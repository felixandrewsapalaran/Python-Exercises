
"""
Alternative 1: A simple approach would be to iterate over the list
and use each distinct element of the list as a key of dictionary and
store the corresponding count of that key as values.
"""

# count the frequency elements in a list using dictionary
def CountFrequency(my_list):

    # Creating an empty dictionary
    frequency = {}

    # iterate over the list
    for item in my_list:
        # check if the item is in our
        # frequency dictionary
        if item in frequency:
            # if it does take the value
            # of that index and increment by 1
            frequency[item] += 1
        else:
            # if not in frequency dict yet 
            # set it equal to 1
            frequency[item] = 1
    
    
    for key, value in frequency.items():
        print(f"Key: {key} | Value: {value}")


# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    CountFrequency(my_list)




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


