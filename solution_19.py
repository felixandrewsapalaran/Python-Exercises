def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string:
        # Add any non-blank letter to the
        # end of one string, and to the front
        # of the other string.
        if letter != " ":
            new_string += letter
            reverse_string = letter + reverse_string
    # Compare the strings
    if new_string.lower() == reverse_string.lower():
        return True
    return False

print(is_palindrome("Never Odd or Even")) # should be True
print(is_palindrome("abc")) # should be False
print(is_palindrome("kayak")) # should be True 