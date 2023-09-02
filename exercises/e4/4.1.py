# Write a program that uses a while loop to
# print out all
# numbers divisible by three in the range of 1-1000.
x = 1
while x <= 1000:
    if x % 3 == 0:
        print(f'{x} is divisible to 3')
    x = x + 1