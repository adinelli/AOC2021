import numpy as np

Infty = 1000
f = open('input_11.csv','r')
Lines = f.readlines()

data = []
for line in Lines:
	row = [int(x) for x in line.strip()]
	data.append(row)

data = np.array(data)
[N,M] = np.shape(data)

energy = np.ones(shape=(N+2,M+2), dtype='int64')*(-Infty) # Add a frame of -Infty around dataset
increase = np.zeros(shape=(N+2,M+2), dtype='int64') # Matrix of energy increases due to neighbouring flashes
flashes = np.zeros(shape=(N+2,M+2), dtype='int64') # Matrix of flashes
energy[1:N+1,1:M+1] = data

def restore_frame(matrix):
	[n,m] = np.shape(matrix)
	matrix[0,:] = -Infty
	matrix[n-1,:] = -Infty
	matrix[:,0] = -Infty
	matrix[:,m-1] = -Infty
	return

# Iterate over steps
for k in range(0,10000):
	flag = True
	energy+=1	# Increase energy of all octopuses by 1
	
	# Iterate until everyone that could has flashed
	while flag == True:
		flag = False
		# Look for octopuses that have flashed
		for i in range(1,N+2):
			for j in range(1, M+2):
				if energy[i,j]>9:
					energy[i,j] = 0	# Set his energy to 0
					flashes[i,j] = 1	# Update his flash for this step
					# Compute energy increase for neighbours
					increase[i+1,j] += 1
					increase[i-1,j] += 1
					increase[i,j+1] += 1
					increase[i,j-1] += 1
					increase[i-1,j-1] += 1
					increase[i+1,j-1] += 1
					increase[i-1,j+1] += 1
					increase[i+1,j+1] += 1
		# Increase energy of octopuses unless they flashed
		for i in range(1,N+2):
			for j in range(1, M+2):
				energy[i,j] += increase[i,j]*(1-flashes[i,j]) # Update energy if octopus has not flashed
				if energy[i][j]>9:
					flag=True		# If a new octopus can flash, restart loop
		increase *= 0
	
	num_flash = np.sum(flashes[:,:])
	flashes *= 0
	restore_frame(energy)
	if(num_flash == N*M):
		print(energy)
		print(k+1)
		break
