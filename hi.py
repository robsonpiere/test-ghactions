from os import getenv
from datetime import datetime
print("Hi 😁")
print("I'm a action test! 😁")
print(getenv('TAG', "tag not found! 👀"))
print(getenv('VARIAVEL', "VARIAVEL not found! 👀"))
print(datetime.now())
