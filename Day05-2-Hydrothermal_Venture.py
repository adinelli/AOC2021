import numpy as np
import pandas as pd

df=pd.read_csv('input_05.csv',sep=",",header=None)
# Split central columns with sep = -> and merge with first and last columns
dfcleancsv = pd.concat([df[[0]], df[1].str.split("->",expand=True).astype(int),df[[2]]],axis=1)
# Convert four columns to numpy
data=dfcleancsv.to_numpy()
N = len(data[:,0])

# Keep only horizontal/vertical/45-degree lines in dataset
i=0
remove = []	# List of rows to remove
while i<N:
	print('Reading: %d/%d' %(i,N-1))
	if (data[i,0]!=data[i,2] and data[i,1]!=data[i,3] and (np.abs(data[i,1]-data[i,3])!=np.abs(data[i,0]-data[i,2]))):
		remove.append(i)
	i+=1
data = np.delete(data, remove, axis = 0)
N = len(data)

# Determine grid shape: [0,0] -> [frame_x, frame_y]
frame_x=max(np.max(data[:,0]),np.max(data[:,2]))
frame_y=max(np.max(data[:,1]),np.max(data[:,3]))
Grid = np.zeros((frame_y+1,frame_x+1),dtype='int64')
Counter = np.zeros((frame_y+1,frame_x+1),dtype='int64') # Counts dangerous areas

for i in range (0,N):
	print("Row %d / %d" %(i,N-1))
	print(data[i,:])
	# Define displacement unit vector
	u=[int(data[i,2]-data[i,0]),int(data[i,3]-data[i,1])]
	if (u[0]!=0): 
		u[0]=int(u[0]/np.abs(u[0]))
	if (u[1]!=0): 
		u[1]=int(u[1]/np.abs(u[1]))
	print(u)
	# Initial position and grid update at (x0,y0)
	x = data[i,0]
	y = data[i,1]
	Grid[y,x]+=1
	if Grid[y,x]>1:	
		Counter[y,x]=1
	# Fill intermediate positions
	while (x!=data[i,2] or y!=data[i,3]):
		x += u[0]
		y += u[1]
		Grid[y,x]+=1
		if Grid[y,x]>1:	
			Counter[y,x]=1
	
print(Grid)
print(Counter)
print(np.sum(Counter))
