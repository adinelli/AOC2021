import numpy as np
import pandas as pd

f = open('test_12-1.csv','r')
Lines = f.readlines()

# Crate a dictionary {cave: [size, neighbour1, neighbour2, ...]}
CAVES = {}
for line in Lines:
	line = line.strip().split('-')
	
	# Store the two caves
	cave1 = line[0]
	cave2 = line[1]
	
	# Store the size of cave1
	if cave1.isupper()==1:
		size1='BIG'
	else:
		size1='small'
	# Store the size of cave2
	if cave2.isupper()==1:
		size2='BIG'
	else:
		size2='small'

	# For a new cave, add its size and neighbours in list val
	if cave1 not in CAVES.keys():
		val1 = [size1, cave2]
	# If a cave has already been stored, add new neighbour to the list of values
	else:
		val1 = CAVES.get(cave1)
		val1.append(cave2)
	# Same for cave2:
	if cave2 not in CAVES.keys():
		val2 = [size2, cave1]
	else:
		val2 = CAVES.get(cave2)
		val2.append(cave1)
	
	# Update the cave dictionary
	CAVES.update({cave1: val1})
	CAVES.update({cave2: val2})
	
print(CAVES)

# Remove from dictionary of caves
def remove_cave(x, caves):
	neighbours = caves.get(x)[1:]
	print('neighborhood of x=',x, neighbours)
	caves.pop(x)	# Remove key corresponding to a cave
	# For all neighbours of x, remove all connections with x
	for n in neighbours:
		nn = caves.get(n)
		nn.remove(x)
		caves.update({n: nn})	# Update connections of n having removed edge (n,x)


# Visit caves
def visit_caves(x0, xf,caves):
	counter = 0	# Path counter
	print('\nx0=',x0)
	
	# If start point and end point coincide
	if x0==xf:
		print('\t-> Reached the end!')
		return 1
	
	# If no more caves are visitable
	if len(caves)==0:
		return 0
	
	# Else, compute recursively all possible paths in [x0,xf]
	# We store size and available neighbours of the x0 cave
	size = caves.get(x0)[0]
	neighbours = caves.get(x0)[1:]
	
	# If no neighbours are left, no path going to end exists
	if len(neighbours)==0:
		print('\t-> Dead end!')
		return 0		
	print('size',size)
	print('neigh',neighbours)
	
	visitable_caves = caves.copy()
	print('Visitable caves',visitable_caves)
	
	# If x0 cave is small, we have to remove it from visitable
	# caves in the next iterations
	if size=='small':
		remove_cave(x0, visitable_caves)
		# Then we explore all paths between [xx, xf]
		for xx in neighbours:
			print('New path starts from',xx,'with visitable caves',visitable_caves)
			counter += visit_caves(xx, xf, visitable_caves)
		
	# If a cave is BIG, we can simply explore all paths between the
	# neighbours of x0 and xf
	else:
		for xx in neighbours:
			counter += visit_caves(xx, xf, visitable_caves)
	
	return counter
	
print(visit_caves('start','end',CAVES))

		
