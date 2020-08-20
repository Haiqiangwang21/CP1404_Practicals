"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


'''
Allows user input score and determine the grade the score has achieved 

Haiqiang Wang
'''

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")
score = float(input("Enter score: "))
