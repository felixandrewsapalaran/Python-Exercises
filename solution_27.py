def count_letters(text):
    result = {}
    
    for letter in text.lower():
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("Tenant"))
print(count_letters("a long string with a lot of letters"))