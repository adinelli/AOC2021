import numpy as np

# Import target area
f = open('input_17.csv','r')
line = f.readlines()[0].strip().split(' ')
line = [x.strip(',') for x in line]
xtarget = line[2]
ytarget = line[3]
xtarget=[int(x) for x in xtarget[2:].split('..')]
ytarget=[int(y) for y in ytarget[2:].split('..')]

xmin = xtarget[0]
xmax = xtarget[1]
ymin = ytarget[0]
ymax = ytarget[1]

# Positions as a function of step x(n, v0x); y(n, v0y)
def x(n, v0x):
	n_threshold = v0x # Steps after which the probe stops along x
	# For n>n_threshold, the x position is the one computed for n_threshold
	if n>n_threshold:
		n=n_threshold
	# Compute the x position
	if v0x>0:
		return int(n*v0x - n*(n-1)/2)
	else:
		return -int(n*v0x - n*(n-1)/2)
	
def y(n, v0y):
	return int(n*v0y - n*(n-1)/2)

# We want to make vy0>0 maximal. After a certain number of steps
# the probe is back at y=0 with velocity -(vy0+1). Not to overshoot
# the target, vy should thus be to the min(y) of the target -1
vybest = np.abs(ymin)-1

# FIRST PART
# The particle stops along y after vy0 steps: that corresponds to
# the point of max height
print(y(vybest, vybest))

## SECOND PART
# We consider xmax, xmin > 0 and ymax, ymin < 0
# Find the range of vx, vy that can hit the target
vxmin = int(np.floor(-0.5 + 0.5*np.sqrt(1+8*xmin^2)))+1
vxmax = xmax
vymin = ymin
vymax = -ymin-1

vx_range = np.arange(vxmin, vxmax+1, 1, dtype='int64')
vy_range = np.arange(vymin, vymax+1, 1, dtype='int64')
nmax = max(xmax+1,2*(-ymin+1))
counter = 0
v_list = []

for vx in vx_range:
	for vy in vy_range:
		print(vx,vy)
		flag = True
		n = 1
		# Iterate until you hit the target or do too many steps
		while flag == True:
			xx = x(n,vx)
			yy = y(n,vy)
			n += 1
			# When you hit the target, add v to the list and count+1
			if (xx<=xmax) and (xx>=xmin) and (yy<=ymax) and (yy>=ymin):
				counter += 1
				v_list.append((vx,vy))
				flag = False
			if n>nmax:
				flag = False
				
print(counter)
