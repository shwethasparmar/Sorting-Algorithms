from array import *;

def moveRobo(r, c , numRows, numCols):
	print "Called moveRobo with (%s, %s)" % (str(r), str(c))
	if(r==numRows and c==numCols):
		# print str(r)+ ", " + str(c)
		return True

	if (c+1 <= numCols):
		if(a[r][c+1] != 0):
			# print "Taking right"
			# print "R value in first if is " + str(r)
			# print "C value in first if is "+str(c)	
			moveRobo(r, c+1, numRows, numCols)

	if (r+1 <= numRows):
		if(a[r+1][c] !=0):
			# print "Going down"
			# print "R value in second if is "+str(r)
			# print "C value in second if is "+str(c)
			moveRobo(r+1, c, numRows, numCols)


n = 3
a = [[1] * n for i in range(n)]

a[0][2] = 0
a[2][1] = 0

res = moveRobo(0, 0, 2, 2)

for row in a:
    print(' '.join([str(elem) for elem in row]))