import numpy as np

f = open('test_16-1.csv','r')
hexa = f.readlines()[0].strip()
N = len(hexa)

b=bin(int(hexa,16))[2:].zfill(N*4)

def decode(x, N):
	L=len(x)
	j=0
	VERSION_SUM = 0	# Sum of versions in packets and subpackets
	counter = 0	# Counts the number of packages in a string
	
	if N==None:
		limit = True
	else:
		N = int(N)
		limit = counter<N
		end_point = N
		
	while j<L and limit:
		version=int(int(x[j:j+3],2))
		package=int(int(x[j+3:j+6],2))
		VERSION_SUM += version
		if package==4:
			i=j+6
			flag=True	# Remains true until the first 5-bit block starting with 0 is encountered
			literal=''
			# Store digits of literal
			while flag == True:
				# Check first bit of the 5-bit block
				if x[j+i]=='0':
					flag = False
				digit=x[j+i+1:j+i+5]	# Store last 4 bits of the block
				literal=literal+str(digit)
				i+=5
			literal=int(int(literal,2))	# Convert literal to decimal
			j=i+3
			
		else:
			new_version=0	# Sum of versions of sub-packets
			new_count=0 	# Number of sub-packets
			end_point=0		# Contains the length of sub-packets
			LtID=int(int(x[j+6:j+9],2))	# Length data type
			# If LtID==0 we are given the total length of the subsequent sub-packets
			if LtID=='0':
				sub_length=int(int(x[j+9:j+24],2))
				[new_version, end_point, new_count] = decode(x[j+24:j+24+sub_length], None)
			# If LtID==1 we are given the number of sub-packets
			elif LtID=='1':
				sub_num=int(int(x[j+9:j+20],2))
				sub_num = str(sub_num)
				[new_version, end_point, new_count] = decode(x[j+20:j+20], sub_num)

			VERSION_SUM += new_version
			counter+=new_count
			j+=end_point
			
		counter+=1
		print(counter,N)
			
	return VERSION_SUM, end_point, counter


print(decode(b, None))
