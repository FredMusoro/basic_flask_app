class CommandCentre:
	def __init__(self):
		self.order_status = {}
		self.drone_status = {1: "Idle"} 

	def add_order(self, order_id):
		self.order_status[order_id] = "Order is placed and we are working on it."


	def completed_order(self, order_id):
		self.order_status[order_id] = "Completed"

	def register_drone_trip_completed(self):
		self.drone_status[1] = "Idle"