#Importing that the python package requires and making the first objects
from flask import Flask
from server.warehouse import Warehouse
from server.commandcentre import CommandCentre
commandcentre = CommandCentre()
warehouse = Warehouse([3,5],5)
from server.Drone import Drone
app = Flask(__name__)
drone = Drone()

from server import routes