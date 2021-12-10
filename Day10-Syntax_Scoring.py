import numpy as np

file = open('input_10.csv','r')
Lines = file.readlines()

#------------------------------- FUNCTIONS -----------------------
# Conversion string -> num (first part)
def convert(c):
	if c=='(':
		return -3
	elif c==')':
		return +3
	elif c=='[':
		return -57
	elif c==']':
		return +57
	elif c=='{':
		return -1197
	elif c=='}':
		return +1197
	elif c=='<':
		return -25137
	elif c=='>':
		return +25137

# Conversion string -> num for incomplete lines
def convert_incomplete(c):
	if c=='(':
		return +1
	elif c=='[':
		return +2
	elif c=='{':
		return +3
	elif c=='<':
		return +4
		
#------------------------------ CODE --------------------------------

# Store corrupted and incomplete lines
corrupted = []
incomplete = []

# Syntax points for corrupted lines
pC=0

for line in Lines:
		line=line.strip()
		# We iterate removing good closures "[],{},(),<>"
		new=line.replace('{}','').replace('[]','').replace('()','').replace('<>','')
		while new!=line:
			line=new
			new=line.replace('{}','').replace('[]','').replace('()','').replace('<>','')
		# Once we have removed all good closures:
			# if the remaining line is empty -> Correct line
			# if it contains only open brackets -> Incomplete line
			# if it contains a closed bracket -> Corrupted line
			
		# We convert brackets into the corresponding numerical points
		row=[convert(line[i]) for i in range(0,len(line))]
		
		# Count correct lines if present
		if line==[]:
			correct += 1
		else:
			# If there is a positive number in line (closed bracket) -> corrupted line
			flag=1 # Bool to check whether a positive number has been found in the line
			for xx in row:
				if xx>0:
					corrupted.append(line)
					pC+=xx*flag # Update syntax points with only the first error
					flag=0	# When the first error is found, switch flag to 0
				# If no corruption was found:
			if flag==1:
				incomplete.append(line)
	
print(pC)



## SECOND PART
# Syntax points for incomplete lines
pI=np.zeros(len(incomplete),dtype='int')

row=[]
j=0
for line in incomplete:
	# Store in numerical row with inverted order
	row=[convert_incomplete(line[len(line)-i-1]) for i in range(0,len(line))]
	# Count points
	for xx in row:
		pI[j]*=5
		pI[j]+=xx
	j+=1

pI=np.sort(pI)
middle=int((len(pI)-1)/2)
print(pI[middle])
