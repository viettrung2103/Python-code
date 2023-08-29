# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.
import random

list1 = ['0','1','2','3','4','5','6','7','8','9']
# list2 = [1,2,3,4,5,6,7,8,9]
list3 = ["1","2","3","4","5","6"]

a = random.choice(list1)
b = random.choice(list1)
c = random.choice(list1)
d = random.choice(list1)
e = random.choice(list1)
f = random.choice(list1)

a1 = random.choice(list3)
b1 = random.choice(list3)
c1 = random.choice(list3)
d1 = random.choice(list3)
a2 = random.choice(list3)
b2 = random.choice(list3)
c2 = random.choice(list3)
d2 = random.choice(list3)


sequence1 = a+b+c
sequence2 = d+e+f

sequence3 = a1+b1+c1+d1
sequence4 = a2+b2+c2+d2

print("3 digits")
print("Two random combinations are:")
print(f'{sequence1} and {sequence2}')

print("----------")
print("4 digits")
print("Two random combinations are:")
print(f'{sequence3} and {sequence4}')
