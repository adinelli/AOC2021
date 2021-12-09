import numpy as np
import pandas as pd

Input = pd.read_csv("input_07.csv", sep=',', header=None)
crabs = np.transpose(Input.to_numpy())
N = len(crabs)
maxpos = np.max(crabs)

## FIRST PART
xopt = 0 			# Optimal position
copt = +1e100 # Optimal cost, initially set to +infty

for xx in range(0,maxpos+1):
	cost = 0 # Cost
	for j in range (0, N): 
		cost += int(np.abs(crabs[j]-xx))
	if cost < copt:
		copt = cost
		xopt = xx

print(copt, xx)


## SECOND PART
xopt = 0 			# Optimal position
copt = +1e100 # Optimal cost, initially set to +infty

for xx in range(0,maxpos+1):
	cost = 0 # Cost
	for j in range (0, N): 
		k = int(np.abs(crabs[j]-xx))
		cost += k*(k+1)/2
	if cost < copt:
		copt = cost
		xopt = xx

print(copt, xx)
