import numpy as np
import csv

file = open('input_09.csv','r')
Lines = csv.reader(file)

Input = []
for row in Lines:
		Input.append([int(row[0][i]) for i in range (0,len(row[0]))])
		
N = np.shape(Input)[0]
M = np.shape(Input)[1]

# Surround the input matrix with 10's so to avoid boundary problems
data = 10*np.ones((N+2,M+2),dtype=int)
data[1:N+1,1:M+1] = Input

LowPoints = []
points = 0
for i in range (1,N+1):
	for j in range (1,M+1):
		if (data[i][j]<data[i][j-1]) and (data[i][j]<data[i][j+1]) and (data[i][j]<data[i+1][j]) and (data[i][j]<data[i-1][j]):
				points += data[i][j]+1
				LowPoints.append([i,j])
				
print(points)



## SECOND PART
K = len(LowPoints)	# Total number of lowpoints
basins = np.zeros((K,N+2,M+2),dtype=int)	# For each lowpoint, a table of basins is assigned
size = np.ones(K,dtype=int)	# Size of the basin for each lowpoint

# Initialize the basins by including just the lowpoints
for k in range(0,K):
	[l,m] = LowPoints[k]
	basins[k][l][m] = 1

# Check the points above, below, to the right and left of a given (x,y)
# If their value is <9, add them to the k^th basin and iterate over 
# the neighbours of the new points
def add_neighbours_to_basin(x,y,k):
	if (data[x+1][y]<9) and (basins[k][x+1][y]!=1):
		basins[k][x+1][y] = 1
		size[k] += 1
		add_neighbours_to_basin(x+1,y,k)
	if (data[x][y+1]<9) and (basins[k][x][y+1]!=1):
		basins[k][x][y+1] = 1
		size[k] += 1
		add_neighbours_to_basin(x,y+1,k)
	if (data[x-1][y]<9) and (basins[k][x-1][y]!=1):
		basins[k][x-1][y] = 1
		size[k] += 1
		add_neighbours_to_basin(x-1,y,k)
	if (data[x][y-1]<9) and (basins[k][x][y-1]!=1):
		basins[k][x][y-1] = 1
		size[k] += 1
		add_neighbours_to_basin(x,y-1,k)
	return

# For each low point, find the basins
for k in range(0,K):
	[x0,y0] = LowPoints[k]
	add_neighbours_to_basin(x0,y0,k)

size = np.flip(np.sort(size))
print(size[0],size[1],size[2])
print(size[0]*size[1]*size[2])
