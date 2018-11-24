def bubbleSort(a):
	for i in range(len(a)):
		flag = False
		for j in range(len(a)-1):
			if(a[j] > a[j+1]):
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
				flag = True
		if(flag == False):
			break


a = [5, 4, 6, 1, 2, 9]
print "Before sorting"
print a
print "\n\n"
bubbleSort(a)
print "BUBBLE SORT - Final sorted list"
print a
print "------------------------------------------------------------------------------------\n\n\n"


a = [5, 4, 6, 1, 2, 9, 2, 3, 3, 10]
print "Before sorting"
print a
print "\n\n"
bubbleSort(a)
print "BUBBLE SORT - Final sorted list (contains duplicates)"
print a
print "------------------------------------------------------------------------------------\n\n\n"