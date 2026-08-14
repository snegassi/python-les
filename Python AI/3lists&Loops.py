

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

# stock_prices = [150, 200, 300, 50] # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
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

# item_counts = [10, 5, 2] # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON

# # To Update/Change item
# item_counts[0] = 15
# print(item_counts)

# # To Add item
# item_counts.append(8)
# print(item_counts)

# # Independent Check
# if item_counts[2] < 5:
#     print("🚨 Warning: Item 3 is low stock!")

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

## The List is the belt. (# The list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON)

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
# logs = ["Success", "Failed", "Success", "Success", "Failed"] # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
# # For loop is Worker
# for status in logs:   # "status" indicated Single item of the list at a time
#     if status == "Failed":
#         print("⚠️ Security Warning: Failed Login Detected!") # Since the Print is Inside the For-loop. It prints one at a time for each Statues failed it finds, since its in a loop
#     else:
#         print("Login OK.")  #Since the Print is Inside the For-loop. It prints one at a time for each Statues Success it finds, since its in a loop

# Result = Login OK.
#          ⚠️ Security Warning: Failed Login Detected!
#          Login OK.
#          Login OK.
#          ⚠️ Security Warning: Failed Login Detected!

# There it is! You just automated your first security audit.
# Instead of writing 5 separate if statements, you wrote one piece of logic and told Python to "apply this to everything in the list." 
# If that list had 1,000,000 logs, Python would have finished the whole thing in a split second.
#------------------------------------

# 🛠️ Step 4.2: The "Accumulator" (The Running Total)
## In Data Analysis, we don't just want to print things; we want to count things. 
## How many people failed to log in? What is the total of all sales?

## To do this, we create a variable outside the loop (starting at 0) and update it inside the loop.
# Python
# # --- OUR DATA ---
# sales = [10, 50, 100, 20] # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
# total_money = 0  # We start at zero

# # --- THE LOOP ---
# for s in sales:
#     # Add the current sale to our running total
#     total_money = total_money + s
#     print(f"Added {s}. Current total is: {total_money}") #Since THE Print is Inside the for-loop. It prints one at a time for each s it finds

# # --- Outside the loop-THE RESULT ---
# print(f"--- FINAL SALES TOTAL: ${total_money} ---")### Since the print is Outside the for- loop/ If. It prints the Final Result of total_money in the End Once.


# Result = Added 10. Current total is: 10
#          Added 50. Current total is: 60
#          Added 100. Current total is: 160
#          Added 20. Current total is: 180
#          --- FINAL SALES TOTAL: $180 ---
#-------------------------

## ✏️ Exercise 4.3: The "Error Counter"
# Let's combine your "Security Scanner" with a "Counter." This is exactly how IT dashboards track system health.

# Create a list: status_codes = [200, 404, 200, 500, 200].
# (Note: 200 means "OK", anything else is an error!)
# Create a variable error_count = 0.
# The Loop: for code in status_codes:
# Inside the Loop (Tabbed):
#    IF code != 200: (The != means "Not Equal To")
#      Print "Found an error: [code]".
#      Add 1 to your counter: error_count = error_count + 1.
# Outside the Loop (No Tab):
#   Print "Total Errors Found: [error_count]".
## When you run this, does it correctly count the 2 errors (404 and 500)? 
## Why this matters: You are now moving from just "looking" at data to "calculating" results from data. 
# This is the heart of building AI Agents—they take in a list of information and give you a summary! How did the counting go?

# status_codes = [200, 404, 200, 500, 200] # 200 means "OK", anything else is error! AND # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
# error_count = 0 # THe counting Variable Staring at Zero

# for code in status_codes:
#     if code != 200: # != means "Not Equal to"
#         print(f"Found an error: {code}") ### Since THE Print is Inside the For-loop. It prints one at a time for each error it finds, since its in a loop
#         error_count = error_count + 1 # Adding One error at a time

# # Outside the loop- PRINTING FOR TOTAL ERRORS
# print(f"Total Errors Found: {error_count}") ### Since the print is Outside the for- loop/ If. It prints the Final Result of errors in the End Once.

# Result = Found an error: 404
#          Found an error: 500
#          Total Errors Found: 2

## 1. Was it the right code?
# Yes. Your code is functionally perfect.
## Your indentation is exactly where it needs to be (the if is inside the for, and the print for the total is outside).
## Your logic (code != 200) correctly targets only the errors.
## Your counter (error_count + 1) accurately tracks the occurrences.

## 2. Was it right to use an f-string?
## Actually, you chose the best possible method. In modern Python (the kind used in AI and professional IT), 
# f-strings are the "Gold Standard."
## You mentioned you used them because you didn't remember another method, but even if you knew the others, 
# f-strings are what a "Senior Developer" would use. ---

## 💡 Just for your knowledge (The "Older" Methods)
# Since you are an IT Analyst, you might see older code in legacy systems that looks like this. 
# It’s good to recognize them, even if you don't use them:

## The Comma Method: print("Found an error:", code)
# Why it's okay: It’s simple.
# Why it's worse: Python forces a space between them, and you have less control over the sentence.

## The Plus Method: print("Found an error: " + str(code))
# Why it's worse: You have to manually turn the number into a string using str(), or Python will crash. It's very tedious.

## F-strings (like yours) are cleaner because you just "drop" the variable into the curly braces {} and Python handles the rest.

## 🛠️ A Small "Pro Tip" for your Counter
# In your code, you wrote:
## error_count = error_count + 1 (Counting by 1)

## This is 100% correct. However, in the IT world, you will often see a "shortcut" for this that does the exact same thing:
# error_count += 1
## The += simply means "add to the current value." It saves you a bit of typing.
#----------------------------

# Excellent. Since you've mastered the "Data Auditor" (counting) and "F-strings", let’s put them to work.
## We will do two exercises. The first is a "warm-up" to lock in the += shortcut, and the second is a "Real-World IT" scenario.

## ✏️ Exercise 4.5: The "Server Status" Monitor
# In this one, we are checking a list of server response times (in milliseconds). 
# Any time over 500ms is considered "Slow."

# Create a list: response_times = [100, 550, 200, 800, 450].
# Create a counter: slow_count = 0.
# The Loop: for time in response_times:
# Inside the Loop:
# IF time > 500:
#    Print an F-string: "⚠️ Warning: {time}ms is too slow!".
#    Add 1 to your counter using the shortcut: slow_count += 1.
# Outside the Loop:
#    Print an F-string showing the total number of slow servers.

# response_times = [100, 550, 200, 800, 450] # time over 500 is "Slow" and # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
# slow_count = 0 # Empty variable,if we want to add 1(number) to it later from the LOOP Using "slow_count += 1(counting)"

# for time in response_times:
#     if time > 500:
#         print (f"⚠️ Warning: {time}ms is too slow!") #Since THE Print is Inside the For-loop. It prints one at a time for each Time it finds.
#         slow_count += 1

# print(f"The total count of slow response = {slow_count}")# Since the print is Outside the for- loop/ If. It prints the Final Result of slow_count in the End Once.

# Result = ⚠️ Warning: 550ms is too slow!
#          ⚠️ Warning: 800ms is too slow!
#          The total count of slow response = 2

## ✏️ Exercise 4.6: The "Email Filter" (Independent + Loop)
# As an IT Support Analyst, you might need to separate "Internal" emails from "External" ones for security.

# Create a list: emails = ["boss@company.com", "hacker@gmail.com", "hr@company.com", "client@yahoo.com"].
# Create two empty lists: internal = [] and external = [].
## The Loop: for address in emails: ????why use "in" in for-loop ??
# Inside the Loop:
#    IF "@company.com" in address: 
#    Append the address to the internal list.
#    ELSE:
#    Append the address to the external list.
# Outside the Loop:
#    Print both lists using F-strings to see your "Sorted" data.
## ❓ Quick Check-in
# Take your time with these in VS Code.
## One thing to watch for: Make sure your internal = [] and external = [] are outside (above) the loop. 
## If you put them inside, Python will "reset" them to empty every time the loop spins!

# emails = ["boss@company.com", "hacker@gmail.com", "hr@company.com", "client@yahoo.com"] # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
# internal = [] # Empty list, if we want to Add Specific items to it later from the LOOP Using ".append()"
# external = [] # Empty list, if we want to Add Specific items to it later from the LOOP Using ".append()"

### do a loop to go over the list one by one 
# for address in emails: # for one by one i called it address but the list varibale = emails
#     if "@company.com" in address: ### ????
#         internal.append(address)
#     else:
#         external.append(address)

# print(f"The internal list = {internal} and external list = {external}")

# Result = The internal list = ['boss@company.com', 'hr@company.com'] and external list = ['hacker@gmail.com', 'client@yahoo.com']
#****************************
### The difference between Partial Match and Exact Match.
## 🔍 2) The "In" vs. "==" Distinction
## You are 100% correct.
## "== (Exact Match)": This is like a fingerprint scanner. If you wrote if address == "@company.com", it would only be true if the person's email address was literally just those 12 characters. 
# Since no one has the email address "@company.com", your list would stay empty!
## "in (Partial Match)": This is like a metal detector. It doesn't care what else is in your pocket; it’s just looking to see if any part of the "address" contains that specific string of text.

## Try this in your VS Code terminal:
## print(f"{internal=}")
## Output: internal=['boss@company.com', 'hr@company.com']
#------------------------------------------------

## 🛠️ Exercise 4.7: The "Final Boss" of Loops & Logic
#### Since you understood the += 1 (counting) vs. += value (summing) distinction, 
## let's do one "Master Exercise" that combines everything we've learned so far:
## A List of data.
## A For Loop to automate it.
## A Counter (to see how many).
## A Sum (to see how much).
## An Independent If check.
#-------------------------------------------------
# The Scenario: You are auditing a list of cloud storage folders. Some are "Oversized" (over 100GB).

# Create a list: folder_sizes = [20, 150, 80, 300, 45].
# Create two variables: oversized_count = 0 and total_oversized_gb = 0.
# The Loop: for size in folder_sizes:
# Inside the Loop:
#   IF size > 100:
#     Print: f"⚠️ Found huge folder: {size}GB"
#     Count it: Add 1 to oversized_count.
#     Sum it: Add the size to total_oversized_gb.
# Outside the Loop:
#   Print the final count of big folders.
#   Print the total GB occupied by those big folders.
# When you finish this, tell me: * What was the final oversized_count?
# What was the final total_oversized_gb?
# I'll be right here to check your logic once you've run it!

# folder_sizes = [20, 150, 80, 300, 45] # This list is the "RAW DATA" that's PROVIDED and NEED to be WORKED-ON
# oversized_count = 0  # Variable for Over 100gb
# total_oversized_gb = 0

# for size in folder_sizes:
#     if size > 100:
#         print(f"⚠️ Found huge folder: {size}GB") ## Since THE Print is Inside the For-loop. It prints one at a time for each Size it finds.
#         oversized_count += 1 # (counting 1 at a time to know how many folders are oversized)
#         total_oversized_gb += size # (adding the total gb of over BY SIZE one at a time)

# print(f"{oversized_count=}") ## Since the print is Outside the for- loop/ If. It prints the Final Result of oversized_count in the End Once.
# print(f"{total_oversized_gb=}GB")## Since the print is Outside the for- loop/ If. It prints the Final Result of total_oversized_gb in the End Once.

# Results =  ⚠️ Found huge folder: 150GB
#            ⚠️ Found huge folder: 300GB
#            oversized_count=2
#            total_oversized_gb=450GB

## You nailed it. Your code is clean, professional, and mathematically sound. 
## By using both += 1 and += size, you successfully performed two different types of data analysis at the same time: 
# Frequency (How often?) and Magnitude (How much?).

## 💡 Why your {variable = } trick is great
# I love that you used the = inside the f-string. In a professional IT environment, 
# when you are debugging a script, seeing oversized_count = 2 is much more helpful than just seeing a random 2 floating in the terminal. 
# It gives your data context.
#----------------------------------------------
### 🚦 The "Master of Logic & Loops" Checkpoint
##You have officially mastered the "Big Three" of Python automation:

## Lists: Storing groups of data.
## For Loops: Walking through every item in a list.
## If Statements inside Loops: Asking questions about each item as you walk.

## 🔍 The "Reset" Trap (A Quick Conceptual Check)
# You correctly put oversized_count = 0 above the loop.

## "Outside the Loop": It's like a bucket sitting on the floor. 
# The loop walks by and drops a coin in it every time it finds a big folder.

## "Inside the Loop": If you put oversized_count = 0 inside the tabbed section,
#  it would be like emptying the bucket every time you looked at a new folder. 
# You would only ever have the "last" folder's result.
#-----------------------------------------------

