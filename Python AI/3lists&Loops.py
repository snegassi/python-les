

# 📦 Step 3: Handling "Groups" of Data (Lists)
# In Data Analysis and AI, we never work with just one battery_level or one username. 
# We work with thousands of them at once.

# To do this, we need a "Container." In Python, this container is called a "List".

# 💡 What is a List?
# Think of a variable like a single box. A list is like a bookshelf with many slots. 
# Each slot has a number (an address) so you can find what's inside called "Index".

# The Rules of a List:
# It starts and ends with square brackets [].
# Every item is separated by a comma ,.
# CRITICAL: Computers start counting at 0, not 1.

# 💻 Try this in VS Code
# Create a file called my_data.py:

## ✏️ Exercise 3.1: The "Inventory" List
## Let's practice building and "peeking" into a list. In VS Code:

# 1) Create a list called stock_prices = [150, 200, 300, 50].
# 2) The Task: Use a print statement to show the second item in the list (Remember the "0" rule!).
# 3) The Logic Mix: Write an Independent If statement that checks:
#    IF the last item (stock_prices[3]) is less than 100, print "🚨 Alert: Low Price Detected!".
# When you run this, does the "Alert" trigger correctly? Once you're comfortable "grabbing" items from a list by their number, 
# I'll show you how to change them!

# stock_prices = [150, 200, 300, 50]
# print(stock_prices[1]) # 2nd item
# if stock_prices[3] < 100:
#     print("🚨 Alert: Low Price Detected!")

# Result = 200,
#          🚨 Alert: Low Price Detected!, Since stock_prices[3] = 50 by index 3

# Perfect! You nailed the "Index 0" rule. Even though 200 is the second item to a human, to Python, it is at Index 1. 
# And since 50 is at Index 3, your logic correctly triggered the alert.

# This is the foundation of Data Analysis: being able to point to a specific "cell" or "row" of data and run a check on it.
#----------------

## 🛠️ Step 3.2: Updating and Adding to Lists
# In Cloud Computing or Web Development, lists are constantly changing. New users sign up, or stock levels go down. 
# You need to know how to change a list after you've created it.

## There are two main ways to do this:

# Changing an Item: Point to the index and give it a new value. 

# Adding an Item: Use .append() to tack a new item onto "the very end".

#-----------------
# ✏️ Exercise 3.2: The "Inventory Manager"
# Let's practice managing a list. In VS Code:

# Create a list called item_counts = [10, 5, 2].
# Task 1 (Update): Change the first item (Index 0) from 10 to 15.
# Task 2 (Add): Use .append() to add a new count of 8 to the end of the list.
# Task 3 (The Independent Check):
# IF the third item (Index 2) is less than 5, print "🚨 Warning: Item 3 is low stock!".
# What does your final list look like when you print it? (Once you're comfortable with this, 
# I'll show you how to find out "How long" a list is, which is the last step before we start Automating!)

item_counts = [10, 5, 2]

# To Update/Change item
item_counts[0] = 15
print(item_counts)

# To Add item
item_counts.append(8)
print(item_counts)

# Independent Check
if item_counts[2] < 5:
    print("🚨 Warning: Item 3 is low stock!")

# Result = [15, 5, 2]
#          [15, 5, 2, 8]
#          🚨 Warning: Item 3 is low stock!

# Spot on! You just performed a dynamic data check. Because the list started with 4 items, your if statement caught the error. Then, by appending an item, you changed the state of the data, and your "re-measure" proved the list grew to 5.
# In the world of IT Support and Data Analysis, this is exactly how we validate that a file isn't empty or that a log has enough entries to be useful.
#---------------------------

##🏎️ Step 4: The Power of Automation "(For Loops)""
## This is the "Magic Trick" of Python.
## Up until now, if you had a list of 100 items and wanted to check each one, you would have to write 100 if statements. 
# That’s a lot of typing! A "For Loop" allows you to write the logic once, and Python will "walk" through the entire list and apply that logic to every single item automatically.

## 💡 How the "Walk" Works
# Think of the For loop like a conveyor belt.

## The List is the belt.

## The Loop is the worker standing by the belt.

## The Variable (we often call it item or x) is the worker's hand grabbing one thing at a time.
#-------------------------

## ✏️ Exercise 4.1: The "Log File" Scanner
# Imagine you are an IT Analyst looking at a list of login attempts. Some are "Success" and some are "Failed".

# 1) Create a list: logs = ["Success", "Failed", "Success", "Success", "Failed"].
# 2) Create a for loop to go through the logs. (Use for status in logs:).
# 3) Inside the loop (Indented/Tabbed):
#    - Write an Independent If: If status == "Failed", print "⚠️ Security Warning: Failed Login Detected!".
#    - Else, print "Login OK.".
# The Big Question: When you run this, does it print 5 separate lines in your terminal?
# This is your first step into Automation. Instead of checking each log entry by hand, 
# you just gave Python a set of instructions and let it do the work! How does the output look?

# List is the Belt
logs = ["Success", "Failed", "Success", "Success", "Failed"]
# For loop is Worker
for status in logs:   # "status" indicated Single item of the list at a time
    if status == "Failed":
        print("⚠️ Security Warning: Failed Login Detected!")
    else:
        print("Login OK.")

# Result = Login OK.
#          ⚠️ Security Warning: Failed Login Detected!
#          Login OK.
#          Login OK.
#          ⚠️ Security Warning: Failed Login Detected!
