# Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle. A unit circle has the radius of one and
# it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle
# so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates
# with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points. Each point inside the square is tested for
# whether it resides inside circle A. Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing
# if it fulfills the inequation x^2+y^2<1.).
# π≈4n/N
import random
X = 1
X_NEGATIVE = -1
Y = 1
Y_NEGATIVE = -1

#1 ask how many points inside the square
try: # check for not int or empty
    total_point = int(input("How many points: "))
    inside_point = 0
    n = 0
#1.1 generate random cordinate for the point
    while n <= total_point:
        # print is for test, but use with n < 100
        # print(f"time: {n}")
        # print(f"point inside: {inside_point}")
        #random.uniform will get a random float number from [a,b]
        x = random.uniform(X,X_NEGATIVE)
        y = random.uniform(Y,Y_NEGATIVE)
#2 check whether the point is inside the circle or not, using inequation
        result = x**2 + y**2
        if result < 1:
            inside_point = inside_point+1
            n = n+1
        else:
            n = n+1
#3 pi = points inside / total point
    pi = 4* inside_point / total_point
    print(f"pi: {pi}") #result with n = 1,000,000 is pi = 3.141924
    print("finish")
except ValueError: #not int or empty reult
    print('Invalid input')