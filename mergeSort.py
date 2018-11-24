import math
def merge(a, b):
	c=[]
	i = 0
	j = 0
	print "Merging "
	print a
	print b
	while(i<(len(a)) and j< (len(b))):
		if(a[i] <= b[j]):
			c.append(a[i])
			i = i+1
		elif(b[j] < a[i]):
			c.append(b[j])
			j = j+1

	while(i!= (len(a))):
		c.append(a[i])
		i = i+1

	while(j!= (len(b))):
		c.append(b[j])
		j = j+1

	print "Merged"
	print c
	return c

def mergeSort(a, low, high):
	if(low < high):
		MR = int(math.ceil(float(high+low)/2))
		ML = MR-1
		left = mergeSort(a, low, ML)
		right = mergeSort(a, MR, high)
		merged = merge(left, right)
		return merged
	else:
		return [a[low]]		

a = [3, 2, 4, 1, 5, 90, 62]
sortedList = mergeSort(a, 0, len(a)-1)
print "\n\n\n"
print "MERGESORT - Final sorted list"
print sortedList
print "------------------------------------------------------------------------------------\n\n\n"

a = [3, 2, 1, 12, 15, 9, 6, 10, 10, 10, 10]
sortedList = mergeSort(a, 0, len(a)-1)
print "\n\n\n"
print "MERGESORT - Final sorted list (contains duplicates)"
print sortedList
print "------------------------------------------------------------------------------------\n\n\n"
