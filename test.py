import math
import os

import sys
from os import rename
import requests


# name = input("Your name? ")
# print("Hello, ", name)
print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))
print(greet("Corey"))
# r = requests.get("https://coreyms.com")
# print(r.status_code)
print("Hello, my name is marasy.")
