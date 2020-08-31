#!/usr/bin/env python3

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import hashlib


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

#randomNumber creates a random number between 1 and 9
def randomNumber():
    return random.randint(1,9)

#Register randomNumber;
server.register_function((randomNumber), 'randomNumber')


#Inizialize passwort
password = "1234"

#Hash passwort and randomNumber
hashedPasswordAndRandomNumber = hashlib.sha256()
hashedPasswordAndRandomNumber.update(password.encode('utf-8'))
hashedPasswordAndRandomNumber.update(str(randomNumber).encode('utf-8'))
print(hashedPasswordAndRandomNumber.hexdigest())



## Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
# server.register_function(pow)

## Register a function under a different name
# def adder_function(x,y):
#     return x + y
# server.register_function(adder_function, 'add')

## Register an instance; all the methods of the instance are
## published as XML-RPC methods (in this case, just 'div').
# class MyFuncs:
#    def div(self, x, y):
#        return x // y

# server.register_instance(MyFuncs())

# Run the server's main loop
server.serve_forever()