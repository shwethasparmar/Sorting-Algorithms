def selectionSort(a):
	for i in range(0, len(a)):
		minimumIndex = i
		for j in range(i, len(a)):
			if a[j] < a[minimumIndex]:
				minimumIndex = j

		temp = a[i]
		a[i] = a[minimumIndex]
		a[minimumIndex] = temp

a = [64, 25, 12, 22, 11]
print "Before sorting"
print a
selectionSort(a)
print "\n\n"
print "INSERTION SORT - Final sorted list"
print a
print "------------------------------------------------------------------------------------\n\n\n"

a = [64, 25, 12, 22, 11, 1, 2, 6, 5, 5, 6]
print "Before sorting"
print a
selectionSort(a)
print "\n\n"
print "INSERTION SORT - Final sorted list (contains duplicates)"
print a
print "------------------------------------------------------------------------------------\n\n\n"