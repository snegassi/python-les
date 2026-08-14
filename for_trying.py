
# x = 1

# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5")
# else:
#     print("ha ha ")
# print("finished")

#  Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.

raw_hr = input("Enter the hours:")
raw_rate_hr = input("Enter the rate per hours:")

try: 
    hr = int(raw_hr)
except:
    # hr = -1
    hr = "Enter hour in Number"

try: 
    pay = float(raw_rate_hr)
except:
    pay = "Enter Pay rate in Number"
    # pay = -1

# if hr > 0:
#     print("Number of hour Accepted")
# else:
#     print("Number of hour Not Accepted")
print (hr, "+" , pay)
