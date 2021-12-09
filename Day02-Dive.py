import numpy as np
import pandas as pd

content = pd.read_csv('input_02.csv', sep=" ", header=None)
Input = content.to_numpy()

x=0	# Horizontal position
y=0	# Depth

for i in range (0,len(Input)):
	if Input[i,0]=='up':
		y-=Input[i,1]
	elif Input[i,0]=='down':
		y+=Input[i,1]
	elif Input[i,0]=='forward':
		x+=Input[i,1]
print(x,y,x*y)


x=0	# Horizontal position
y=0 # Depth
a=0	# Aim

for i in range (0,len(Input)):
	if Input[i,0]=='up':
		a-=Input[i,1]
	elif Input[i,0]=='down':
		a+=Input[i,1]
	elif Input[i,0]=='forward':
		x+=Input[i,1]
		y+=a*Input[i,1]
print(x,y,x*y)
