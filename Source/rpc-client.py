#!/usr/bin/env python3

import xmlrpc.client
import hashlib


s = xmlrpc.client.ServerProxy('http://localhost:8000')

randomNumber = s.createRandomNumber()


print(randomNumber) # Returns a Random Number between 1 and 9
print("Bitte geben Sie ihr Passwort ein: ")
password = input()



# Hash Password and Random Number
cHash = hashlib.sha256()
cHash.update(password.encode('utf-8'))
cHash.update(str(randomNumber).encode('utf-8'))
print(cHash.hexdigest())

s.verifyPassword(randomNumber, cHash.hexdigest())

s.adder_function(5,2)









## Print list of available methods
# print(s.system.listMethods())