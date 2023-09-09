# 1/
# Type ineteger number
# input <= 0 >> ends
# Otherwise print out the facorial of the number

# START = 1 ## always starting with 1
# try:
#     number = int(input("Type integer number:"))
#     while number != "" and number > 0:
#         for i in range (1,number+1):  # to get from 1 to n ( range: 1 to n-1)
#              START = START * i
#              ## n = 1: START = 1,
#              #  N = 2 : START = START * 2   == 1 * 2
#              #  N = 3: START = START * 3    == 1 * 2 * 3
#              print (START)
#         number = int(input("Type integer number:"))
#     print("Thank for playing")
#
# except ValueError:
#     print("Thank you for playing")
# ###---

# while True:
#     number = int(input("Type number: "))
#     if number <= 0:
#         break
#     factorial = 1
#     new = 1
#     while new <= number:
#         factorial *= new
#         new += 1
#
#     print(factorial)

#-----
#2
#WRITE SENTENCE
text = input("Type your sentence:")
# spliting the sentence ot each word
text_split = text.split()
print(text_split)
# PRINT OUT FIRST LETTER OF THE SENTENCE
# EACH LETTER ON A SEPERATE LINE
# for item in text_split:
#     print(f"First lestter í: {item[0]}")
for index,item in enumerate(text_split,start=1):
    print(f"{index}.  {item[0]}")
#




