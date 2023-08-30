# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

FEMALE_UPPER = 155
FEMALE_LOWER = 117
MALE_UPPER = 167
MALE_LOWER = 134

gender = input("What is your gender (male/female): ")
hemoglobin = int(input("Please type your hemoglobin value: "))

if gender == 'male':
    if hemoglobin < MALE_LOWER:
        print("your hemoglobin value is low")
    elif MALE_LOWER <= hemoglobin <= MALE_UPPER:
        print("your hemoglobin value is normal")
    else:
        print("your hemoglobin value is high")
elif gender == 'female':
    if hemoglobin < FEMALE_LOWER:
        print("your hemoglobin value is low")
    elif FEMALE_LOWER <= hemoglobin <= FEMALE_UPPER:
        print("your hemoglobin value is normal")
    else:
        print("your hemoglobin value is high")
else:
    print("No gender found. Program close")