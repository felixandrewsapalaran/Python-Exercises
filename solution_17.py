def even_numbers(maximum):
      return_string = ""
  for x in range(2, maximum + 1, 2):
    return_string += str(x) + " "
  return return_string.strip()

print(even_numbers(6))
print(even_numbers(10))
print(even_numbers(1))
print(even_numbers(3))
print(even_numbers(0))