def step(stepNo, n):
	if(stepNo + 1 == n ):
		return 1
	elif (stepNo + 2 == n):
		return 2
	elif (stepNo +3 == n ):
		return 4

	return step(stepNo+1, n) + step(stepNo+2, n) + step(stepNo+3, n)
	
	

#counter = 0

def step1(stepNo, n):
	if(stepNo + 1 == n ):
		return 1
	elif (stepNo + 2 == n):
		return step(stepNo + 1, n) + 1
	elif (stepNo +3 == n ):
		return step(stepNo + 1, n) + step(stepNo + 2, n)
	else:
		return step(stepNo+1, n) + step(stepNo+2, n) + step(stepNo+3, n)

print(step1(0,5))
