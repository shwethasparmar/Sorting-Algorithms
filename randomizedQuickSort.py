import random
def randomizedPartition(a, start, end):
	pivot = a[random.randint(start, end)]
	pIndex = start
	print "Before partition"
	print a
	for i in range(start, end):
		if(a[i]<pivot):
			temp = a[i]
			a[i] = a[pIndex]
			a[pIndex] = temp
			pIndex = pIndex + 1

	a[end] = a[pIndex]
	a[pIndex] = pivot
	print "After partition"
	print a
	return pIndex

def quickSort(a, start, end):
	if(start < end): 
		pIndex = randomizedPartition(a, start, end)
		quickSort(a, start, pIndex-1)
		quickSort(a, pIndex+1, end)



a = [3, 2, 1, 12, 15, 9, 6, 10]
quickSort(a, 0, len(a)-1)
print "\n\n\n"
print "RANDOMIZED QUICKSORT - Final sorted list"
print a
print "------------------------------------------------------------------------------------\n\n\n"

a = [3, 2, 1, 12, 15, 9, 6, 10, 10, 10, 10]
quickSort(a, 0, len(a)-1)
print "\n\n\n"
print "RANDOMIZED QUICKSORT - Final sorted list (contains duplicates)"
print a
print "------------------------------------------------------------------------------------\n\n\n"