def squares(start, end):
    squares = [value ** 2 for value in range(start, end + 1)]
    return squares

print(squares(2, 3)) # should be [4, 9]
print(squares(1, 5)) # should be [1, 4, 9, 16, 25]
