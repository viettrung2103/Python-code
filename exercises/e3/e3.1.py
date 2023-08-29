# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish
# back into the lake and notifies the user of how many centimeters below the size
# limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

print("---- MEASURING SYSTEM ----")
LIMIT =  42
size_str = input("What is the lenght of your fish (in cm):")

size = float(size_str)

if size < LIMIT :
    short = LIMIT - size
    print(f"PLEASE RELEASE THE FISH")
    print(f"FISH IS UNDERSIZE, THE FISH IS {short} CM BELOW THE REQUIREMENT")
else:
    print("THE FISH IS BIG ENOUGH")
    print("YOU CAN KEEP THE FISH")
    print("HAVE A NICE DAY")
    print("--ENDING MEASURING--")



