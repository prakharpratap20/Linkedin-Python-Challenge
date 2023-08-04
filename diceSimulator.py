# Challenge 
# Write a Python function to determine the probability of 
# certain outcomes when rolling dice

from random import randint  
from collections import Counter

def rollDice(*dice, numTrials=1000000):
    counts = Counter()
    for _ in range(numTrials):
        counts[sum((randint(1, sides) for sides in dice))] += 1
        
    print("\n Outcome \t Probability")
    for outcome in range(len(dice), sum(dice) + 1):
        print(f"{outcome}\t{counts[outcome] * 100 / numTrials :0.2f}%")
        
rollDice(6, 6, 6, 6, 6)
# here 5 dices having 6 faces each are being used as an example 