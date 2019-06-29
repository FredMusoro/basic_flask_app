#This defines our Warehouse class 
#Currently it is one so it is a class for one.

class Warehouse:
	def __init__(self, products, parking):
		self.products = products #a list of products where the index in the list is its product type
		self.parking = parking  #number of parkings available at the warehouse

	def warehouse_info(self):
		return"The warehouse has {} products and {} parking.".format(self.products, self.parking)