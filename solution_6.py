def newSort(my_array):

    # created an empty list to hold
    # the newly sorted values
    container = []

    # created a copied of passed in list
    copy_arr = my_array[:]
    for i in range(len(my_array)):

        # check each items in orig list
        # to see if if it a negative
        if my_array[i] < 0:

            # if it is append it to the container
            container.append(my_array[i])
        else:

            # take the max number since we want the 
            # list to be in descending order
            container.append(max(copy_arr))

            # destroying the copy by removing each 
            # item in the copied list
            copy_arr.remove(max(copy_arr))
    return container

my_array = [-1, 3, 5, -1, 55, 23, -1, 43]

print(newSort(my_array))
