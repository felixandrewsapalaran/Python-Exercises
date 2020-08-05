# Python-Exercises
# Use this program to exercise 🐍  3 skills 

-----------------------------------------------------------------------------------------------------------------------
# Problem Num: 1

# Goal: Generate random number

Instructions for guessing_game.py

Have you ever played a game with your friends where you ask them to Pick a number between some range of numbers like: "Pick a number between 1 and 10"? Their job is to make a guess, and you tell them whether their guess is too high or too low. Their next guess is based on what you've told them. If they guess the right answer the game is done. Normally you try to do this in the lowest number of tries possible. Often it is used to compete with friends to see who can get the answer in the lowest number of guesses.

Build a console number guessing game that prompts a player to choose a number between a specified range of numbers. After the user guesses the correct number, display the number of attempts it took them to guess correctly.

**How the program works**
* Made sure the script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
* As a player of the game, they should see a some kind of text header, welcome or game intro message, before or above the menu.
* As a player of the game, they should be continuously prompted for a guess until they get it right.
* As a player of the game, after an incorrect guess they should be told if their answer is higher or lower than the answer, so that they can narrow down their guesses.
* As a player of the game, after the game ends they should be shown their number of attempts at guessing.
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

# Goal: Model Farm

The focus of this assignment isless about the Python class syntax and more about software design in general, which is highly subjective. This assignment is intentionally left open ended to encourage you to think about how you would organize your code into classes.

Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attribute s, and methods. Think about the inheritance. How can you prevent code dupication? Take the time to work through as many iterations as you feel are necessary.

The actual requirements are open to interpretation, but try to adhere to these guidelines:

1. You should have at least four classes: the parent "Animal" class and at least three child animal classes that inherit from "Animal"

2. Each class should have a few attributes and at least one method that models some behaviors appropriate for a specific animal or all animals - walkin, runnin, eating, sleeping, and so on.

3. Keep it simpl. Utilize inheritence. Make sure you output details about the animals and their behaviors.







