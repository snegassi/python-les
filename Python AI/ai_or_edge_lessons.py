
# the code to comment = cntrl + /

# astr = 'Hello Bob'
# aa=[4,5,6,7]
# istr = str(astr)
# print(len(aa))
# print('First', istr)
# print(isinstance(istr,int))

#stuff = dict()
#print(stuff.get('candy',7))#?? is this stating that key is candy & value to it is 7
#print(stuff['candy'])#???? is this because the dictionary is enmpty now


## To make our output look professional (like a real website or app), we use F-Strings. 
## It stands for "Formatted String." It lets us put variables directly inside a sentence.
# coffee_price = 5.50
# cups_per_week = 7
# total_spent = coffee_price * cups_per_week
# print(f'I spend {total_spent} on coffee per week')


##if you're building a website that gives different access levels based on age:
# my_age = 15

# if my_age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# print("Budget check complete.") # this line will print everytime because its un-indented


##--The "Security Gate" Challenge of Logic conditions--
# username= "admin"
# password = "wrong123" # 0r change the password to "wrong123" to see another effect

# if username == "admin" and password == "secret123": # both conditions have to be true for the if conditon as a whole to work if not, it fails & goes to the next condition
#     print("Access Granted")
# else:
#     print("Access Denied")

##----🚦 Independent Ifs vs. If/Elif----
##--if / elif / else--: This is like a multiple-choice question. 
# Only one answer can be chosen. Once Python finds a "True" one, it skips the rest.

##--Multiple if statements--: This is like a " checklist".
# Python checks every single one, regardless of whether the one before it was true or false.
# OR
#Python treats every if like a brand new question. It doesn't care if the one before it was true or false.
# It checks every single one.

#----let's build a "Game Score Checker"---
# score = 150
# lives_left = 3

# if score > 100:
#     print("Level 1 Complete")
# if lives_left > 0:
#     print("Still in the game")

##--- When you put one if/elif/else block and then start a new if block below it, you are creating multiple independent checklists.
##---- 💡 Why would we do this?
# We do this when we have different categories of questions that don't depend on each other.

#-----Think of a Movie Theater App:--Example-1
#---Category 1: What is the ticket price based on age? (if/elif/else)
#---Category 2: Does the user want popcorn? (if/else)
# One doesn't stop the other from happening.

# --- OUR DATA ---
# age = 25
# has_coupon = True

# # --- CHECKLIST 1: Ticket Price (One Choice Only) ---
# if age >= 60:
#     print("Ticket: $8 (Senior)")
# elif age <= 12:
#     print("Ticket: $5 (Child)")
# else:
#     print("Ticket: $12 (Adult)")

# # --- CHECKLIST 2: Discount (Separate Question) ---
# if has_coupon == True:
#     print("Discount: Applied 20% off!")
# else:
#     print("Discount: None")

#---The "Online Store" Challenge--Example-2
# Let's try coding a "Double Checklist" yourself to lock this in.

# Create a variable order_total = 150.
# Create a variable shipping_type = "Express".
#---Block 1 (Tax Check):-----
# If order_total > 100, print "High Value Tax Applied".
# Else, print "Standard Tax Applied".
#---Block 2 (Shipping Check - Separate):----
# If shipping_type == "Express", print "Shipping in 1-2 days".
# Else, print "Shipping in 5-7 days".

# order_total = 150
# shipping_type = "Express"

# #--Block 1 (Tax Check)
# if order_total > 100:
#     print("High Value Tax Applied")
# else:
#     print("Standard Tax Applied")

# #--Block 2 (Shipping Check - Separate)
# if shipping_type == "Express":
#     print("Shipping in 1-2 days")
# else:
#     print("Shipping in 5-7 days")



##----Question---Can these independent checklists be dependent on each other? l
# ike lets say the output of the first is needed used by the second one ?

# Gemini said
# You have just hit on the exact way that data analysis and AI pipelines are built!
# The answer is yes. In fact, this is how we "pass the baton" from one piece of logic to another. 
# To do this, we usually use a Variable to store the result of the first checklist, 
# and then the second checklist looks at that variable.

#----💻 How it Works in VS Code (The "Baton Pass")----
# Imagine you are building a website's checkout.
# Checklist 1: Calculates the price.
# Checklist 2: Uses that price to decide if the user gets free_shipping.
##----Example-1---
# # --- INITIAL DATA ---
# item_type = "Electronics"
# order_total = 0 # We start at 0

# # --- CHECKLIST 1: Set the Price ---
# if item_type == "Electronics":
#     order_total = 150
# else:
#     order_total = 50

# # --- CHECKLIST 2: Check for Free Shipping (Dependent on Checklist 1) ---
# if order_total > 100:
#     print(f"Total is ${order_total}. You get FREE shipping!")
# else:
#     print(f"Total is ${order_total}. Shipping is $10.")
# Why this is powerful: The second checklist doesn't care how the order_total became 150.
#  It only cares about the current value of the variable.
#  This keeps your code organized and easy to read.

##-----Example-2----
# ✏️ Exercise 2.9: The "AI Game Difficulty" Challenge
# Let's try a "Baton Pass" yourself. 
# This is how a game AI might decide how hard to make a level.

# In VS Code:
# Create a variable player_score = 250.
# Create a variable difficulty_level = "Easy" (This is our starting point).
# Block 1 (The Logic):
# IF player_score > 200, change difficulty_level to "Hard".
# (You don't need an else here if you want it to stay "Easy" otherwise).

# Block 2 (The Output):
# Write an Independent If that checks: IF difficulty_level == "Hard", print "Warning: Boss Fight Initiated!".
# Write an Else for that second block that prints "Keep exploring...".
# Test it out:
# Run it with player_score = 250. Do you see the warning?
# Change player_score to 50. Does it say "Keep exploring"?
# This is a huge milestone! You’ve moved from simple "Yes/No" questions to Systems Thinking.
#  How does your code look?

# player_score = 50 # this is the one that change
# difficulty_level = "Easy"
# #---Block 1(logic)
# if player_score > 100:
#     difficulty_level = "Hard"
# # (You don't need an else here if you want it to stay "Easy" otherwise).

# #---Block 2(The Output/Decision)
# if difficulty_level == "Hard":
#     print("Warning: Boss Fight Initiated!")
# else:
#     print("Keep exploring...")
# In the world of Data Analysis and AI, this is a huge concept. 
# You took "Raw Data" (the score), processed it through "Logic" (the first if block) 
# to create "New Information" (the difficulty level), and then used that information to drive a "Decision" (the second if block).

###------ 🚦 The "Logic" Milestone------
# Once you finish this exercise, you will have mastered:
# Single If/Else (One choice).
# If/Elif/Else (One choice out of many).
# Independent Ifs (The Checklist).


## ------🪜 The "Staircase" (Nested Ifs)------
# In our "Checklist" (Independent Ifs), the two questions didn't care about each other.

# In a Staircase, the second question only exists if the first answer was "Yes."
# If the first answer is "No," Python skips the whole staircase and walks away.

# 💻 Step-by-Step Exercise 2.17: The "VIP Entry"
# Let's use the simplest variables possible to see the "Staircase" in action. 
# Copy this into VS Code:

# Python
# # --- OUR DATA ---
# has_ticket = True
# is_vip = True

# # --- THE STAIRCASE ---
# if has_ticket == True:
#     print("1. Ticket Accepted! Welcome to the show.")

#     # This next part is INDENTED (Tabbed). 
#     # It ONLY runs if 'has_ticket' was True.
#     if is_vip == True:
#         print("2. 🌟 VIP Status detected! Proceed to the Lounge.")

# # This is NOT indented, so it runs no matter what.
# print("End of security check.")
# 💡 Why is this different?
# If you change has_ticket to False, Python hits the first line, sees it's false, and jumps all the way to the bottom.
# It won't even look at the VIP variable, because without a ticket, VIP status doesn't matter!


##-------💻 Exercise 2.18: The "Smart Home" System------
# Let's build this in VS Code. We will have one independent check for the Alarm, and one nested check for the Lights.

# Python
# # --- OUR DATA ---
# is_alarm_on = True
# is_dark = True
# is_someone_home = False

# # --- BLOCK 1: Independent Alarm Check ---
# if is_alarm_on == True:
#     print("🚨 Security System: Active.")
# else:
#     print("🔓 Security System: Off.")

# # --- BLOCK 2: Independent Light Check (with a Staircase!) ---
# if is_dark == True:
#     print("🌙 It is dark outside.")
    
#     # NESTED IF: We only care if someone is home if it's dark!
#     if is_someone_home == True:
#         print("💡 Action: Turning lights on.")
#     else:
#         print("🔋 Action: Keeping lights off to save power.")

#------💡 Why the above works:------
# Independence: The Alarm check doesn't care if it's dark or if someone is home. It does its job and moves on.
# Nesting: The "Turning lights on" message cannot happen unless it is both dark AND someone is home.

###--------You have now mastered the three "Golden Rules" of Python Logic:------

# The Choice: if/elif/else (Pick only one path).
# The Checklist: if + if (Independent checks).
# The Staircase: if inside if (One check depends on another 
# or the 1st if must be true for the inside/2nd if to run).



###------📦 Step 3: Handling "Groups" of Data (Lists)------
# In Data Analysis and AI, we never work with just one battery_level or one username. 
# We work with thousands of them at once.

# To do this, we need a "Container." In Python, this container is called a List.

# 💡 What is a List?
# Think of a variable like a single box. A list is like a bookshelf with many slots. 
# Each slot has a number (an address) so you can find what's inside.

# The Rules of a List:
# It starts and ends with square brackets [].
# Every item is separated by a comma ,.
# CRITICAL: Computers start counting at 0, not 1.

#------💻 Exercise 3.0: Try this in VS Code---------------
# Create a file called my_data.py:

# Python
# # --- OUR DATA ---
# # A list of sensor readings for an AI 
# readings = [25, 30, 85, 12, 100]

# # 1. Print the whole bookshelf
# print(readings)

# # 2. Print just the FIRST item (Index 0)
# print(f"The first reading is: {readings[0]}")

# # 3. Print the THIRD item (Index 2)
# print(f"The third reading is: {readings[2]}")


#----------- ✏️ Exercise 3.1: The "Inventory" List-----------------
# Let's practice building and "peeking" into a list. In VS Code:

# Create a list called stock_prices = [150, 200, 300, 50].
# The Task: Use a print statement to show the second item in the list (Remember the "0" rule!).
# The Logic Mix: Write an Independent If statement that checks:
# IF the last item (stock_prices[3]) is less than 100, print "🚨 Alert: Low Price Detected!".
# When you run this, does the "Alert" trigger correctly?

# Once you're comfortable "grabbing" items from a list by their number,
#  I'll show you how to change them!

# creating list
# stock_prices= [150,200,300,50]
# print(stock_prices[1])

# if stock_prices[3] < 100:
#     print("🚨 Alert: Low Price Detected!")


##------------ 🛠️ Step 3.2: Updating and Adding to Lists------------------------
# In Cloud Computing or Web Development, lists are constantly changing.
#  New users sign up, or stock levels go down. 
# You need to know how to change a list after you've created it.

# There are two main ways to do this:
# Changing an Item: Point to the index and give it a new value.
#OR
# Adding an Item: Use .append() to tack a new item onto the very end.

#---------- 💻 Try this in VS Code-------------
# Create a file called update_list.py:

# Python
# # --- INITIAL DATA ---
#users = ["Alice", "Bob", "Charlie"]

# # 1. Change Bob to "Robert" (Index 1)
# users[1] = "Robert"
# print(f"Updated list: {users}")

# # 2. Add a new user to the end
#users.append("David")
#print(f"List after append: {users}")

#Soo
#-------------✏️ Exercise 3.2: The "Inventory Manager"----------------------
# Let's practice managing a list. In VS Code:
# Create a list called item_counts = [10, 5, 2]
# Task 1 (Update): Change the first item (Index 0) from 10 to 15.
# Task 2 (Add): Use .append() to add a new count of 8 to the end of the list.
# Task 3 (The Independent Check):
#IF the third item (Index 2) is less than 5, print "🚨 Warning: Item 3 is low stock!".

# item_counts = [10, 5, 2]
# item_counts[0]=15 #change the value
# item_counts.append(8)
# print(item_counts)
# if item_counts[2] <5:
#     print("🚨 Warning: Item 3 is low stock!")


##------ 📏 Step 3.3: The "Tape Measure" (len)----
# In AI and Web Development, you often don't know how big a list is. 
# A website might have 10 users today and 1,000 tomorrow. 
# To handle this, Python has a built-in "Tape Measure" called len().

# len is short for Length. It tells you exactly how many items are in the list.

#----💻 Try this in VS Code----
# Create a file called measure.py:

# Python
# # --- OUR DATA ---
# guest_list = ["Alice", "Bob", "Charlie", "David"]

# # 1. Measure the list
# number_of_guests = len(guest_list)

# # 2. Print the result
# print(f"There are {number_of_guests} guests on the list.")

# # 3. Use it in Logic
# if len(guest_list) > 3:
#     print("⚠️ Warning: The room is getting crowded!")

# guest_list = ["Alice", "Bob", "Charlie", "David"]
# number_of_guests= len(guest_list)
# print(number_of_guests)
# print(f"There are {number_of_guests} guests on the list.")
# if len(guest_list) >3:
#     print("⚠️ Warning: The room is getting crowded!")


#----- ✏️ Exercise 3.3: The "Data Audit"--------
# Let's practice using the "Tape Measure" with the logic we've already mastered.

# In VS Code:
# Create a list called sensor_data = [1.5, 2.3, 0.9, 4.1].
# Task 1 (Measure): Create a variable called data_count that stores the length of the list using len().
# Task 3 (Independent Check):
#    IF data_count is less than 5, print "🚨 Error: Not enough data for analysis!".
# Task 4 (Update): Use .append() to add a new number, 3.3, to the list.
# Task 5 (Re-Measure): Print the new length of the list.
# Does the error message disappear if you add enough items to the list? 
# Once you've got the hang of measuring lists, we are officially ready for the "Big Reveal":
# Automating these checks so you don't have to write them one by one!

# sensor_data = [1.5, 2.3, 0.9, 4.1,7]
# data_count = len(sensor_data)
# if data_count < 5:
#     print("🚨 Error: Not enough data for analysis!")

# sensor_data.append(3.3)
# print(len(sensor_data))


##-------------- 🏎️ Step 4: The Power of Automation (For Loops)--------------------
# This is the "Magic Trick" of Python.

# Up until now, if you had a list of 100 items and wanted to check each one, 
# you would have to write 100 if statements. That’s a lot of typing! 
# A "For Loop " allows you to write the logic once, and Python will "walk" through the entire list and apply that logic to every single item automatically.

##-------------- 💡 How the "Walk" Works----------------------
# Think of the loop like a conveyor belt.

# The List is the belt.

# The Loop is the worker standing by the belt.

# The Variable (we often call it item or x) is the worker's hand grabbing one thing at a time.

# 💻 Try this in VS Code
# Create a file called my_first_loop.py:

# Python
# # --- OUR DATA ---
# temperatures = [72, 101, 68, 105, 70]

# # --- THE LOOP ---
# # 't' is our temporary nickname for "the item I am holding right now"
# for t in temperatures:
#     print(f"Checking temp: {t}")
    
#     # We can put our Logic inside the loop!
#     if t > 100:
#         print("🚨 ALERT: Overheating!")
#     else:
#         print("✅ Temperature is normal.")

# print("Done checking all sensors.")
#-----------------------------------------------------------
##------------- ✏️ Exercise 4.1: The "Log File" Scanner
# Imagine you are an IT Analyst looking at a list of login attempts.
#  Some are "Success" and some are "Failed".

# In VS Code:
# Create a list: logs = ["Success", "Failed", "Success", "Success", "Failed"].
# Create a for loop to go through the logs. (Use for status in logs:).
# Inside the loop (Indented/Tabbed):
# Write an Independent If: If status == "Failed", print "⚠️ Security Warning: Failed Login Detected!".
# Else, print "Login OK.".
# The Big Question: When you run this,does it print 5 separate lines in your terminal?

# This is your first step into Automation. Instead of checking each log entry by hand, 
# you just gave Python a set of instructions and let it do the work! How does the output look?

# logs = ["Success", "Failed", "Success", "Success", "Failed"]
# for status in logs:
#     if status == "Failed": # i from the above MUST be used here 
#         print("⚠️ Security Warning: Failed Login Detected!")
#     else:
#         print("Login OK.")


##------------------ 🛠️ Step 4.2: The "Accumulator" (The Running Total)
# In Data Analysis, we don't just want to print things; we want to count things.
#  How many people failed to log in? What is the total of all sales?

# To do this, we create a variable outside the loop (starting at 0) and update it inside the loop.

# 💻 Try this in VS Code
# Create a file called counter.py:

# Python
# # --- OUR DATA ---
# sales = [10, 50, 100, 20]
# total_money = 0  # We start at zero

# # --- THE LOOP ---
# for s in sales:
#     # Add the current sale to our running total
#     total_money = total_money + s
#     print(f"Added {s}. Current total is: {total_money}")

# # --- THE RESULT ---
# print(f"--- FINAL SALES TOTAL: ${total_money} ---")
#------------------------------------------------------------------------

## -------------✏️ Exercise 4.3: The "Error Counter"
# Let's combine your "Security Scanner" with a "Counter." This is exactly how IT dashboards track system health.

# In VS Code:
# Create a list: status_codes = [200, 404, 200, 500, 200].
# (Note: 200 means "OK", anything else is an error!)
# Create a variable error_count = 0.
# The Loop: for code in status_codes:
# Inside the Loop (Tabbed):
#   IF code != 200: (The != means "Not Equal To")
#   Print "Found an error: [code]".
#   Add 1 to your counter: error_count = error_count + 1.
# Outside the Loop (No Tab):
# Print "Total Errors Found: [error_count]".

# When you run this, does it correctly count the 2 errors (404 and 500)?
#  Why this matters: You are now moving from just "looking" at data to "calculating" results from data. 
# This is the heart of building AI Agents—they take in a list of information and give you a summary! 
# How did the counting go?

# status_codes = [200, 404, 200, 500, 200]
# error_count = 0

# for code in status_codes:
#     if code != 200:
#         print(f"Found an error: {code}")# I had to use f-string here & blow, inorder to print the code and error_count varibles
#         error_count = error_count + 1

# print(f"Total Errors Found: {error_count}")

##--- Another exercise for loop---
##------------------ ✏️ Exercise 4.5: The "Server Status" Monitor---------
# In this one, we are checking a list of server response times (in milliseconds). 
# Any time over 500ms is considered "Slow."

# In VS Code:
# Create a list: response_times = [100, 550, 200, 800, 450].
# Create a counter: slow_count = 0.
# The Loop: for time in response_times:
# Inside the Loop:
# IF time > 500:
# Print an F-string: "⚠️ Warning: {time}ms is too slow!".
# Add 1 to your counter using the shortcut: slow_count += 1.
# Outside the Loop:
# Print an F-string showing the total number of slow servers.

# response_times = [100, 550, 200, 800, 450]
# slow_count = 0  # If it takes more time to respond means it "Slow Server" hence slow_count

# for time in response_times:
#     if time > 500:
#         print(f"⚠️ Warning: {time}ms is too slow!")
#         slow_count += 1  #difference between += time (summing the numbers "of value time") and += 1 (counting the items "number of servers") make sense
# print(f"The total number of slow servers is {slow_count}")

##---------Another exercise for loop---
##------- ✏️ Exercise 4.6: The "Email Filter" (Independent + Loop)---------
# As an IT Support Analyst, you might need to separate "Internal" emails from "External" ones for security.

# In VS Code:
# Create a list: emails = ["boss@company.com", "hacker@gmail.com", "hr@company.com", "client@yahoo.com"].
# Create two empty lists: internal = [] and external = [].
# The Loop: for address in emails:
# Inside the Loop:
# IF "@company.com" in address:
# Append the address to the internal list.
# ELSE:
# Append the address to the external list.
# Outside the Loop:
# Print both lists using F-strings to see your "Sorted" data.

# ❓ Quick Check-in
# Take your time with these in VS Code.
# !!!! One thing to watch for: Make sure your internal = [] and external = [] are outside (above) the start of the loop.
# If you put them inside, Python will "reset" them to empty every time the loop spins!

# emails = ["boss@company.com", "hacker@gmail.com", "hr@company.com", "client@yahoo.com"]
# internal = []
# external = []

# for address in emails:
#     if "@company.com" in address:
#         internal.append(address)
#     else:
#         external.append(address)
# print(f"for internal address list = {internal}")   
# print(f"for external address list = {external}")   
#           
##If you put an = sign inside the curly braces like this {internal=}, 
# Python will automatically print the name of the variable and its value for you.
# Try this in your VS Code terminal:
# print(f"{internal=}")
# Output: internal=['boss@company.com', 'hr@company.com']


##You hit the nail right on the head! You’ve perfectly identified the difference between "Partial Match" and "Exact Match".
# 🔍 2) The "In" vs. "==" Distinction
# You are 100% correct.
# == (Exact Match): This is like a fingerprint scanner. If you wrote if address == "@company.com", it would only be true if the person's email address was literally just those 12 characters. Since no one has the email address "@company.com", your list would stay empty!

# in (Partial Match): This is like a metal detector. It doesn't care what else is in your pocket; it’s just looking to see if any part of the "address" contains that specific string of text.

# #🛠️ Exercise 4.7: The "Final Boss" of Loops & Logic
# Since you understood the += 1 (counting) vs. += value (summing) distinction, 
# let's do one "Master Exercise" that combines everything we've learned so far:
# 1)A List of data.
# 2)A For Loop to automate it.
# 3)A Counter (to see how many).
# 4)A Sum (to see how much).
# 5)An Independent If check.

# The Scenario: You are auditing a list of cloud storage folders. Some are "Oversized" (over 100GB).
# In VS Code:
# Create a list: folder_sizes = [20, 150, 80, 300, 45].
# Create two variables: oversized_count = 0 and total_oversized_gb = 0.
# The Loop: for size in folder_sizes:
# Inside the Loop:
# IF size > 100:
# Print: f"⚠️ Found huge folder: {size}GB"
# Count it: Add 1 to oversized_count.
# Sum it: Add the size to total_oversized_gb.
# Outside the Loop:
# Print the final count of big folders.
# Print the total GB occupied by those big folders.
# When you finish this, tell me: * What was the final oversized_count?
# What was the final total_oversized_gb?
# I'll be right here to check your logic once you've run it!

# folder_sizes = [20, 150, 80, 300, 45]
# oversized_count = 0 # this is for += time (summing the numbers)
# total_oversized_gb = 0 # this is for += 1 (counting the items)

# for size in folder_sizes:
#     if size > 100:
#         print(f"⚠️ Found huge folder: {size}GB")
#         oversized_count += 1 # Count it: Add 1 to oversized_count
#         total_oversized_gb += size # Sum it: Add the size to total_oversized_gb
# print(f"final count of big folders: {oversized_count = }") # the = makes the value name and the value to be printed
# print(f"total GB used by big folders: {total_oversized_gb = }") # the = makes the value name and the value to be printed

##---🚦 The "Master of Logic & Loops" Checkpoint-------
# You have officially mastered the "Big Three" of Python automation:

# Lists: Storing groups of data.
# For Loops: Walking through every item in a list.
# If Statements inside Loops: Asking questions about each item as you walk.

##------------🔍 The "Reset" Trap (A Quick Conceptual Check)----------
# You correctly put oversized_count = 0 above the loop.

# "Outside the Loop: It's like a bucket sitting on the floor. 
# The loop walks by and drops a coin in it every time it finds a big folder.

# "Inside the Loop:"" If you put oversized_count = 0 inside the tabbed section,
# it would be like emptying the bucket every time you looked at a new folder. You would only ever have the "last" folder's result.

#-------------------End of LISTS, FOR LOOPS, & IF STATMENTS-------------

##------------- 📦 Step 5: Dictionaries (Data with Labels)-------------------
# Up until now, we’ve used Lists []. Lists are great for a simple row of items,
# but in IT Support and AI, we often need to store "Pairs" of information.

# For example, a User isn't just a name; they have an ID, an Email, and a Department.
# In Python, we use a Dictionary {} to map a "Key" to a "Value."

# 💡 The Anatomy of a Dictionary
# Curly Brackets: { }
# The Key: The label (e.g., "name")
# The Value: The data (e.g., "Gemini")
# The Colon: Separates them ("name": "Gemini")

# #------💻 Try this in VS Code
# Python
# # --- OUR DATA (The Dictionary) ---
# user_profile = {
#     "username": "IT_Pro_2026",
#     "access_level": "Admin",
#     "login_attempts": 3
# }

# # 1. Accessing data (We use the 'Key' like an index)
# print(f"User is: {user_profile['username']}") ## Just like List with index but here put the index within single/double quotes

# # 2. Updating data
# user_profile["login_attempts"] = 4
# print(f"Updated attempts: {user_profile['login_attempts']}")


##--------- ✏️ Exercise 5.1: The "Server Info" Card---
# Let's practice building a "label" for a piece of hardware.

# In VS Code:
# Create a dictionary called server:
# Set "ip" to "192.168.1.1"
# Set "status" to "Online"
# Set "ram_gb" to 16
# Task 1: Use an F-string to print: "The server at {ip} is currently {status}."
# Task 2 (The Logic Mix): Write an Independent If statement:
# IF server["ram_gb"] is less than 32, print "⚠️ Suggestion: Upgrade RAM for better performance."

# server = {"ip" : "192.168.1.1",
#            "status" : "Online",
#              "ram_gb" : 16
#                }

# # Task 1
# print(f"The server at {server["ip"]} is currently {server["status"]}") 
# # On some python editors,If you ever see a red squiggly line there, 
# # a common "pro" habit is to use single quotes for the keys inside the f-string, like this:
# #print(f"The server at {server['ip']} is currently {server['status']}")

# # Task 2
# if server["ram_gb"] < 32:
#     print("⚠️ Suggestion: Upgrade RAM for better performance.")
#-----------------------------------------------------------------------

##--------- 🔍 1) How does it feel using Curly Brackets {}?------
# Dictionaries are usually the "Aha!" moment for IT professionals. 
# While a List is just a pile of "data", a Dictionary is a "Database Record". It tells you exactly what every number means.

##--------- 🛠️ Step 5.2: Adding and Deleting from Dictionaries----------
# In IT Support, systems are dynamic. You might need to add a "Last Boot Time" to a server record or remove a "User" from a database.

# To Add/Update: Just assign a value to a new key.
# To Delete: Use the del keyword.

# 💻 Try this in VS Code
# Python
# device = {"type": "Laptop", "brand": "Dell"}

# # 1. Add a new piece of info
# device["os"] = "Windows 11"

# # 2. Change an existing piece of info
# device["brand"] = "Alienware"

# # 3. Remove a piece of info
# del device["type"]

# print(f"{device=}")


##------------------ ✏️ Exercise 5.2: The "Troublesit Ticket"------------------------
# Let's simulate an IT ticketing system.
# In VS Code:
# Create a dictionary called ticket:
# "id": 101
# "issue": "Blue Screen"
# "priority": "Low"
# Task 1 (Update): The issue is serious! Change the "priority" from "Low" to "High".
# Task 2 (Add): Add a new key called "assigned_to" and set it to your name.
# Task 3 (Logic Mix): * IF the priority is "High", print: "🚨 URGENT: Ticket {id} ({issue}) is assigned to {assigned_to}!"

# ticket = { "id": 101,
#           "issue": "Blue Screen",
#             "priority" : "Low"
            
#          }
# # Task 1 (Update):
# # Since The issue is serious, change:
# ticket["priority"]= "high"

# # Task 2 (Add):
# ticket["assigned_to"] = "Daniel"

# # Task 3 (Logic Mix):
# if ticket["priority"] == "high":
#     print(f"🚨 URGENT: Ticket {ticket["id"]} ({ticket["issue"]} is assigned to {ticket["assigned_to"]})!")


#######-------------- 🚀 Step 5.3: The "List of Dictionaries" (Real Data)----------------------
# In IT Support, you never have just one ticket. You have a List of tickets.
# This is where your two skills (Lists + Dictionaries) merge.

# 💻 Try this in VS Code
# Create a file called big_data.py:

# Python
# # A List of Dictionaries
# all_tickets = [
#     {"id": 101, "issue": "Blue Screen", "status": "Open"},
#     {"id": 102, "issue": "Password Reset", "status": "Closed"},
#     {"id": 103, "issue": "No Internet", "status": "Open"}
# ]

# # 1. Access the first ticket's issue
# print(f"Ticket 1 Issue: {all_tickets[0]['issue']}") # list [index of the dictionary frm list]['key']

# # 2. Loop through them!
# for t in all_tickets:
#     if t["status"] == "Open":
#         print(f"⚠️ Action Required: Ticket {t['id']} is still Open!") # Since we're picking one by one which is the index/t['key']

##------------------------ ✏️ Exercise 5.3: The "Inventory Audit"----------------
# This is a very common task for an IT Analyst. 
# You have a list of laptops, and you need to find which ones are "Outdated."

# In VS Code:

# Create a list called laptops:
# Laptop 1: {"id": "L01", "os": "Windows 11"}
# Laptop 2: {"id": "L02", "os": "Windows 10"}
# Laptop 3: {"id": "L03", "os": "Windows 11"}

# The Loop: for laptop in laptops:
# Inside the Loop:
# IF the os is not equal to "Windows 11":
# Print: f"🚨 Upgrade needed for Laptop: {laptop['id']}"
# How many laptops in your list need an upgrade? Once you can loop through a list of dictionaries,
# you have officially learned the "data structure" that 90% of the internet is built on "(it's called JSON)".

# needUpdate_laptops = 0
# laptops = [
#     {"id": "L01", "os": "Windows 11"},
#     {"id": "L02", "os": "Windows 10"},
#     {"id": "L03", "os": "Windows 11"}
# ]

# for laptop in laptops:
#     if laptop['os'] != 'Windows 11':
#         print(f"🚨 Upgrade needed for Laptop: {laptop['id']}")
#         needUpdate_laptops += 1
# print(f"This {needUpdate_laptops=} many laptos need Updates") # Added it on my own
#-------------------------------------------------------

##---------Great choice. In IT, we rarely check just one thing.
#  Usually, it’s a combination: "Is the OS old AND is the RAM too low?"

# To do this, we use the "and" keyword. 
# This acts "like a double-lock" on a door—both conditions must be True for the code inside to run.

##--------------✏️ Exercise 5.4: The "Hardware Refresh" Audit-------
# Your company is upgrading. Y
# ou only want to replace laptops that are both running an old OS and have low RAM.

# In VS Code:
# Create a list called inventory:
# {"id": "L01", "os": "Windows 10", "ram": 8}
# {"id": "L02", "os": "Windows 11", "ram": 8}
# {"id": "L03", "os": "Windows 10", "ram": 16}
# {"id": "L04", "os": "Windows 10", "ram": 4}

# Create a list called to_replace = [].

# The Loop: for device in inventory:
# Inside the Loop (The Complex Logic):
# IF device["os"] == "Windows 10" and device["ram"] < 16:
# Print: f"⚠️ High Priority Replace: {device['id']}"
# Append the device["id"] to your to_replace list.
# Outside the Loop:
# Print: f"Total laptops to order: {len(to_replace)}"
# Print the to_replace list.

# 🔍 Two Things to Watch For:
# The Logic: Only Laptops 01 and 04 should match both rules.
# (Laptop 03 has Windows 10, but its RAM is 16, so it's "safe" for now).

# The Brackets: Remember that device is your temporary name for the dictionary you are currently holding.

# How many laptops ended up in your to_replace list? 
# Once you run this, you're doing exactly what a System Administrator does to generate a budget report!

# inventory = [
#     {"id": "L01", "os": "Windows 10", "ram": 8},
#     {"id": "L02", "os": "Windows 11", "ram": 8},
#     {"id": "L03", "os": "Windows 10", "ram": 16},
#     {"id": "L04", "os": "Windows 10", "ram": 4},
# ]

# to_replace = []

# for device in inventory:
#     if device["os"] == "Windows 10" and device["ram"] < 16:
#         print(f"⚠️ High Priority Replace: {device['id']}")
#         to_replace.append(device["id"])

# print(f"Total laptops to order: {len(to_replace)}")
# #print(dir(to_replace))

##------The above would not work , so i aske gemeni to help?--------
# This is a classic "IT Support" moment! Your logic is perfect, but you’ve been hit by a String Mismatch.
# In Python, a string must be a 100% exact match, including every single letter. Look very closely at these two lines:
#      Your Data: {"os": "Windows 10" ...} (with an s)
#      Your If Statement: if device["os"] == "Window 10" (without the s)
# Because "Window 10" is not the same as "Windows 10," 
# the computer says, "Nope, that's not a match!" and skips over the code inside your if statement.
#  This is why your to_replace list is coming back empty. SO THE FIX WAS :

# 🛠️ The Fix
# Change "Window 10" to "Windows 10" in your if statement:

# Python
# if device["os"] == "Windows 10" and device["ram"] < 16:
# 💡 Why This Happens (and how to avoid it)
# In professional IT scripts, we often use the .lower() method or
#  the in keyword to prevent these tiny "typo" bugs from breaking our audits.

##----------- Try this "Bulletproof" Version in VS Code:----------------------

#--------- Python
######## Using 'in' is safer than '==' because it catches "Windows 10" # THIS IS THE WHOLE / MAIN POINT
#-----------# even if there's a small typo or extra space.
########---if "Windows 10" in device["os"] and device["ram"] < 16: # THE USE OF WHAT WE NEED (Windows 10) IN THEN ANY CONDITION (in device["os"] and device["ram"] < 16) IS BETTER

##------------😈 Step 5.5: The "Tricky" Audit (The Nested Logic Trap)
# Ready for a challenge? This one uses or and not.
# or means if EITHER thing is true, the door opens.
# not flips the answer (True becomes False).

# The Scenario: You are managing a server room. 
# You need to flag any server that is either overheating OR has a status that is NOT "Active".

# In VS Code:
# Create a list called servers:
# {"id": "S1", "temp": 80, "status": "Active"} (80 is fine)
# {"id": "S2", "temp": 110, "status": "Active"} (Too hot!)
# {"id": "S3", "temp": 75, "status": "Maintenance"} (Not Active!)
# {"id": "S4", "temp": 120, "status": "Offline"} (Both bad!)

# The Goal: Create a loop that prints a warning if:
# The temp is greater than 100 * OR The status is not equal to "Active"

# The Challenge:
# If you use or, your code should catch S2, S3, and S4. Only S1 should be ignored.
# Try writing the if statement for this one. Pay close attention to the != (Not equal) and the or.


# servers=[
#  {"id": "S1", "temp": 80, "status": "Active"},
#  {"id": "S2", "temp": 110, "status": "Active"}, 
#  {"id": "S3", "temp": 75, "status": "Maintenance"}, 
#  {"id": "S4", "temp": 120, "status": "Offline"}
# ]

# for s in servers:
#     if s['temp'] > 100 or s['status'] != 'Active':
#         print(f"This server: {s['id']} has either it's temp: {s['temp']} or status: {s['status']}, issue")
#--------------------------------------------------------

##--------Since you are an IT Support Analyst with experience in Tier 1 and Tier 2 support,
#  let's look at a "Boss Level" real-world example: The Automated Onboarding Audit.

# Imagine a new batch of employees just started. Some are in IT and need high-power laptops
# , and some are in Sales and just need a standard setup.
#  You need to find any "Mismatches" where an employee has the wrong equipment.

##----------- ✏️ Boss Level Exercise: The Onboarding Audit----------
# In this scenario, we are looking for Error Cases. A "Mismatch" happens if:

# The user is in "IT" but has less than 16 GB of RAM.
# -- OR --
# The user is in "Sales" but has a "MacBook" (your company policy only allows Windows for Sales).

# In VS Code:
# Create this list of dictionaries:
# Python
# employees = [
#     {"name": "Alice", "dept": "IT", "ram": 32, "device": "MacBook"},   # OK
#     {"name": "Bob", "dept": "IT", "ram": 8, "device": "Windows"},     # ERROR (Low RAM for IT)
#     {"name": "Charlie", "dept": "Sales", "ram": 16, "device": "MacBook"}, # ERROR (Mac for Sales)
#     {"name": "David", "dept": "Sales", "ram": 8, "device": "Windows"} # OK
# ]
# Create an empty list: flagged_users = [].
# The Loop: for person in employees:
# The Complex Logic (Nested Ifs):
# IF person["dept"] == "IT" and person["ram"] < 16:
# Print: f"⚠️ {person['name']} (IT) needs a RAM upgrade!"
# flagged_users.append(person["name"])
# ELIF person["dept"] == "Sales" and person["device"] == "MacBook":
# Print: f"⚠️ {person['name']} (Sales) has unauthorized hardware!"
# flagged_users.append(person["name"])
# The Result: Print the final flagged_users list.

# 💡 Why this is "Real World"
# The elif: This stands for "Else If." 
# It allows you to check a different rule if the first one wasn't met. 
# It keeps your code from checking "Sales" rules for "IT" people.

# Data Integrity: This script would save you hours of manual spreadsheet checking.

# employees = [
#      {"name": "Alice", "dept": "IT", "ram": 32, "device": "MacBook"},   # OK
#      {"name": "Bob", "dept": "IT", "ram": 8, "device": "Windows"},     # ERROR (Low RAM for IT)
#      {"name": "Charlie", "dept": "Sales", "ram": 16, "device": "MacBook"}, # ERROR (Mac for Sales)
#      {"name": "David", "dept": "Sales", "ram": 8, "device": "Windows"} # OK
#  ]

# flagged_users = []

# for e in employees:
#     if e['dept'] == 'IT' and e['ram'] < 16:
#         print(f"⚠️ {e['name']} (IT) needs a RAM upgrade!")
#         flagged_users.append(e['name'])

#     elif e['dept'] == 'Sales' and e['device'] == "MacBook":
#         print(f"⚠️ {e['name']} (Sales) has unauthorized hardware!")
#         flagged_users.append(e['name'])

# print(f"Lists of falgged_users: {flagged_users}")
#--------------------------------------------------------------------------------

##--------- 🔍 The "In" List: How it Works--------------------
# Think of it like a VIP Guest List at a club. 
# Instead of the bouncer asking, "Are you Alice? Or are you Bob? Or are you Charlie?", 
# the bouncer just holds a list and checks if your name is in it.

# 💻 Real-World Example: The "Bad Software" Audit
# Imagine your company has banned certain apps for security reasons (like "Torrent", "Keylogger", or "Unapproved_VPN").

# Without the "In" List (The messy way):

# Python
# if app == "Torrent" or app == "Keylogger" or app == "Unapproved_VPN":
#     print("🚨 Security Alert!")

# With the "In" List (The Master way):

# Python
# banned_apps = ["Torrent", "Keylogger", "Unapproved_VPN", "TikTok", "MineCraft"]
# current_app = "TikTok"

# if current_app in banned_apps:
#     print(f"🚨 Security Alert: {current_app} is not allowed on company hardware!")

##-------------✏️ Exercise 5.6: The "Regional Support" Filter------------------
# You are routing support tickets. Tickets from "London", "Paris", and "Berlin" need to be sent to the EMEA Team.

# In VS Code:
# Create a list: emea_cities = ["London", "Paris", "Berlin"].
# Create a dictionary for a new ticket:
#     ticket = {"id": 505, "city": "Paris"}.
# The Logic:
# IF the ticket["city"] is in emea_cities:
# Print: "Routing to EMEA Support Team..."
# ELSE:
# Print: "Routing to Global Support Team..."

# emea_cities = ["London", "Paris", "Berlin"]
# ticket = {"id": 505, "city": "Paris"}

# if ticket["city"] in emea_cities:
#     print("Routing to EMEA Support Team...")
# else:
#     print("Routing to Global Support Team...")
#------------------------------------------------

##----------------- ✏️ Boss Level Exercise 5.7: The "Security Firewall" Audit--------------------
# The Scenario: You are auditing a network. 
# You have a list of "Dangerous Protocols" that should never be open on a public-facing server.

# Your Rules:
# Dangerous Protocols: ["Telnet", "FTP", "HTTP"] (These are unencrypted).
# The Flag: A server is a "Critical Security Risk" if:
# Its protocol is in the dangerous_protocols list.
# -- AND --
# Its visibility is "Public".

# In VS Code:

# The Data:
# Python
# network_inventory = [
#     {"id": "Srv-01", "protocol": "HTTPS", "visibility": "Public"},
#     {"id": "Srv-02", "protocol": "Telnet", "visibility": "Public"},
#     {"id": "Srv-03", "protocol": "FTP", "visibility": "Private"},
#     {"id": "Srv-04", "protocol": "HTTP", "visibility": "Public"}
# ]

# dangerous_protocols = ["Telnet", "FTP", "HTTP"]
# The Task: Loop through network_inventory.

# The Logic: Use an if statement to find the servers that match both rules (In the dangerous list AND Public).

# The Action: Print a warning for the dangerous servers: 
# f"🚨 SECURITY BREACH: {server['id']} is exposing {server['protocol']} to the Public!"

# network_inventory = [
#      {"id": "Srv-01", "protocol": "HTTPS", "visibility": "Public"},
#      {"id": "Srv-02", "protocol": "Telnet", "visibility": "Public"},
#      {"id": "Srv-03", "protocol": "FTP", "visibility": "Private"},
#      {"id": "Srv-04", "protocol": "HTTP", "visibility": "Public"},
#  ]
# dangerous_protocols = ["Telnet", "FTP", "HTTP"]

# for server in network_inventory:
#     if server['protocol'] in dangerous_protocols and server['visibility'] == 'Public':
#        print(f"🚨 SECURITY BREACH: {server['id']} is exposing {server['protocol']} to the Public!")

##------------------------------ 😈 The "Ultimate" Tricky Mix (Self-Correction)----------------------------
# Sometimes in IT, data is messy. Someone might type "ftp" (lowercase) or "FTP " (with a space).

# Try this "Stress Test" in VS Code:
# Change Srv-03 in your list to: {"id": "Srv-03", "protocol": "ftp", "visibility": "Public"} (Make it lowercase and Public).
# Run your code again.
# Wait... did Srv-03 get flagged?
# If your dangerous_protocols list has "FTP" (uppercase), Python will see "ftp" (lowercase) and think they are different!

# The Trick:
# To fix this, professional IT Analysts use .upper() to force the data to match their list.

# Python
# if server['protocol'].upper() in dangerous_protocols and server['visibility'] == 'Public':
#--------------------------------------------------------------------------------------

##--------- Understood! You’ve mastered the "Logic" and "Data" parts of Python. 
# Now, we are going to learn how to package that logic so you don't have to type it out 100 times.

######## In IT, a "Function" is like a custom command you build yourself. 
# Instead of writing a loop and 5 if statements every time you check a server, you just type check_server(my_data).#######

##-------- 💡 The 3 Parts of a Function-----------
# The Definition (def): This is where you build the "machine."

# The Parameter: The "input" the machine needs to work (like a server's ID).

# The Return: The "output" the machine spits back out to you.


##---------------- 💻 Exercise 6.1: Your First IT Tool----------
# Let’s build a function that checks if a user's account is "Locked" based on their login attempts.

# In VS Code:
# Define the function:
# Python
# def check_account_status(attempts):
#     if attempts >= 3:
#         return "LOCKED"
#     else:
#         return "Active"
# Use the function (Call it):

# Python
# # Test 1: Someone with 1 attempt
# user_1 = check_account_status(1)
# print(f"User 1 is: {user_1}")

# # Test 2: Someone with 5 attempts
# user_2 = check_account_status(5)
# print(f"User 2 is: {user_2}")


##----- 🛠️ Why this is a "Power Move"------
# Imagine you have 1,000 users. Instead of writing that if/else logic 1,000 times,
#  you just "call" check_account_status() for every name in your list. It makes your code clean and reusable.

##-------------------- ✏️ Exercise 6.2: The "RAM Auditor" Function--------------------------
# Now, let's turn your previous "RAM check" into a reusable tool.

# In VS Code:

# Define a function called needs_upgrade.
# It should take one parameter: ram_size.
# Inside:
# IF ram_size is less than 16, return True.
# ELSE, return False.
# Test it: * print(needs_upgrade(8))
# print(needs_upgrade(32))

# ❓ Check-in
# Does it make sense that attempts and ram_size are just "placeholders"? 
# They don't have a value until you actually call the function with a number.

# Can you see how the return keyword is like the "Exit" door of the function,
#  handing the answer back to your main program?

# def needs_upgrade(ram_size):
#     if ram_size < 16:
#         return True  # calling it True because if ram < 16 needs upgrade/ to be worked on
#     else:
#         return False # calling it False because if ram > 16 DON'T need upgrade/ to be worked on = ITS GOOD
# print(needs_upgrade(8))
# print(needs_upgrade(32))
#------------------------------------------------------------

##------------ ✏️ Exercise 6.3: The "Multiple Parameter" Tool--------------
# Most IT tools need more than one piece of info. 
# Let's build a function that takes two inputs: username and is_admin.

# In VS Code:
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
#     if is_admin == True:
#         return (f"ADMIN: {username}")
#     else:
#         return (f"USER: {username}")
    
# print(generate_access_label("Daniel", True))
# print(generate_access_label("Guest_User", False))
#------------------------------------

# You said
# so everything that starts with is_ is considered as boolean and true?

# Gemini said
# That is a fantastic observation! You’ve just spotted one of the most important "unwritten rules" of professional programming.

# Strictly speaking, the computer doesn't care what you name a variable. You could call a Boolean potato = True, and it would work. However, in the IT and AI world, we use "Naming Conventions" to make code readable for other humans (like your teammates or Ms. Bom).

# 🏷️ The "is_" Convention
# When a variable or function starts with is_, has_, or can_, it is a strong signal to other programmers that the value inside is a Boolean (True or False).

# Variable Name	       Likely Data Type    	What it's asking
# is_admin	              Boolean	        Is this person an admin? (Yes/No)
# has_ssd	              Boolean	        Does this laptop have an SSD? (Yes/No)
# can_reboot	          Boolean	        Is the server allowed to reboot? (Yes/No)
# user_name	              String	         What is the name?
# ram_gb	              Integer	        How much RAM is there?

##--------🧠 Is it always True?------
# Not necessarily! The is_ part is just the label on the box.

# If is_admin = True, the box contains "Yes."
# If is_admin = False, the box contains "No."

##---The beauty of this naming style is how it reads in an if statement. It sounds like English:
# if is_active: or if is_locked:

##-------- ✏️ Final Challenge: The "Storage Alert" System---------------------
# Before we wrap up Step 6, let's see you put that "Naming Convention" and "Function Logic" into action with the Storage Alert exercise.

# In VS Code:
# Function: def get_status(percent):
# > 90: Return "CRITICAL 🚨"
# > 75: Return "WARNING ⚠️"
# Else: Return "Healthy ✅"
# Data:
# Python
# servers = [
#     {"id": "Srv-A", "usage": 95},
#     {"id": "Srv-B", "usage": 40},
#     {"id": "Srv-C", "usage": 82}
# ]
# Loop: Run through the list and print the status for each.

# ❓ Check-in
# Can you see how using a name like is_full would be better than just full?

# Does the if/elif/else structure inside a function feel like a "brain" that processes the numbers you feed it?


# def get_status(percent):
#     if percent > 90: 
#         return "CRITICAL 🚨"
#     elif percent > 75: 
#         return "WARNING ⚠️"
#     else:
#         return "Healthy ✅"

# servers = [
#      {"id": "Srv-A", "usage": 95},
#      {"id": "Srv-B", "usage": 40},
#      {"id": "Srv-C", "usage": 82}
#  ]

# for server in servers:
#     #result = get_status(server['usage']) # 1st try to check output
#     #result = (f"{server['id']}: {get_status(server['usage'])}") # 2nd try with server name & server status
#     result = (f"{server['id']}: with {server['usage']}% usage is {get_status(server['usage'])}") # 3rd the best try with structured sentence server name & server status
#     print(result)

# Look at that! You didn't just write the code; you iterated like a professional developer.

# Your "3rd try" is the perfect balance of data and human-readable reporting. You’ve successfully combined:
# Data Structures (List of Dictionaries)
# Custom Logic (The Function)
# Iteration (The Loop)
# String Formatting (The F-string)

# 🔍 Why your 3rd Try is the "Senior Analyst" Choice
# In IT, if you just print CRITICAL 🚨, your boss won't know which server is dying. If you print Srv-A: CRITICAL 🚨, they still don't know why. By including the usage %, you’ve provided the Context along with the Status.

# 🛠️ A Quick Look Under the Hood
# When you run that loop, here is what Python is doing "behind the scenes":
# Step 1: Grabs Srv-A.
# Step 2: Sees usage: 95.
# Step 3: Teleports that 95 into the get_status function.
# Step 4: The function hits the first if, says "Yep, 95 is > 90," and teleports CRITICAL 🚨 back out.
# Step 5: Your F-string catches that result and prints the final line.

##------ 🎓 You have completed the Fundamentals!------------
# You now have the "Core Four" skills needed for both IT Automation and AI Development:
# Variables & Types (Strings, Integers, Booleans)
# Logic & Comparison (If/Elif/Else, and/or/not)
# Containers (Lists & Dictionaries)
# Reusability (Loops & Functions)

# ❓ What's Next?
# We can go in two directions now:
# Option A: Error Handling (try/except) – How to stop your code from "crashing" when it hits a server that is missing data (e.g., a server with no usage key).
# Option B: Libraries & Modules – Learning how to use "pre-built" tools to do things like check your actual computer's RAM or create a file on your desktop.

# Smart move. In IT Support, a script that "crashes" is worse than no script at all. 
# If you're running a backup or a security audit and the code hits a single error 
# (like a missing file or a server that's offline), the whole program stops.

##--------- Error Handling is the "Safety Net" that keeps your code running even when things go wrong.----------------

##--------🛡️ Step 7: Error Handling (The Try/Except Block)
# In Python, we use a try and except block.
# try: "Try to run this code."
# except: "If a specific error happens, don't crash! Do this instead."

#------------- 💻 Exercise 7.1: The "Zero Division" Trap------------------------
# Imagine you are calculating a server's uptime. If the "Total Days" is 0 (maybe a brand new server), the computer will panic because you cannot divide by zero in math.

# Python
# def get_uptime_ratio(hours, days):
#     try:
#         ratio = hours / days
#         return f"Uptime Ratio: {ratio}"
#     except ZeroDivisionError:
#         return "⚠️ Error: Cannot calculate for 0 days."

# # Test 1: Normal data
# print(get_uptime_ratio(24, 1))

# # Test 2: "Broken" data
# print(get_uptime_ratio(10, 0))

##--------------- ✏️ Exercise 7.2: The "Missing Data" Audit----------------------
# This happens all the time in Data Analysis. You have a list of users, 
# but one user is missing their "email" key. Without error handling, your loop will crash with a KeyError.

# The Data:
# Python
# users = [
#     {"name": "Daniel", "email": "daniel@test.com"},
#     {"name": "Guest"} # Missing the 'email' key!
# ]
# # The Loop with a Safety Net:

# for u in users:
#     try:
#         print(f"Sending email to: {u['email']}")

#     except KeyError:
#         print(f"⚠️ Skipping {u['name']}: No email address found.")

##-------🔍 Why this matters for your Goal----------
# When you start building Websites or AI Agents, the "outside world" will send you messy data. Like:

# A user might type a letter where a number should be.
# The AI might return an empty response.
# A database might be temporarily offline.

# try/except ensures your website stays online and your AI agent doesn't "die" just because of one bad input.

# ❓ Check-in
# Does it make sense that except only runs if something breaks inside the try block?
# Can you see how this makes your IT scripts "Unstoppable"?     

##------------- Since you're aiming for AI Agents, this "Nested" error logic is vital. 
# AI agents often make "API calls" (talking to another computer). Two things usually go wrong:
     # Connection Error: The internet is down (The "Phone" is broken).
     # Data Error: The AI sends back "Garbage" data (The "Message" is gibberish).

# If you don't handle both, your agent will "hang" or crash.

##-------------- 🕸️ Step 7.3: The Nested "Double Safety Net"--------------
# In Python, you can "stack" except blocks to handle different problems differently. 
# Think of it like a Sorting Machine for errors.

# The Scenario: You are writing a script for an AI Agent that calculates a "Risk Score" based on a user's ID.

# Python
# # S1 is perfect.
# # S2 has a "Bad ID" (not a number).
# # S3 is missing the ID key entirely!
# server_data = [
#     {"id": "101"}, 
#     {"id": "ABC"}, 
#     {"status": "offline"} 
# ]
# The Logic (The Nested Trap):

# Python
# for server in server_data:
#     try:
#         # Step 1: Try to get the ID (Might cause KeyError ## meaning if step-1 fails means it failed at "KeyError which is a Ticket that Python already knows", then next step is it jumps to the first except called KeyError (1 step failure = jumps to 1 except))
#         raw_id = server["id"]
        
#         # Step 2: Try to turn it into a number (Might cause ValueError ## meaning if Step-2 fails means it failed at "ValueError which is a Ticket that Python already knows", then next Step is it jumps to the second except called ValueError (2 step failure = jumps to 2 except))
#         numeric_id = int(raw_id)
        
#         print(f"✅ Success: Server ID is {numeric_id}")

#     except KeyError:
#         print("❌ Error: ID field is missing from this server!")

#     except ValueError:
#         print(f"⚠️ Warning: ID '{raw_id}' contains non-numeric characters!")

##--- so if step 1 is error then the process jumps to the 1st except , 
# and if failure happens in step-2 it jumps to to the 2nd except then right?

# Gemini said
# Exactly! You’ve got the "Path of Least Resistance" logic down perfectly.

# Python is always looking for the nearest exit the moment something goes wrong. 
# It won't keep trying to walk through a "closed door" (an error); 
# it just jumps to the safety net you built for that specific door.

# 🏢 The "Level 1 vs. Level 2" Breakdown
# Think of your try block as a two-story building.

# Step 1 (The Ground Floor): Accessing the Dictionary Key.
# If this fails, you can't even get to the stairs. You jump out of the building to the KeyError net.
# Step 2 (The Second Floor): Converting the Data to an Integer.
# If you make it to the stairs but the data is "rotten" (letters instead of numbers), 
# you jump out of the second floor into the ValueError net.

# 🧪 One Final "Trick" Question
# If you had a dictionary like this: server = {"id": "105"}.

# Step 1: raw_id = server["id"] — SUCCESS.
# Step 2: numeric_id = int(raw_id) — SUCCESS.
# Step 3: print("Server is Ready!") — SUCCESS.

# Does any except block run?
# No! If the try block finishes with zero "Tickets" (errors), 
# Python skips all the except blocks and just continues with the rest of your script. 
# The safety nets are only there if someone falls!

# 📦 Option B: Libraries (The "Power-Up" for AI)
# Now that you are a master of Error Handling, let’s see how we use Libraries to build your AI Agents and Websites.

##---- In Python, we don't write "The Brain" from scratch. We Import it.----

# Example: Talking to an AI (The "OpenAI" or "Gemini" Library)
# When you build an AI Agent, you will use a library. 
# You don't have to write the code that connects to the internet; the library does it for you.

# How it looks (Conceptual):
# Python
# import ai_library # Option B: Using a Library

# def ask_ai(question):
#     try:
#         # The library handles the complex "Talk to AI" part
#         response = ai_library.generate(question)
#         return response
#     except ai_library.ConnectionError:
#         # Option A: You handle the "No Internet" error
#         return "Check your Wi-Fi, the AI is offline!"
# ❓ The Decision
# Do you see how Option A (Errors) and Option B (Libraries) work together?

# The Library does the heavy lifting (Web, Data, AI).
# The Error Handling makes sure that if the Library fails, your whole project doesn't crash.

# You've got the rhythm now! Let's do a Real-World IT Support exercise.
# When you are an Analyst, you often have to calculate the "Load" on a server. This involves two things that can break:

# The Server is Missing: (The Key isn't in your list).
# The Data is "Broken": (The CPU usage is recorded as a string like "HIGH" instead of a number like 90).

##------- ✏️ Exercise 7.5: The "Server Load" Calculator
# The Task: You have a function that calculates how much "Headroom" a server has left (100 minus the usage).

# The Data:

# Python
# # Srv-01 is perfect.
# # Srv-02 has a 'KeyError' (missing the 'usage' key).
# # Srv-03 has a 'ValueError' (usage is a string 'MAX' instead of a number).
# inventory = [
#     {"id": "Srv-01", "usage": 80},
#     {"id": "Srv-02", "status": "Online"},
#     {"id": "Srv-03", "id_label": "Srv-03", "usage": "MAX"}
# ]
# The Logic:
# Create a for loop to check each server.
# Inside the try block:
# Get the usage.
# Convert it to an integer.
# Calculate headroom = 100 - usage.
# Print the result.
# Add an except KeyError:
# Print "❌ Error: Usage data missing for this server."
# Add an except ValueError:
# Print "⚠️ Error: Usage must be a number, not text!"


#---Correct Way
# inventory = [
#     {"id": "Srv-01", "usage": 80},
#     {"id": "Srv-02", "status": "Online"},
#     {"id": "Srv-03", "id_label": "Srv-03", "usage": "MAX"}
# ]

# def calculate_headroom(server_dict):
#     try:
#         # Step 1: Try to get the usage (Might cause KeyError)
#         usage = server_dict["usage"] # checks if the server have a key called "usage" is Yes, it access it's value. if No, is jumps to z 1st except
        
#         # Step 2: Try to do math (Might cause ValueError if usage is "MAX")
#         result = 100 - int(usage)
#         return f"Headroom is {result}%"

#     except KeyError:
#         return "❌ Error: 'usage' key missing!"
#     except ValueError:
#         return "⚠️ Error: Usage must be a number, not text!"

# for server in inventory:
#     # We pass the WHOLE dictionary so the function can check for the key
#     status = calculate_headroom(server)
    
#     # Use quotes correctly in your f-string
#     print(f"Server {server.get('id', 'Unknown')}: {status}")
# ❓ Why did I change server["usage"] to just server?
# If I pass server["usage"] into the function, and the key is missing (like in Srv-02), the program crashes outside the function. By passing the whole server dictionary, the try block inside the function can catch the KeyError safely!

# ❓ Check-in
# Do you see how int(usage) does the "Checking" for you? If it can't do it, it just triggers the ValueError ticket.

# Does the difference between the Key (the drawer) and the Value (what's inside) feel clearer now that you've seen them fail in the same script?

# Try running this corrected version in VS Code and tell me if the output for Srv-02 and Srv-03 matches what you expected!