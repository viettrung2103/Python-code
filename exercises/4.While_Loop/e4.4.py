# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.
import random

play = input("Do you want to play a game(y/n) :")
while play == 'y':
    number = random.randint(1,10);
    guess = int(input("Please type a number (1-10): "))
    if guess > 10 or guess < 1:
        print("number should be between 1 and 10")
        guess = int(input("Please type a number (1-10): "))
    # print(f'guess: {guess}')
    # print(f"number: {number}")
    if guess > number:
        print("Too high!!")
    if guess == number:
        print("Correct!!")
        break
    if guess < number:
        print("Too low")
    play = input("Do you want to continue(y/n): ")

print("Thank you for playing")
