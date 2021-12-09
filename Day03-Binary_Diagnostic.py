import numpy as np
import csv

file = open('input_03.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append([int(row[0][i]) for i in range (0,len(row[0]))])

L = len(rows[0])	# Number of digits
M = len(rows)			# Number of rows

## FIRST PART
result = np.zeros(L)
gamma = 0
epsilon = 0

for j in range (0, L):
	for i in range (0, M):
		result[j] += rows[i][j]/M
		
	if result[j]>=0.5:
		result[j]=1
		gamma	+= 10**(L-1-j)
	else:
		result[j]=0
		epsilon	+= 10**(L-1-j)
print("Gamma rate:\t", gamma, int(str(gamma),2))
print("Epsilon rate:\t", epsilon, int(str(epsilon),2))
print("Result 1: \t", int(str(gamma),2)*int(str(epsilon),2))


## SECOND PART
# O2 generator rating
result = np.zeros(L)	# Re-initialize array of results
sequenceO2 = rows			# Array where we store numbers according to criteria
M = len(rows)

for j in range (0, L):
	for i in range (0, M):
		result[j] += sequenceO2[i][j]/M
		
	if result[j]>=0.5:
		result[j]=1
	else:
		result[j]=0
	
	# Remove rows according to rule
	remove = []	# List of rows to remove
	k=0
	while k<M:
		if (sequenceO2[k][j]!=result[j]):
			remove.append(k)
		k+=1
	sequenceO2 = np.delete(sequenceO2, remove, axis = 0)
	M = len(sequenceO2)
	if M<=1:
		break
# Convert the selected number into a binary string and in decimal form
O2_generator = sum([int(sequenceO2[0][i]*10**(L-1-i)) for i in range (0,L)])
print("O2 generator rating:\t", O2_generator, int(str(O2_generator),2))


# CO2 generator rating
result = np.zeros(L)	# Re-initialize array of results
sequenceCO2 = rows		# Array where we store numbers according to criteria
M = len(rows)

for j in range (0, L):
	for i in range (0, M):
		result[j] += sequenceCO2[i][j]/M
		
	if result[j]>=0.5:
		result[j]=0
	else:
		result[j]=1
		
	# Remove rows according to rule
	remove = []	# List of rows to remove
	k=0
	while k<M:
		if (sequenceCO2[k][j]!=result[j]):
			remove.append(k)
		k+=1
	sequenceCO2 = np.delete(sequenceCO2, remove, axis = 0)
	M = len(sequenceCO2)
	if M<=1:
		break
# Convert the selected number into a binary string and in decimal form
CO2_generator = sum([int(sequenceCO2[0][i]*10**(L-1-i)) for i in range (0,L)])
print("CO2 generator rating:\t", CO2_generator, int(str(CO2_generator),2))
print("Result 2: \t", int(str(CO2_generator),2)*int(str(O2_generator),2))
