# Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.
import sys

a = input("type a: ")
try:
    a = int(a)
except:
    print("a is not an integer number")
    sys.exit(1)

b = input("type b: ")
try:
    b = int(b)
except:
    print("b is not an integer")
    sys.exit(1)

c = input("type c: ")
try:
    c = int(c)
except:
    print("c is not an integer")
    sys.exit(1)
sum = a+b+c
product = a * b * c
average = (sum)/3

print(f'Sum is: {sum}')
print(f'Product is: {product}')
print(f'Average is: {average}')