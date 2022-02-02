import numpy as np
import collections

f = open('test_14.csv','r')
Lines = f.readlines()
count = 0
rule = []

for line in Lines:
	if line!='\n':	# Skip empty line
		if count==0:
			formula0 = line
		else:
			rule.append(line.strip().split(' -> '))
		count += 1
		
rule_pairs = [row[0] for row in rule]
replacement = [row[1] for row in rule]


def replace_with_rules(s):
	new = s[0]	# Create new string starting from the first charachter of s
	# Take all adjacent pairs of chars in s
	for i in range(0,len(s)-1):
		pair = s[i]+s[i+1]
		# If it has to be replaced, update it according to rule
		if pair in rule_pairs:
			j=rule_pairs.index(pair)
			new = new+replacement[j]+s[i+1]
		# Else add it to new without changes
		else:
			new = new+s[i+1]
	return new

formula = formula0	# Initialize
for i in range (0,10):
	formula = replace_with_rules(formula)
	#print('After step ', i+1,': ', formula)
	#print(len(formula))
formula = formula.strip()	

# Count most and least common
char_count = collections.Counter(formula)
most_common = collections.Counter(formula).most_common(1)
least_common = collections.Counter(formula).most_common(len(char_count))

print(most_common[0])
print(least_common[len(char_count)-1])
print(most_common[0][1]-least_common[len(char_count)-1][1])
