# Building Number Guessing Game


# import random module
import random

# store number of user attemp to guess here
num_attemp = []

# create function that will display the score
def display_score():
	# check if there's a current available score
	if len(num_attemp) <= 0:
		print("Great news! There is no currently high score on the table. You could be the first!")
	else:
		#display the minimum attempt on the list
		print(f"The current high score is {min(num_attemp)}")

# create a function that will control the game
def game():

	# generate a random number from 1 to 10
	jackpot_num = random.randint(1, 10)
	name = input("Hi! What's your name? ")
	# create a welcome page
	greetings = print(f"""
	
	--------------------------------------------
	Welcome to the Number Guessing Game {name}
	--------------------------------------------
	""")

	# prompt the user if they want to play
	play = input("Do you want to play the Guessing Game? (Y|N): ")	

	# count every attempt to guess the number
	attempt = 0

	# if the user answered yes start the game
	while play.lower() == 'y':
		try:
			# capture user chosen number
			guess = int(input("Please pick a number between 1 and 10: "))
			# raise error if the user input is outside the give range
			if guess < 1 or guess > 10:
					raise ValueError("Please guess a number within the given range")
			# compare the user guessed number to jackpot number
			if guess == jackpot_num:
				print(f"You got it! My number was {jackpot_num}")
				# once user guessed the correct number increment
				attempt += 1
				# store number of attemp into the list
				num_attemp.append(attempt)
				# let user know how mant times it took them to guessed the number
				print(f"It took you {attempt} tries to guessed the number\n")
				# prompt the user if they want to play again
				play_again = input("Would you like to play again? (Y|N): ")
				# if user answered `no` to play again
				if play_again.lower() == 'n':
					print("That's Ok, thanks for playing again.")
					# break out of the game
					break	
				# if the user answer yes do the following:				
				# restart the number of attempt
				attempt = 0
				# display the previous score
				display_score()
				# generate random number again
				jackpot_num = random.randint(1,10)
			# check if the guess number is greater than the jackpot number
			# give them a HINT
			elif guess > jackpot_num:
					print(f"It's lower than {guess}")
					# incerement attempt
					attempt += 1
			# check if the guess number is less than the jackpot number
			elif guess < jackpot_num:
					print(f"It's higher than {guess}")
					attempt += 1
		# print the message below if the user input other than integer
		except ValueError as err:
			print(f"Oh no!, {err} is not a valid value. Try again...")
	else:		
		# if the user doesn't want to play the game
		print(f"That's OK, It's nice meeting you {name}!")


# calling the functions
if __name__ == '__main__':
    	game()
			
