#Version: Python 3.9
#Description: This program will display random numbers between 1 and 100, as many times a user wants, with a imported Random.txt file. 

import random

with open("Random.txt", "w") as handle:
    for i in range(int(input('How many to generate?: '))):
        n = random.randint(1, 100)

        print(n, file=handle)
        print(n)

