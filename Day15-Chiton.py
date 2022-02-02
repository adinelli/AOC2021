import numpy as np
import pandas as pd

Infty = 1e100
f = open('input_15.csv', 'r')
Lines = f.readlines()

risk = []
for line in Lines:
	row = [int(x) for x in line.strip()]
	risk.append(row)
risk = np.array(risk)
[N,M] = np.shape(risk)

# Matrix of visited locations
check = np.zeros((N,M))
check[0][0] = 1
# Indices of the final destination
xend = M-1	# Column
yend = N-1	# Row

# Dijkstra's algorithm
def dijkstra(x0,y0,xf,yf):
	P = N*M		# Total number of points
	
	D = Infty*np.ones(N*M, dtype='int64')	# Array of distances from starting point, set to Infty 
	s = x0 + y0*M		# Index of starting point in the D array
	f = xf + yf*M		# Index of final point in the D array
	D[s] = 0	# The starting point has distance 0 from itself
	
	# Define array of points still to visit and remove s from it
	NotVisited = [x for x in range(0,P)]
	
	flag = True
	
	while f in NotVisited:
		u = np.argmin([D[x] if x in NotVisited else Infty for x in range(0,P)])		# u is the point closest to the visited set
		xu = int(u % M)
		yu = int(np.floor(u/N))
		neighbours = [[yu+1,xu],[yu,xu+1],[yu-1,xu],[yu,xu-1]]	# Neighbours of u
		
		NotVisited.remove(u)		# Remove u from points to visit
		# For each neighbour v of u in NotVisited
		# check if it is most convenient to reach it passing from u
		# or else from another visited point
		for v in neighbours:
			xv = v[1]
			yv = v[0]
			j = xv + yv*M		# Index of v on distance array
			
			# Take into account boundaries
			if yv>=0 and yv<N and xv>=0 and xv<M:	
			
				# If the neighbour v has not been visited, check optimal path to reach it
				if j in NotVisited:
					if D[j] >= D[u] + risk[xv][yv]:
				 		D[j] = D[u] + risk[xv][yv]
	return D[f]
		
print(dijkstra(0,0,xend,yend))
