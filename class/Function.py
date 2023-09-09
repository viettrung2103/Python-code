# a = 5
# b = 3

# def cal (a,b):
#     a = 3
#     b = 2
#     sum = a + b
#     return sum
# a = int(input("a: "))
# b = int(input("b: "))
#
# addition = cal(a,b)
# print(addition)

#draw_spruce (number)
#3
# " * " 3
# "***" 3
# " * " 3
#4
# "  *   1" 5
# " ***  3" 5
# "***** 5" 5
# "  *   1" 5
#5
# "   *   " 7
# "  ***  " 7
# " ***** " 7
# "*******" 7
# "   *   " 7
#6
# "    *    " 9 (4-0)*(0-4) print
# "   ***   " 9 (3-1)*(1-3)
# "  *****  " 9 (2-2)*(2-2)
# " ******* " 9 (1-3)*(3-1)
# "*********" 9 (0-4)*(4-0)
# "    *    " 9


import math

EMPTY_SPACE= " "
ASTERISK = "*"

def draw_tree(number):
    n=0
    slot_per_line = (number-1)*2 -1 # 3: 3, 4: 5, 5: 7
    length_to_fill = math.floor((slot_per_line-1)/2) # 3:1, 4:2, 5:3
    # "" "* n,* * (leng_to_fill-n),  ,"*" ,* * n , "  " *( length_to_fill -n)"
    if number == 1:
        print("*")
    elif number == 2:
        print("*")
        print("*")
    else:
        while n < number-1:
            print(f"{EMPTY_SPACE* int((length_to_fill - n))}{ASTERISK * n}*{ASTERISK * n}{EMPTY_SPACE * int((length_to_fill-n))}")
            n += 1
        print(f"{EMPTY_SPACE * length_to_fill}*")
# draw_tree(5)

def tree_program():
    number = int(input("how many spruces do you want your tree to have: "))
    draw_tree(number)

tree_program()