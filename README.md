# basic_flask_app
simulating a basic drone sevice

Run: pip install -r requirements.txt to have all the required dependencies. 


The routes that are available are: 
1) '/' and '/info' these provide the info about the warehouse
2) '/orders' this returns all the orders placed with their order IDs
3) '/order_status' this returns the status of all the orders
4) '/placeorder/<int:id>' this places an order for product[id]. Currently two types 
						  of products are in the warehouse, so, id 0 and 1 are available. 
						  This also starts the process of delivery.


During delivery a pause of 2 seconds has been inserted in the code to 
simulate a miniature delivery. 

"python run.py" will start the app.
