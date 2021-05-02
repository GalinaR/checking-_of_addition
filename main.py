"""
Function randomly generate addition problems until the user has gotten 3 problems correct in a row
"""

import random

CORRECT_TIMES = 3 # user should  correct in a row 3 problems

def main():
    i = 1
    while i != 4: # exit from the loop when i = 4
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        result = num1 + num2
        print("What is", num1, "+", num2) # generated addition problem
        answer = int(input("Your answer: ")) #
        if result == answer:
            print("Correct! You've gotten " + str(i) + " correct in a row.")
            i += 1
        else: # user made a mistake
            print("Incorrect. The expected answer is", result)
            i = 1 # correct answers are reset
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()