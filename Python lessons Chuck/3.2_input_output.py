
"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit.
 For the test, enter a score of 0.85.

"""

#Answer 1
score = input("Enter Score: ")

point = float(score)

if point <0.0 or point>1.0:#Think about the number line:Can a number be less than $0.0$ AND greater than $1.0$ at the same time? No.
    #A number can be $-5$, or it can be $10$, but it can't be both.that's why we use or in this case
    print("Error AAA")  

elif point >= 0.9:
    print("Score >=0.9, A")
    
elif point >= 0.8:
    print("Score >=0.8, B")
    
elif point >= 0.7:
    print("Score >=0.7, C")    
    
elif point >= 0.6:
    print("Score >=0.6, D")
    
else :
    print("Score <=0.6, F")