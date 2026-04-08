

"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number 
catch it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
  
largest = None

smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
print("Maximum", largest)

"""

# Answer
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    # 1. Check for the exit condition
    if num == "done":
        print("We break since we caught DONE")
        break
    
    # 2. Try to convert to integer, catch errors like 'bob'
    try:
        n = int(num)
    except:
        print("The input was NOT INTEGER, So user input other integer ?")
        continue  # Goes back to the top of the loop to ask again   
    
    # 3. Logic for Largest and Smallest
    
    if  smallest is None:
        
        smallest = n
        largest = n
        print("This number is the first one & is assigned to both as a starting number since they are both started as None(Empty variable)")
    elif n < smallest:
         smallest = n
         print("After the assinment above at (smallest = n), the 1st smallest", n)# does not print because in the above the 
    elif n > largest:
         largest = n
         print("After the assinment above at (largest = n),1nd largest", n)

print("Minimum is", smallest)
            
print("Maximum is", largest)
