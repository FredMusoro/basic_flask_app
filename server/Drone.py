import time
from server import commandcentre
class Drone():
	def __init__(self):
		self.location = "Warehouse"    #Establishing the initail conditions of a drone
		self.travel = False 
		self.item_loaded = False

	def drone_available(self):
		return True if(self.travel == False) else False

	def go_back_to_warehouse(self):
		commandcentre.register_drone_trip_completed()
		self.location = "Warehouse"
		self.travel = False

	def reached_destination(self, location, order_id):
		commandcentre.completed_order(order_id)
		self.go_back_to_warehouse()

	def make_delivery(self, location, order_id): #add algo to traverse the drone from warehouse to location
		#insert code
		time.sleep(2) #halting the program for 2 seconds to simulate a minature form of delivery
		print("Drone has reached {}".format(location))
		self.reached_destination(location, order_id)
		
	def take_item_to_location(self, location, order_id):
		self.location = "Transit"
		self.travel = True
		self.item_loaded = True 
		self.make_delivery(location, order_id)