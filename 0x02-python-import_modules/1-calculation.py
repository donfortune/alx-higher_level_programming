#!/usr/bin/python3
from calculator_1 import add,sub,mul,div

a = 10
b = 5

result = add(a,b)
result_1 = sub(a,b)
result_2 = mul(a,b)
result_3 = div(a,b)
print(f"{a} + {b} = {result}")
print(f"{a} - {b} = {result_1}")
print(f"{a} * {b} = {result_2}")
print(f"{a} / {b} = {result_3}")


