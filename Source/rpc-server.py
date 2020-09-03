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

# Inizialize isVerified
isVerified = False

#randomNumber creates a random number between 1 and 9
def createRandomNumber():
    return random.randint(1,9)

#Register createRandomNumber; 
server.register_function((createRandomNumber), 'createRandomNumber')


def verifyPassword(randomNumber, cHash):
    global isVerified
    randomNumberServer = 0
    clientHash = ''
    password = '1234'

    randomNumberServer = randomNumber
    print(randomNumberServer)
    clientHash = cHash

    #Hash Server passwort and randomNumber
    serverHash = hashlib.sha256()
    serverHash.update(password.encode('utf-8'))
    serverHash.update(str(randomNumberServer).encode('utf-8'))
    print(serverHash.hexdigest())
    if (serverHash.hexdigest() == clientHash):
        isVerified = True
        print('Erfolgreich verbunden')
        return True
    else:
        isVerified = False
        print('Verbindung ist fehlgeschlagen')
        return False

#Register verifyPassword
server.register_function((verifyPassword), 'verifyPassword')

# Create Adder_function
def adder_function(x,y):
    if(isVerified):
        print(x + y)
        return x + y
    else:
        print("Password falsch")

# Register adder_function
server.register_function(adder_function, 'adder_function')


# Run the server's main loop
server.serve_forever()









## Register an instance; all the methods of the instance are
## published as XML-RPC methods (in this case, just 'div').
# class MyFuncs:
#    def div(self, x, y):
#        return x // y

# server.register_instance(MyFuncs())