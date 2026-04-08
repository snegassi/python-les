
"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above
 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.
"""

#Answer 1

'''hrs = input("Enter Hours:")
rats = input("Enter Rate per hour:")
h = float(hrs)
r = float(rats)

if  h > 40:
    init_hrs = 40
    extra_hrs =  h - 40
    extra_rate= r * 1.5
    gross_pay = (init_hrs * r) + (extra_hrs * extra_rate)
    print(gross_pay)
else :
    gross_pay = h * r
    print(gross_pay)'''

#Answer 2

hrs = input("Enter Hours:")
rats = input("Enter Rate per hour:")
h = float(hrs)
r = float(rats)

if  h > 40:
    init_pay= h * r
    over_pay = (h-40)*(r * 0.5) # since 10 out of 10.5 of 10.5 rate is already calculated for the extra 5hr above, the 0.5 part is left for the 5 hrs 
    gross_pay = init_pay + over_pay
    print(gross_pay)
else:
    gross_pay = h * r
    print(gross_pay)
