import numpy as np
from matplotlib import pyplot as plt

def add_to_set(elem, LIST):
	if elem not in LIST:
		LIST.append(elem)

f = open('input_13.csv','r')
Lines = f.readlines()

coord = []
fold	= []
for line in Lines:	
	if line!='\n':	# Skip empty lines
		line = line.strip().split(',')	# Remove commas
		if "fold" not in line[0]:	# Numerical lines are stored as coordinates
			coord.append([int(i) for i in line])
		else:
			instr = line[0].replace('fold along ','')	# Store fold instructions
			instr = instr.split('=')
			fold.append(instr)

for instr in fold:
	k = len(coord[:])	# Number of distinct points
	folded = []	# Array of points after folding
	
	# Case 1: fold along x direction
	if instr[0]=='x':
		x0 = int(instr[1])
		for i in range (0, k):
			if coord[i][0]>x0:
				coord[i][0] = -coord[i][0] + 2*x0
			add_to_set(coord[i], folded)
			
	# Case 2: fold along y direction
	else:
		y0 = int(instr[1])
		for i in range (0, k):
			if coord[i][1]>y0:
				coord[i][1] = -coord[i][1] + 2*y0
			add_to_set(coord[i], folded)
	coord = folded
	
k = len(coord[:])		# Number of distinct points

xx = [P[1] for P in coord]
yy = [P[0] for P in coord]

xmax = np.max(xx)
ymax = np.max(yy)

print(k)
plt.scatter(xx,yy)
plt.show()
