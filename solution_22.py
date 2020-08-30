def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0
    
    # Iterate through the list
    # used enumarate to assign an index to each item
    # in iterable object
    
    for i, e in enumerate(elements):
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_list.append(e)
        # Increment i
        i += 1
    
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Starberry', 'Peach']
print(skip_elements([])) # Should be []