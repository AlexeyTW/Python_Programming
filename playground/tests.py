import requests, dis
from datetime import datetime
from mymodule import multiply
import opcode

num = 5

print(multiply.__code__.co_code)
print(dis.dis(multiply))
print(opcode.opmap)