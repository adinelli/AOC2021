import numpy as np

Input = open('input_08.csv','r')
Lines = Input.readlines()
counter = 0

for line in Lines:
	row = line.strip().split(" ")
	output = row[len(row)-4:len(row)]
	for i in range(0,len(output)):
		if len(output[i])==2 or len(output[i])==3 or len(output[i])==4 or len(output[i])==7:
			counter += 1
			
print(counter)

## SECOND PART
#----------------------------------- FUNCTIONS -----------------------------------------
def containsAll(str, set):
	# Check whether sequence str contains ALL of the items in set.
	return 0 not in [c in str for c in set]

def determine_mapping(entry, digits):
	# Determine mapping for a given entry
	for s in entry:
		if len(s)==2:
			digits[1]=sorted(s)
		elif len(s)==3:
			digits[7]=sorted(s)
		elif len(s)==4:
			digits[4]=sorted(s)
		elif len(s)==7:
			digits[8]=sorted(s)
	for s in entry:
		if len(s)==6:
			if containsAll(sorted(s),digits[4]):
				digits[9]=sorted(s)
			else:
				if containsAll(sorted(s),digits[1]):
					digits[0]=sorted(s)
				else:
					digits[6]=sorted(s)
	for s in entry:
		if len(s)==5:
			if containsAll(digits[6],sorted(s)):
				digits[5]=sorted(s)
			else:
				if containsAll(digits[9],sorted(s)):
					digits[3]=sorted(s)
				else:
					digits[2]=sorted(s)		

#------------------------------------ CODE ------------------------------------------------
result = np.zeros(len(Lines),dtype=int)	# Contains all the outputs expressed in decimal form
j = 0 # Counts the number of lines
for line in Lines:
	row = line.strip().split(" ")
	entry = row[0:len(row)-5]
	output = row[len(row)-4:len(row)]
	
	# Re-initialize values of digits
	digits = ['','','','','','','','','','']
	# Determine mapping
	determine_mapping(entry, digits)
	
	for i in range(0,len(output)):
		# Sort alphabetically the four output digits
		x=sorted(output[i])	
		for K in range (0,10):
			if x == digits[K]:
				result[j] += K*10**(3-i)
	j+=1
	
print(sum(result))
