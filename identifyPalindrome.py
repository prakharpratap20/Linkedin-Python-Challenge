# Challenge 
# Write a Python fucntion to determine if a given string is a palindrome 

import re
from turtle import forward  

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r"[a-z]+", phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards 

print(is_palindrome("race car"))