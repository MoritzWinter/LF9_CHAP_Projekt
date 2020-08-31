#!/usr/bin/env python3

import xmlrpc.client
import hashlib

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print(s.randomNumber()) # Returns a Random Number between 1 and 9
print("Bitte geben Sie ihr Passwort ein: ")
password = input()

# Hash Password and Random Number
hashedPasswordAndRandomNumber = hashlib.sha256()
hashedPasswordAndRandomNumber.update(password.encode('utf-8'))
hashedPasswordAndRandomNumber.update(str(s.randomNumber).encode('utf-8'))
print(hashedPasswordAndRandomNumber.hexdigest())

## Print list of available methods
# print(s.system.listMethods())