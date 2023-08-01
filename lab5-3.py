"""
Question 3 (Now try this with a loop – which is best for this problem WHILE or FOR??)

The code above will randomly set the variable rand_num to be 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9.
Using that information, create a fully documented program that will randomly choose a number from,
and including, 1 to 100. Do not display the number.
Ask the user to guess the number.
Supply feedback to the user to tell them that their guess was too low or too high and give them another
guess. When they guess it correctly, tell them how many guesses they took.

import random

rand_num = random.randrange(10)
"""
import random

rand_num = random.randrange(10)
counter = 0
k = 1
while k != 0:
    n = int(input("Let's play the game! Can you guess the number? It's your move:"))
    if n > rand_num:
        print("Too high")
        counter += 1
    elif n < rand_num:
        print("Too low")
        counter += 1
    else:
        print("Perfect", "number of attempts =", counter)
        k = 0