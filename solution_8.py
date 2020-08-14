def calculate_storag(filesize):
    
    block_size = 4096

    # use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size

    # use the  modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size

    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return filesize

print(calculate_storag(1)) # should return 4096
print(calculate_storag(4096)) # should return 4096
print(calculate_storag(8192)) # should return 8192
print(calculate_storag(6000)) # should return 8192