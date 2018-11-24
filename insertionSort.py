def insertionSort(unsorted):

	for i in range(1, len(unsorted)):
		key = unsorted[i]
		for j in range(i, -1, -1):
			if(key < unsorted[j]):
				unsorted[j+1] = unsorted[j]
				if(j==0):
					unsorted[j] = key
			elif (key > unsorted[j]):
				unsorted[j+1] = key
				break
			elif (key == unsorted[j]):
				continue;

				
a = [10, 9, 2, 6, 14]
print "Before sorting"
print a
insertionSort(a)
print "\n\n"
print "INSERTION SORT - Final sorted list"
print a
print "------------------------------------------------------------------------------------\n\n\n"

a = [10, 9, 2, 6, 14, 1, 1, 2, 3, 56]
print "Before sorting"
print a
insertionSort(a)
print "\n\n"
print "INSERTION SORT - Final sorted list (contains duplicates)"
print a
print "------------------------------------------------------------------------------------\n\n\n"
