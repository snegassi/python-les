

### 📦 Step 6: Functions (Building Your Own Tools)
## Up until now, we’ve been writing "Scripts"—code that runs from top to bottom once. 
# But in IT Support, you often perform the same task over and over (like resetting a password or checking a server's health).

## Instead of rewriting the code every time, we wrap it in a Function. 
# Think of a function like a Macro or a Saved Command.

### 💡 The "Recipe" for a Function:

# def: Short for "Define." It tells Python, "I'm building a tool!"

# The Name: Give it a clear name (e.g., check_ram).

# The Parameter: The "input" you give the tool (inside parentheses).

# The return: The "output" the tool gives back to you.
#---------------------------------

# Python
# # 1. Define the tool
# def welcome_user(name):
#     return f"Hello {name}, welcome to the IT Portal."

# # 2. Use the tool (Call it)
# message = welcome_user("Daniel")
# print(message)
#---------------------------------------

# def process_data(my_input):
#     print("Type:", type(my_input))
#     print("Length:", len(my_input))

# # CALLING WITH A LIST
# process_data([1, 2, 3]) 
# # Result: Type: <class 'list'>, Length: 3

# # CALLING WITH A STRING
# process_data("[1, 2, 3]") 
# # Result: Type: <class 'str'>, Length: 9
#--------------------------

### def register_student(name, grades, age):
#     print(f"Registering {name}...")
#     print(f"Average grade: {sum(grades) / len(grades)}")

# # Calling the function
# register_student("Marcus", [88, 92, 79], 20)
# print(register_student("Marcus", [88, 92, 79], 20))

###---- Breakdown of the inputs above:
# "Marcus": String (Needs quotes because it's a name).
# [88, 92, 79]: List (Needs brackets, but NO quotes around the brackets).
# 20: Integer (No quotes).
#----------------------------

## ✏️ Exercise 6.1: The "Security Scanner" Function
# Let's turn your "Password Strength" logic into a reusable tool.

# Define the function: def is_secure(password):
# Inside the function (Tabbed):
# IF len(password) is greater than 8:
# return "Strong"
# ELSE:
# return "Weak"
# Use the function:
# Create a variable: result = is_secure("12345")
# Print the result.

# ❓ Check-in
# Can you see how the word password inside the def line is just a "placeholder"? When you call the function with "12345", that number "plugs into" the placeholder.
# Does the return keyword make sense? It's how the function "hands" the answer back to the main part of your script.
# Once you've run your first function, tell me: What happens if you call is_secure("PythonIsCool2026")?

# In len():
# List context:len([1, 2, 3]): Python sees 3, Since the items r inside the list/[]
# List context: len(["Apple"]) is 1 (1 item inside the list), Since the items r inside the list/[]
# String context: len("Apple") is 5 (5 letters)/characters
# len("[1, 2, 3]"): Python sees 9 characters, Since the "" is outside the list, the[]'s r considered Separate 

# def is_secure(password):
#      # Inside the function (Tabbed)
#      if len(password) > 8: # len()= only works with (strings,list,dictionary & tuples) and Not (integers & float)
#          return "Strong"
#      else:
#           return "Weak"   
# #Outside the function
# result = is_secure("12345") # to support the above comment, that;s why here the input is within "" = "12345"
# print(result)

# Result = Weak
#-----------------------------------

## Exercise 6.2: The "RAM Auditor" Function
# Now, let's turn your previous "RAM check" into a reusable tool.

# Define a function called needs_upgrade.
# It should take one parameter: ram_size.
# Inside:
# IF ram_size is less than 16, return True.
# ELSE, return False.
# Test it: * print(needs_upgrade(8))
# print(needs_upgrade(32))

# ❓ Check-in
# Does it make sense that "attempts" and "ram_size" are just "placeholders"? 
# They don't have a value until you actually call the function with a number.
# Can you see how the return keyword is like the "Exit" door of the function, 
# handing the answer back to your main program?

# def needs_upgrade (ram_size):
#     if ram_size < 16:
#         return True
#     else:
#         return False

# # Calling the function
# call = needs_upgrade(8)
# print(call)

# Result = True
#----------------------------------

### print VS return ???
# The simplest way to think about it is: print is for people; return is for the computer.

# 1. print() is a "Display"
# When you use print, you are telling the computer to show a value on the screen so you can see it. 
# Once it's printed, that value is gone as far as the program is concerned. The function doesn't "hold onto" it.

# 2. return is a "Result"
# When you use return, the function hands a value back to the part of the program that called it. 
# You can then save that value in a variable, use it in a math equation, or pass it to another function.

# A Real-World Example
# Imagine you are at a Smoothie Shop:

## "print" is like the blender making a loud noise. You know it’s working, and you can see the fruit spinning, 
# but the noise doesn't give you a smoothie to drink.

# "return" is the employee actually handing you the cup. 
# You now "possess" the smoothie and can go do something else with it (like drink it or put it in the fridge).

# Python
# def add_and_print(a, b):
#     print(a + b)

# def add_and_return(a, b):
#     return a + b

# # Scenario A: Using Print
# result_a = add_and_print(5, 5) # This shows "10" on the screen.
# print(result_a + 10)           # ERROR: result_a is "None" because nothing was returned.

# # Scenario B: Using Return
# result_b = add_and_return(5, 5) # Nothing shows on the screen yet.
# print(result_b + 10)            # This works! It prints "20".
#-----------------------------------------

### 🛠️ The "Pro" Version of your Function
# Since you are heading toward Data Analysis and AI, using Booleans is better because you can use them directly in "if statements" later.

# Python
# def needs_upgrade(ram_size):
#     if ram_size < 16:
#         return True   # Notice: No quotes!
#     else:
#         return False  # Notice: No quotes!

# # Now we can use the result directly:
# if needs_upgrade(8):  # If only prints, if the if's conditions is True so for 50 (result = Nothing) but for <16 like 8 (result = Ordering new RAM stick... )
#     print("Ordering new RAM stick...")

#-------------------------

## ✏️ Exercise 6.3: The "Multiple Parameter" Tool
# Most IT tools need more than one piece of info. Let's build a function that takes two inputs: username and is_admin.

# Define the function: def generate_access_label(username, is_admin):
# Inside the function:
# IF is_admin is True:
# return f"ADMIN: {username}"
# ELSE:
# return f"USER: {username}"
# Test it with two calls:
# print(generate_access_label("Daniel", True))
# print(generate_access_label("Guest_User", False))

# ❓ Check-in
# Does it make sense how the function "matches" the inputs? 
# (The first thing you type becomes username, and the second becomes is_admin).
# Do you see why True (without quotes) is more powerful than just the word "True"?

# def generate_access_label(username, is_admin):
#     if is_admin is True:
#         return f"ADMIN:{username}"
#     else:
#         return f"USER:{username}"
# # Test Calls
# print(generate_access_label("Dani", False))
# print(generate_access_label("Maria", True))

# Result = USER:Dani
#          ADMIN:Maria

### Why "is" is dangerous for other things ???
# If you tried to use is with numbers or strings, your code would eventually break.

# a = 500
# b = 500

# print(a == b) # True (The values are the same)
# print(a is b) # False (They are two different '500' objects in memory)

## The "Pythonic" Way
# In Python, you actually don't need "is" or "==" when "working with booleans". 
# Since is_admin is already True or False, you can just evaluate it directly:

# def generate_access_label(username, is_admin):
#     if is_admin:  # This is the cleanest, most "Pythonic" way # here if only runs if the Condition is True or jumps to else or terminates
#         return f"ADMIN:{username}"
#     return f"USER:{username}"  # Here u don't even need to write else, it's already understood

##### The Rule of Thumb:
## Use "==" for almost everything (numbers, strings, lists).

## Use "is" only when checking for None.

## Use "the variable" itself (e.g., if is_admin:) for booleans.
#-----------------------------

### 🚀 Step 6.4: The "Real-World" Loop + Function Combo
# This is the ultimate test of everything you’ve learned so far. 
# We are going to take a List of Dictionaries and process them using a Function.

### This is how enterprise-level software works:
## The Data (The List)
## The Logic (The Function)
## The Engine (The Loop)

## ✏️ Final Challenge: The "Storage Alert" System
# You have a list of servers, and you need to flag which ones are running out of disk space.

# Define a function called check_storage(percent_used):
# IF percent_used is greater than 90, return "CRITICAL 🚨"
# ELIF percent_used is greater than 75, return "WARNING ⚠️"
# ELSE, return "Healthy ✅"
# The Data:
# Python
# servers = [
#     {"id": "Srv-A", "usage": 95},
#     {"id": "Srv-B", "usage": 40},
#     {"id": "Srv-C", "usage": 82}
# ]
# The Engine (The Loop):
# Loop through the servers.
# Inside the loop, call your function: status = check_storage(server["usage"])
# Print: f"Server {server['id']} is {status}"

# ❓ Check-in
# Do you see how the Function handles the "Thinking," while the Loop handles the "Work"?
# Can you imagine how easy it would be to change your "Warning" threshold from 75 to 80? You'd only have to change one line in your function, even if you had a million servers!

# Data
# servers = [
#      {"id": "Srv-A", "usage": 95},
#      {"id": "Srv-B", "usage": 40},
#      {"id": "Srv-C", "usage": 82}
# ]

# # Logic
# def check_storage(percent_used):
#     if percent_used > 90:
#         return "CRITICAL 🚨"
#     elif percent_used > 75:
#         return "WARNING ⚠️"
#     else:
#         return "Healthy ✅"

# # The Engine (The Loop):
# for s in servers:
#     status = check_storage(s['usage'])
#     print(f" Server:{s['id']} is {status}")

# Result =  Server:Srv-A is CRITICAL 🚨
#           Server:Srv-B is Healthy ✅
#           Server:Srv-C is WARNING ⚠️

### So everything that starts with "is_" is considered as boolean and true ????

## That is a fantastic observation! You’ve just spotted one of the most important "unwritten rules" of professional programming.
## Strictly speaking, the computer doesn't care what you name a variable. You could call a Boolean potato = True, and it would work. 
# However, in the IT and AI world, we use "Naming Conventions" to make code readable for other humans (like your teammates or Ms. Bom).

## 🏷️ The "is_" Convention
# When a variable or function starts with is_, has_, or can_,
# it is a strong signal to other programmers that the value inside is a Boolean (True or False).

# Variable Name	  Likely Data Type	   What it's asking
# is_admin	      Boolean	           Is this person an admin? (Yes/No)
# has_ssd	      Boolean	           Does this laptop have an SSD? (Yes/No)
# can_reboot	  Boolean	           Is the server allowed to reboot? (Yes/No)
# user_name	      String	           What is the name?
# ram_gb	      Integer	           How much RAM is there?


## 🧠 Is it always True?
# Not necessarily! The is_ part is just the label on the box.

# If is_admin = True, the box contains "Yes."
# If is_admin = False, the box contains "No."

# The beauty of this naming style is how it reads in an if statement. It sounds like English:
# if is_active: or if is_locked:
#-------------------------------

## ✏️ Final Challenge: The "Storage Alert" System
# Before we wrap up Step 6, let's see you put that "Naming Convention" and "Function Logic" into action with the Storage Alert exercise.

# Function: def get_status(percent):
# > 90: Return "CRITICAL 🚨"
# > 75: Return "WARNING ⚠️"
# Else: Return "Healthy ✅"
# Data:
# servers = [
#     {"id": "Srv-A", "usage": 95},
#     {"id": "Srv-B", "usage": 40},
#     {"id": "Srv-C", "usage": 82}
# ]
# Loop: Run through the list and print the status for each.

# ❓ Check-in
# Can you see how using a name like is_full would be better than just full?
# Does the if/elif/else structure inside a function feel like a "brain" that processes the numbers you feed it?

# 1st Data:
servers = [
    {"id": "Srv-A", "usage": 95},
    {"id": "Srv-B", "usage": 40},
    {"id": "Srv-C", "usage": 82}
]

# 2nd logic
def get_status(percent):
    if percent > 90:
        return "CRITICAL 🚨"
    elif percent > 75:
        return "WARNING ⚠️"
    else:
        return "Healthy ✅"

# 3rd Engine(loop)
for s in servers:
    #result = get_status(s['usage']) # 1st try to check output

    #result = (f"{s['id']}: {get_status(s['usage'])}") # 2nd try with server name & server status

    result = (f"{s['id']}: with {s['usage']}% usage is {get_status(s['usage'])}") # 3rd try with structured sentence server name & server status

    print(result) # 3rd one used

# Result = Srv-A: with 95% usage is CRITICAL 🚨
#          Srv-B: with 40% usage is Healthy ✅
#          Srv-C: with 82% usage is WARNING ⚠️

## Look at that! You didn't just write the code; you iterated like a professional developer.
# Your "3rd try" is the perfect balance of data and human-readable reporting. You’ve successfully combined:

## Data Structures (List of Dictionaries)
## Custom Logic (The Function)
## Iteration (The Loop)
## String Formatting (The F-string)

## 🔍 Why your 3rd Try is the "Senior Analyst" Choice
# In IT, if you just print CRITICAL 🚨, your boss won't know which server is dying. 
# If you print Srv-A: CRITICAL 🚨, they still don't know why. 
# By including the usage %, you’ve provided the Context along with the Status.

# 🛠️ A Quick Look Under the Hood
# When you run that loop, here is what Python is doing "behind the scenes":

# Step 1: Grabs Srv-A.
# Step 2: Sees usage: 95.
# Step 3: Teleports that 95 into the get_status function.
# Step 4: The function hits the first if, says "Yep, 95 is > 90," and teleports CRITICAL 🚨 back out.
# Step 5: Your F-string catches that result and prints the final line.

###🎓 You have completed the Fundamentals!
## You now have the "Core Four" skills needed for both IT Automation and AI Development:

## Variables & Types (Strings, Integers, Booleans)
## Logic & Comparison (If/Elif/Else, and/or/not)
## Containers (Lists & Dictionaries)
## Reusability (Loops & Functions)

# ❓ What's Next?
# We can go in two directions now:
# Option A: Error Handling (try/except) – How to stop your code from "crashing" when it hits a server that is missing data (e.g., a server with no usage key).
# Option B: Libraries & Modules – Learning how to use "pre-built" tools to do things like check your actual computer's RAM or create a file on your desktop.
# Which path sounds more interesting for your IT Support and AI goals?