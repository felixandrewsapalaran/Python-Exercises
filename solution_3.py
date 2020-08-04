# Challenge: Simulate an Election

# Simulate the results of an election using a Monte Carlo simulation

from random import random

# keep tract number of times candidate A & B wins
num_times_A_wins = 0
num_times_B_wins = 0

 # number of trials
num_trials = 10_000
for trial in range(0,num_trials):
	# we'll keep track of random votes 
	votes_for_A = 0 
	votes_for_B = 0

# determine who wins the 1st region
if random() <  0.87:
	votes_for_A += 1
else:
	votes_for_B += 1

# determine who wins the 2nd region
if random() < 0.65:
	votes_for_A += 1
else:
	votes_for_B += 1

# determine who wins the 3rd region
if random() < 0.17:
	votes_for_A += 1
else:
	votes_for_B += 1

# determine overall election  outcome
if votes_for_A > votes_for_B:
	num_times_A_wins += 1
else:
	num_times_B_wins += 1

# display the probability Candidate A will win 
print(f"Probility A wins: {num_times_A_wins / num_trials:%}")

# display the probability Candidate B will win 
print(f"Probility B wins: {num_times_B_wins / num_trials:%}")
