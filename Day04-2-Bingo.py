import numpy as np
import pandas as pd

inputfile = open('input_04.csv', 'r')
Lines = inputfile.readlines()
count = 0

for line in Lines:
	if not line.strip(): # Skip blank spaces
		count+=1
	else:
		if count==0:	# Line of drawn numbers
			Numbers = np.array([int(x) for x in line.strip().split(",")])
		else:
			row = np.array([int(x) for x in line.strip().split()])
			
			if count==2: # First time reading from bingo boards
				Bingo = row
			else:
				Bingo = np.vstack((Bingo, row))
		count += 1
		
Check = np.zeros(np.shape(Bingo)) # Table of (0,1) corresponding to numbers that have been drawn on the boards
N = len(Numbers) 	# Length of sequence of numbers that are drawn
M = int(len(Bingo)/5) # Number of boards
L = len(Bingo) 		# Total number of bingo rows

Winners = np.zeros(M)	# Counts if a board has won (1) or not (0)
countwin = 0	# Counts the number of winners


for i in range (0,N):	# Run through all numbers
	for j in range(0,L):	# Run through all rows
		for k in range(0,5):	# Run through all columns
			# Mark numbers that are called
			if Numbers[i]==Bingo[j,k]:
				Check[j,k] = 1
				ntable = int(np.floor(j/5)) # Corresponding board
				
				# Check if someone new wins
				if (np.sum(Check[j,:])==5 or np.sum(Check[ntable*5:(ntable+1)*5,k])==5) and Winners[ntable]!=1:
					Winners[ntable] = 1
					countwin += 1
					print(Check[ntable*5:(ntable+1)*5])
					print("New winner!")
					# Sum of unmarked numbers
					unmarked=0
					for n in range(5*ntable,5*(ntable+1)):
						for m in range(0,5):
							if Check[n,m]==0:
								unmarked += Bingo[n,m]
					print(np.hstack((Bingo[ntable*5:(ntable+1)*5],Check[ntable*5:(ntable+1)*5])))
					print("Winning board:\t", ntable)
					print("Final number\t:", Numbers[i])
					print("Sum of unmarked numbers\t:", unmarked)
					print("Points:\t",unmarked*Numbers[i],"\n")
					
					if countwin==M:
						print('Everyone has won!\n')
						exit()
					
