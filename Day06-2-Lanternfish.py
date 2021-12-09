import numpy as np
import pandas as pd

Input = pd.read_csv('input_06.csv', sep=",", header=None)
lanternfish = np.transpose(Input.to_numpy()) # Create row 1xN

counter = np.zeros(9,dtype='int64') # Each entry corresponds to the number of fish in a status [0,...,8]
N = len(lanternfish)
t=1
tf=256

for i in range(0, N):
	for j in range (0,9):
		if lanternfish[i]==j:
			counter[j]+=1

while t<=tf:
	newcount = counter*0		# Create new empty array where to temporarily store number of fish in a status [0,..,8]
	newcount[8]=counter[0]	# Count how many fish were born at time t
	newcount[6]+=counter[0]	# Reset timer of fish that give birth to new ones (from 0 -> 6)
	for j in range (0,8):
		newcount[j]+=counter[j+1]	# Decrease all timers by 1
	counter=newcount
	t+=1

print('After %d days: Number of lanternfish: %d' %(t-1,sum(counter)))
