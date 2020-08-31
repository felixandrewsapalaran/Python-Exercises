# Python-Exercises
# Use this program to exercise 🐍  3 skills 

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 1

# Goal: OOP (Classes & Objects, Encapsulation & Abstractions, Inheritance, Polymorphism)

Instructions: Demostrate the use of OOP

1. Demonstrate the use of Classes & Objects

2. Demonstrate the use of Encapsulation & Abstractions

3. Demonstrate the use of Inheritance

4. Demonstrate the use of Polymorphism

-----------------------------------------------------------------------------------------------------------------------




-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 2

# Goal: Simulate a Coin Toss Experiment

Instructions for coin_toss_experiment.py

Suppose you flip a fair coin repeatedly until it lands on both heads and tails at least once each. In other words, after the first flip, you continue to flip the coin until it lands on something different.

Doing this generates a sequence of heads and tails. For example, the first time you dd this experiement, the sequence might be heads, heads, then tails.

On avarage, how many flips are needed for the sequence to contain both heads and tails?

Write a simulation that runs 10,000 trials of the experiment and prints the average number of flips per trial.



-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 3

# Goal: Simulate an Election

Instruction: With some help from the random module and a little condition logic, you can simulate an election between two candidates.

Suppose two candidates: Candidate A and Candiadate B, are running for mayor in a city with three voting regions. The most recent polls show that Candidate A has the following chances for winning in each region:

                Region 1: 87% chance of winning
                Region 2: 65% chance of winning
                Region 3: 17% chance of winning
Write a program that simulates the election 10,000 times and prints the percentage of where Candidate A wins.

To keep things simple, assume that candidate wins the electioon is they win in at least two of the three regions.



-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 4

# Goal: List of List

Instruction: Write a program that contains the following lists of lists:

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

Define a function, enrollment_stats(), that takes, as an input, a list of list where each individual list contains 
three elements: 

(a)the name of a university
(b) the total number of enrolled studets
(c) the annual tuition fees.

enrollment_stats() should return two lists: 
1. the first containing all of the student enrollment values
2. the second containing all of the tuition fees

Next, define a mean() and a median() function. Both functions should take a single list as an argument and return 
the mean and median of the values in each list.

Using universities, enrollment_stats(), mean(), and median(), calculate the total number of students, the total tuition,
the mean and median of the number of students, and the mean and median tuition values.

Finally, output all values, and format the output so that it looks like this:

******************************
Total students:   77,285
Total tuition:  $ 271,905

Student mean:     11,040.71
Student median:   10,566

Tuition mean:   $ 38,843.57
Tuition median: $ 39,849
******************************



-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 5

# Goal: Cats With Hats

Instruction: You have 100 cats

One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. 
You walk around the circle 100 times, always starting at the same spo, with the first cat 🐈  (cat #1). Every
time you stop at a cat, you either put a hat on it if it doesn't have one on, or you take its hat off if it has 
one on. 

1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.)
3. The third round, you only stop at every third cat (#3, #6, #9, #12, etc.)
4. You continue this process until you've made 100 rounds around the cats (e.g., you only visits the 100th cat).

Write a program that simply outputs which cats have hats at the end.



-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 6

# Goal: Sort the array in decending order witouth moving the -1 in original index position

Instruction: You given an array [-1, 3, 5, -1, 55, 23, -1, 43]. Create a 
function that will sort this function in descending order without 
removing the -1 in their index position

Expected ouput:  [-1, 55, 43, -1, 23, 5, -1, 3]


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 7

# Goal: Counting Frequncies in a list

Instuction: In this program, we have an array of elements to count 
the occurrence of its each element. One of the approaches 
to resolve this problem is to maintain one array to store the 
counts of each element of the array. Loop through the array and 
count the occurrence of each element as frequency and store it in 
another array

Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
Output : 1 : 5
         2 : 4
         3 : 3
         4 : 3
         5 : 2


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 8

# Goal: Calculating the total number of bytes to store

If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up 4097 bytes will use 4096 * 2 = 8192 bytes of storage. Create a function called calculate_storage  which calculates the total number of bytes needed to store a file of a given size.

1 file should have a total of 4096 of bytes in order to store this file
4096 file should have a total of 4096 of bytes in order to store this file
4097 file should have a total of 8192 of bytes in order to store this file
6000 file should have a total of 8192 of bytes in order to store this file


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 9

# Goal: Sum of all divisors

Instruction: Create a function that returns the sum of all of the divisors of a number,
without including it. A divisor is a number that divides into another without remainder

0 # 0   total = 0
3 # shold sum of 1  total = 1
36 # shold sum of 1+2+3+4+6+12+18   total = 55
102 # should sum of 2+3+6+17+34+51          total = 114



-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 10

# Goal: Sum of all squares of numbers

Instruction: Create a function called the sum_squares that returns the sum of all the squares of numbers between 
0 and x(not included). Remember that you can use the range(x) function to generate a sequence of numbers from 0
to x (not included)

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 11

# Goal: Factorial of a number

Instruction: Create a function called factorial that would return the right factorial number 

Example: 4! = 1*2*3*4 = 24

Test cases: 4! should return 24
Test cases: 5! should return 120

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 12

# Goal: Factorial of a number B

Instructions: Create a funtion named factorial that would return the factorial of n. Print the first 10 factorials (0 to 9)
with the corresponding number. Note factorial of 0! is 1

Expected output
0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 13

# Goal: sum in recursive way

Instruction: Create a function named sum_positive_numbers that take n as 
a number and apply recursive that would add the sum of the 
numnbers.


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 14

# Goal: factorial recursive way


Instruction: Create a function named factorrial that would return
the factorial of n using recursive.

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 15

# Goal: Multiplication table with for loops


Instruction: Create a function that prints out a multiplication table(where each number is the result of multiplying the first number of its row by the number at the top of its column).  Run the function so that it would print out the  multiplication table of 1 to 3:

1 2 3
2 4 6
3 6 9

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 16

# Goal: Counting numbers up or down


Instruction: create a counter function that counts down from start to stop when start is bigger than stop, count up from start to stop then.

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 17 

# Goal: return even numbers seperated by space


Instruction: Create a function named even_numbers that returns a space-seperated string all of positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For exampple, even_numbers(6) returns "2 4 6"

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 18 

# Goal:String comparison [0] == [-1]

Create a function called first_and_last that returns True if the first of the string is the same as the last letter of the string. False if they're different. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 19

# Goal: Palindrom

The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Example of palindromes are words like kayak and radar, and phrases like "Never Odd Even". Create a function called is_palindrome to return True if the passed string is a palindrome, False is not.

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 20

# Goal:Converting miles to kilometers
Create a function called convert_distance_function that would returns the convertion from miles to kilometer and display the phrase "X miles equals Y km", with Y only 1 decimal place.

For example, convert_distance(12) should return "12 miles equals 19.2 km"

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 21

# Goal:nameTag

Create a function named nametag that uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 22

# Goal:Skip next elment

Create a function called skip_elements that would return a list containing every other element from an input list, starting with the first element. 
Tip: You can use for loop to iterate through the inut list

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 23

# Goal: List Comprehensions

A. Create a for loop that would loop from 1 to 10 and print the multiple of 7 (use list comprehension only)
B. Create a list of programming language use list comprehension to loop over the list and print the length of each language
C. Create a for loop using list comprehension that would print a list of numbers divisible by 3 (include 0)


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 24

# Goal: use of list comprehension

Create a function called odd_numbers that would return a list of odd numbers between 1 and n, inclusively

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 25

# Goal: Group list with join function

Create a function called group_list that accepts a group name and a list of members, and returns a string with the format: group_name:
member1, member2,...

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 26

# Goal:Guess lists

Create a function called guest_list that reads in a list of tuples with the name, age, and profession of each party guest, and prints the 
sentence "Guess is X years old and works as Y" for each one. For example, guest_list('Ken', 30, "Chef") should 
print out: Ken is 30 years old and works at as Chef

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 27

# Goal: Counting how many times the letter appear in a word or sentence

Create a function that would count the number of letter appears in a word or sentence

Example: tenant
t: 2
e: 1
n: 2
a: 1

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 28

# Goal: access specifiers

Create a function called groups_per_user that receives a dictionary, which contains group names with the list of users. 

input: 
{
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"] 
}

output:

{
  'admin': ['local', 'public', 'administrator'], 
  'userA': ['local'], 
  'userB': ['public']
  }
  
  
  -----------------------------------------------------------------------------------------------------------------------
# Problem Num: 29

# Goal: add total groceries vaues

Create a function named add_prices that returns the total price of all of the groceries in the dictionary. 


-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 30

# Goal: squared of numbers with list comprehension

Create a function and use list comprehension to create a list of squared numbers(n*n). The function receives the variables start and end,
and returns a list of squres of consecutive numbers between start and end inclusively. For example, squares(2,3) should return [4, 9]

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 31

# Goal: Car model and price with dictionary

Create a function that would iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 32

# Goal:Counting letters

Create a function named count_letters and use a dictionary to count the frequency of letter in the input string. Only letter should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

