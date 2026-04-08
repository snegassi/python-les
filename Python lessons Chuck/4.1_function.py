

"""
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
Do not name your variable sum or use the sum() function.
"""


"""
hr=input("Enter hours:")
rat=input("Enter rates:")

def cal_hr_rate(hr,rat):
    h=float(hr)
    r=float(rat)

    if h <= 40:
        total_pay = h * r
        return total_pay
    else:
        normal_pay= 40 * r
        overtime_pay= (h-40)*(r*1.5)
        total_pay= normal_pay + overtime_pay
        return total_pay
    
cal_hr_rate(hr,rat)
"""
"""
Your logic in the above is completely correct, but if you are submitting this to an automated grader 
(like for a Coursera or Python for Everybody course),
 there are three small details you need to fix to get a passing grade.

1. The Function Name
The prompt specifically asks you to name the function computepay(). 
In programming, sticking to the requested name is crucial because the grading software
 will look for that specific name to test your code.

 2. Printing the Result
Your code calculates the value and returns it, but it doesn't print it to the screen.
 To see the output 498.75, you need to print the result of the function call.

The Return Trip: Think of return like a delivery person. The function goes off, calculates the pay, and 
"delivers" the number back to the variable p. Without print(p), that delivery just sits there unseen!

3. Indentation & Order
In Python, you must define the function before you try to use it. 
While your logic is sound, it's cleaner to put your inputs after the function definition.

Variable Scope: It is usually better to convert the strings to float() before sending them into the function. 
This keeps the function focused only on the math (computepay), not on data conversion. Just as the below
"""
def computepay(h, r):
    if h <= 40:
        total_pay = h * r
    else:
        normal_pay = 40 * r
        overtime_pay = (h - 40) * (r * 1.5)
        total_pay = normal_pay + overtime_pay
    
    return total_pay

# Get inputs and convert to float
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hrs)
fr = float(rate)

# Call the function and print the returned value
p = computepay(fh, fr)
print("Pay", p)