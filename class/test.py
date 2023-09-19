L = ['xy','yz']
for i in L:
    i.upper()
print(L)

#zip to iterate over multi list
#for shortest list
#for name1,name2,... in zip(list1,list2,...)
## unpack return a tuple
names = ['name1','name2','name3','name4']
heros = ['hero1','hero2','hero3','hero4']
universes = ['universe1','universe2','universe3','universe4']
# to iterate 2 lists at the same time
for name, hero,universe in zip(names,heros,universes):
    print(f"{name} is {hero}")

#unpack all
a,b,*c = (1,2,3,4,5)
print(a)
print(b)
print(c)

class Person():
    pass

person = Person()
first_key = "first"
first_value = "Corey"
setattr(person,first_key,first_value)
first = getattr(person,first_key) # retrieve attribute value via its attribute
print(first)

