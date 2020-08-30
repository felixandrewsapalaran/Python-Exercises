# This is without using list comprehension
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(f'Using regular for loop\n{multiples}')

# A
multiples = [x * 7 for x in range(1, 11)]
print(f'\nUsing list comprehension\n{multiples}')

# B
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(f"\nLength of each langauge\n{lengths}")

# C
z = [x for x in range(0,101) if x % 3 == 0]
print(f"\nmultiples of 3 from 0 to 100 \n{z}")