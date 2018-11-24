#Abstraction 
class SouthIndianRestaurant:
	__dishOfTheDay = "" #private variable
	__numberOfEmployees = 0 #private variable

	def __init__(self):
		self.__dishOfTheDay = "Masala Dosa"
		self.__numberOfEmployees = 10

#Method overloading 
	def placeOrder(self, order="Nothing", specialInstructions=''):
		print "This is the order " + str(order)


abc = SouthIndianRestaurant()
abc.placeOrder("Idly")
abc.placeOrder()
abc.placeOrder(5,specialInstructions = "No peanuts")