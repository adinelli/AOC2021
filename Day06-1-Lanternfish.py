import numpy as np
import pandas as pd

Input = pd.read_csv('input_06.csv', sep=",", header=None)
lanternfish = np.transpose(Input.to_numpy()) # Create row 1xN

N = len(lanternfish)
t=1
tf=80

while t<=tf:
	print('t = %d' %t)
	for i in range(0, N):
		lanternfish[i] -= 1
		if lanternfish[i]==-1:
			lanternfish = np.append(lanternfish, [8])
			lanternfish[i]=6
	N = len(lanternfish)
	print('\tNumber of lanternfish: %d' %N)
	t+=1
