#These are all the routes that hit an api and contain how all are processed
from flask import jsonify, abort
from server import app
from random import randint
from server import drone, commandcentre, warehouse
orders_made = []
@app.route("/", methods=["GET"])
@app.route("/info", methods=["GET"])
def info():
	creation = warehouse.warehouse_info()
	if(drone.drone_available()):
		creation += " A drone is available."
	return creation


@app.route("/orders", methods=['GET'])  # All the orders with their IDs
def orders():
	return jsonify(orders_made)
 
@app.route("/order_status", methods = ["GET"])   #Status of all the orders that were placed
def order_status():
	return jsonify(commandcentre.order_status)

@app.route("/placeorder/<int:id>", methods = ["PUT"])
def order(id):
	if(drone.drone_available() and warehouse.products[id] > 0):
		warehouse.products[id] -= 1  # Decreasing a product of the ordered id from the warehouse
		order_id = randint(100, 1000000000) #Generating a random ID for the order
		orders_made.append([id, order_id])
		commandcentre.add_order(order_id)
		drone.take_item_to_location("Location address", order_id)
		return jsonify({"Placed": "Product has been placed with order ID: {}".format(order_id)})
	else:
		abort(404)

