import numpy as np

Input = np.loadtxt('input_01.txt',unpack='True')
counter = 0
for i in range (1, len(Input)):
	if Input[i]>Input[i-1]:
		counter += 1
print(counter)

windows=[Input[0]+Input[1]+Input[2],0.]
counter=0

for i in range(1,len(Input)-2):
	# New first measurement is the old last measurement
	windows[0]=windows[1]
	# Update second window
	windows[1]=Input[i]+Input[i+1]+Input[i+2]
	# Compare
	if windows[1]>windows[0]:
		counter += 1
	
print(counter)
