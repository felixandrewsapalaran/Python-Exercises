# input: [-1, 3, 5, -1, 55, 23, -1, 43]
# output: [-1, 55, 43, -1, 23, 5, -1, 3]

def new_sort(array):
    # create an empty container to hold our 
    # new sorted list
    container = []
    
    # create a copy of the list
    copy_array = array[:]
    
    # iterate throug our array
    for i in range(len(array)):
        
        # check if the index value is 
        # less than 0 
        if array[i] < 0:
            
            # if so append it to the
            # counter container
            container.append(array[i])
        
        else:
            
            # use the copy array take the
            # max number and append it to container
            container.append(max(copy_array))
            
            # remove the max value to copy array
            copy_array.remove(max(copy_array))
    
    # return the value of the container
    return container

array = [-1, 3, 5, -1, 55, 23, -1, 43]

print(new_sort(array))
