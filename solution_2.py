# Challenge: Simulate a Coin Toss Experiment

import random

# function that would return the `heads` or `tails`
# each time you flip it
def coin_flip():
	"""Randomly return `heads` or `tails`."""
	if random.randint(0, 1) == 0:
		return "heads"
	else:
		return "tails"

# keep track number of flips
flips = 0
# total number of trial
num_trials = 10_000

# we'll use for loop to flip the coin 10,000 times
for trial in range(num_trials):
	# check if the flipped coin is `head`
	if coin_flip() == "heads":
		# increment the number of flips by 1
		flips += 1
		# as long as you get `heads` keep flipping
		while coin_flip() == "heads":
			# keep incrementing the total number of flips
			# until `tails` is returned by coin_flip()
			flips += 1
		# once coin_flip() return `tails`, the loop will exit,
		# but we need to add one more to flips to track the
		# last flip that generated `tails`
		flips += 1
	else:
		# coin_flip() returned `tails` on the first flip.
		# increment the number of flips by 1
		flips += 1
		# as long as you get `tails` keep flipping
		while coin_flip() == "tails":
    			# keep incrementing the total number of flips
				# until "heads" is returned by coin_flip()
				flips += 1
		# once coin_flip() returns `heads`, the loop will exit,
		# but we need to add one more to flips to track the 
		# last flip that generated `heads`
		flips += 1

# calculate the average flips per trial
avg_flips_per_trial = flips / num_trials
print(f"\nThe average number of flips per trial is {avg_flips_per_trial}\n")



# Alternative solution B

import random

def coin_flip():
	"""Randomly return 'heads' or 'tail'."""
	if random.randint(0, 1) == 0:
		return "heads"
	else:
		return "tails"

# keep track number of flips
flips = 0
# number of trial or number of flips
num_trials = 10_000

for trial in range(num_trials):
	# flip the coin once and increment the flips tally by 1
	first_flip = coin_flip()
	flips += 1
	
	# continue flipping the coin and updating the tally until
	# a different result is returned by coin_flips()
	while coin_flip() == first_flip:
		flips += 1
	# increment the flip tally once more to account for the 
	# final flip with a different result
	flips += 1

# calculate the average per flips
avg_flips_per_trial = flips / num_trials 
print(f"The average number of flips per trial is {avg_flips_per_trial}.")
