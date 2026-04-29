
# 🚦 Step 2: Making Decisions (If/Else Statements)
# In web development and AI, the program needs to make choices.

# Web Dev: If the user's password is correct, log them in.
# AI: If the sensor sees a person, stop the car.

# We do this using if and else. This introduces a very important Python rule: Indentation (The Tab key).

##----📐 The Syntax of a Decision
# In Python, we use a colon : to start a decision and a Tab (or 4 spaces) to show what code belongs "inside" that decision.

# Try typing this into your VS Code (you can clear your old code or start a new file called decisions.py):

# Python
# # --- THE DECISION MAKER ---
# budget = 50.0

# if total_spent > budget:
#     print("⚠️ Warning: You are spending too much on coffee!")
# else:
#     print("✅ Great job staying under budget!")

# # This line is NOT indented, so it runs no matter what:
# print("Budget check complete.")

##-----💡 Pro Tip: Comparison Operators
# To make these decisions, we use these symbols:

# > (Greater than)
# < (Less than)
# == (Equal to — Note: we use two equals signs to compare!)
# != (Not equal to)

##----✏️ Exercise 2.1 (The Decision Challenge)
# Let's test this "logic" muscle. In your VS Code:
# Create a variable my_age and set it to your age.
# Write an if statement to check if my_age is greater than or equal to 18 (use >=).
# If it is, print("You are an adult.").
# Write an else statement that prints "You are a minor.".
# Bonus: Try changing your age variable to 15 and run it again to see if the message changes!
# Did the message in the terminal change when you changed the age?

# my_age = 15

# if my_age >= 18:
#     print("You are an adult.")
# else:
#     print("You are an Minor.")

# Spot on! You just successfully built your first piece of Logic. 🚦
# By changing the variable and seeing the output change, you've demonstrated the core of how apps work:
# Data goes in, logic processes it, and a specific result comes out.

# In Web Development, this is how you'd check if a user is logged in. 
# In AI, this is how a model decides if an image is a "Cat" or a "Dog" based on a probability score.
#-------------------------------------------------------------

# 🚦 Step 2.5: The "In-Between" (Elif)
# What if there are more than two options? For example, 
# if you're building a website that gives different access levels based on age:
# Under 13: Child account
# 13 to 17: Teen account
# 18 and up: Adult account

# We use elif (short for Else If). It lets us check multiple conditions in a row.
# Copy this into VS Code and try changing the age to see all three messages:

# Python
# age = 15
# if age >= 18:
#     print("Full Adult Access")
# elif age >= 13:
#     print("Limited Teen Access")
# else:
#     print("Child Access Only")

##---- ✏️ Exercise 2.2: The "Price Grader" (Advanced Logic)
# Let's combine everything you've learned so far: Variables, Math, and If/Elif/Else.
# In your VS Code, write a script that:

# Creates a variable item_price = 100.
# Creates a variable discount = 20.
# Creates a variable final_price that subtracts the discount from the price.
# The Logic Part:
# If final_price is greater than 100, print: "That is expensive!"
# If final_price is between 50 and 100 (use elif final_price >= 50:), print: "That is a fair price."
# Otherwise (else), print: "What a bargain!"
# Try running it with item_price = 100 and discount = 20. What does your terminal say?

# item_price = 100
# discount = 20
# final_price = item_price - discount

# if final_price > 100:
#     print("That is expensive!")
# elif final_price >=50 and final_price<=100:
#     print("That is a fair price.")
# else:
#     print("What a bargain!") 

## Result = That is a fair price.
#----------------------------------------------------

# okay but you did not teach me how to compare 2 logics together to produce an output like the elif case ? 
# did you skip something ?????
# You are absolutely right to catch that! I jumped into the elif example without explaining 
# the "logic connectors" that allow us to check multiple conditions at once. That is a crucial step for data analysis and AI.
#------------------------------------------

##------In Python, we use Logical Operators to combine conditions:--------
## "and": BOTH conditions must be True.
## "or": At least ONE condition must be True.
## "not": Flips the result (True becomes False).
#---------------------------------------------

##------🚦 Combining Logic in VS Code
# Let's look at how a professional would write a "price grader" using these operators. 
# Copy this into a new file called logic_test.py:

# price = 80
# on_sale = True

# # Using 'and' to check two things at once
# if price < 100 and on_sale == True:
#     print("This is a great deal!")

# # Using 'or' to check if either is true
# if price > 500 or price < 10:
#     print("This price is extreme (either very high or very low).")

##-----------✏️ Exercise 2.3: The "Security Gate" Challenge
# Let's use and and or to practice. This is exactly how website login systems work.
# In VS Code, write a script that:
# Creates a variable username = "admin".
# Creates a variable password = "secret123".
# The Logic: Use an if statement with and to check if the username is "admin" AND the password is "secret123".
# If both are correct, print: "Access Granted".
# Use else to print: "Access Denied".

# Bonus Question: If you change the password to "wrong123", why does the else block run? 
# (Think about how the and operator works!)

# How does your code look with the and operator included?

# username= "admin"
# password = "wrong123" # 0r change the password to "wrong123" to see another effect

# if username == "admin" and password == "secret123": # Since using "and" logic, both conditions have to be true for the if conditon as a whole to work if not, it fails & goes to the next condition
#     print("Access Granted")

# else:
#     print("Access Denied")

## Result = Access Denied
# Spot on! You nailed the logic. You even added a comment explaining exactly how and works—that’s a sign you’re starting to "know it by heart."
# To answer your bonus question: The else block runs because the and operator is a perfectionist. 
# If even one side is False, the whole if statement fails. Since "wrong123" == "secret123" is False, the gate stays locked. 🔒
#-----------------------------------

##------🔄 Step 3: Efficiency (Loops)
# Imagine you are doing Data Analysis on 10,000 rows of sales data. 
# You wouldn't want to write 10,000 if statements! Instead, we use Loops to tell Python: "Do this task for every item in this list."

##There are two main types of loops. Let's start with the most common one: the for loop.

##---- 📐 The "Range" Loop
## In VS Code, try this. It tells Python to count from 0 up to (but not including) 5.
## The 'i' stands for 'item' or 'index' (it's just a variable name)
# for i in range(5):
#     print(f"This is loop number: {i}")

# ## Result = This is loop number: 0
#             This is loop number: 1
#             This is loop number: 2
#             This is loop number: 3
#             This is loop number: 4


##---- 📐 The "List" Loop (Crucial for Web Dev/AI)
# Usually, we loop through a collection of data.

# Python
# fruits = ["Apple", "Banana", "Cherry"]

# for fruit in fruits:
#     print(f"I want to eat a {fruit}!")

## Result = I want to eat a Apple!
#           I want to eat a Banana!
#           I want to eat a Cherry!

##------ ✏️ Exercise 3.1: The "Automated Emailer"------
# Imagine you are building a website and you want to send a "Welcome" message to 3 new users.
# In VS Code:
# Create a list called new_users = ["Alice", "Bob", "Charlie"].
# Use a for loop to go through each user in that list.
# Inside the loop, use an F-String to print: "Sending welcome email to: [Name]".

# When you run this, does it print all three names automatically?
# (Also, let me know if you want me to explain the [] brackets for lists more deeply before we move on!)

# new_users = ["Alice", "Bob", "Charlie"]
# for Name in new_users:
#     print(f" Sending welcome email to: {Name}")

## Result =  Sending welcome email to: Alice
#            Sending welcome email to: Bob
#            Sending welcome email to: Charlie
#----------------------------------------------

## You're asking about Independent If Statements.

# This is a very important distinction. In a "Nested If" or "If/Elif," Python stops as soon as it finds one true answer. 
# But sometimes, you need Python to check every single condition because more than one thing could be true at the same time.

##------🚦 Independent Ifs vs. If/Elif
## if / elif / else or Nested If : This is like a multiple-choice question. Only one answer can be chosen. 
# Once Python finds a "True" one, it skips the rest.

## Multiple if statements: This is like a checklist. Python checks every single one, 
# regardless of whether the one before it was true or false.  

# Let's strip it back to exactly what we have learned: Numbers, Booleans (True/False), and Basic Math.

##---------- 🛑 The "Checklist" (Independent If Statements)
## In an If/Elif (what we did before) or Nested If, Python is looking for one answer. 
# As soon as it finds a "True" one, it stops and ignores everything else.

## In Independent Ifs, Python treats every if like a brand new question. 
# It doesn't care if the one before it was true or false. It checks every single one.

##-----------💻 Exercise 2.6: The "Fitness Tracker"
# Let's use only the math and variables we know. Imagine you have a fitness app.

# In your VS Code, type this:
# # --- OUR DATA ---
# steps_taken = 12000
# calories_burned = 600

# # --- CHECK 1 (Independent) ---
# if steps_taken > 10000:
#     print("🏆 Goal Reached: 10,000 steps!")

# # --- CHECK 2 (Independent) ---
# if calories_burned > 500:
#     print("🔥 Goal Reached: High Calorie Burn!")

## Notice: * There is no elif.
## There is no "else".
## Because 12000 is more than 10000 AND 600 is more than 500, Python will print BOTH messages.

## If we had used "elif", Python would have printed the first one and then stopped, 
# even though you burned a lot of calories!

##------✏️ Your Turn (Step-by-Step)
# In your VS Code, let's build a "Game Score Checker" using only what we've covered:
# Create a variable score = 150.
# Create a variable lives_left = 3.
# Write the first if: Check if score is greater than 100. If it is, print "Level 1 Complete".
# Write a second if (not an elif): Check if lives_left is greater than 0. If it is, print "Still in the game".
# When you run this, do you see both messages in the terminal? (This proves Python checked both "boxes" on your checklist!)
# Once you are 100% comfortable with this "Checklist" style, I will explain the "Staircase" (Nested Ifs) using only these same simple variables.

# score = 150
# lives_left = 3

# if score > 100:
#     print("Level 1 Complete")

# if lives_left > 0:
#     print("Still in the game")

## Result = Level 1 Complete
#           Still in the game

## Perfect. You've got it! Because those are "two separate if statements", Python treated them as a checklist. 
# It checked the score, saw it was true, and printed the message. 
# Then, it moved to the next if, saw it was also true, and printed that message too.

## If you had used "elif", Python would have seen the score was over 100, printed the first message, 
# and stopped right there, never even checking your lives!
#--------------------------------------

###-------🪜 Step 2.7: The "Staircase" (Nested If Statements)
## Now, let's learn the Nested If. This is when one "Question" only matters if the "First Question" was true.

# Think of it like a security gate:
# Question 1: Do you have a key? 🔑
# Question 2 (Only if you have a key): Is the key the right color? 🎨

# 💻 See it in VS Code
# Let's use the variables you already know. Copy this into a new file called nested.py:

# Python
# # --- OUR DATA ---
# score = 150
# has_bonus_item = True

# # --- THE STAIRCASE (NESTED IF) ---
# if score > 100:
#     print("Level 1 Complete!")
    
#     # This next part ONLY runs if the score was > 100
#     if has_bonus_item == True:
#         print("Congrats! You also found the Hidden Star! ⭐")

# print("Game check finished.")
# Why do we do this? If your score was only 50, Python would skip the entire block. 
# It wouldn't even check if you had a bonus item, because you didn't finish the level first!

#--------✏️ Exercise 2.7: The "ATM" Challenge
# Let's practice the "Staircase" logic. In your VS Code, write a script that:
# Create a variable account_balance = 100.
# Create a variable withdrawal_amount = 40.
# The First If: Check if account_balance > 0.
# If it is, print "Account is active.".
# Inside that If (The Staircase): Check if withdrawal_amount <= account_balance.
# If it is, print "Withdrawal successful!".
# The Else (Optional): At the very bottom (not indented), print "Thank you for using our bank.".

# When you run this, do you see both messages? What happens if you change the account_balance to 0? 
### (Take your time with the indentation—it's the most important part of "knowing it by heart"!)

# account_balance = 100
# withdrawal_amount = 40

# if account_balance > 0:
#     print('Account Active')
#     # the Starecase
#     if  withdrawal_amount <= 100:
#         print("Wihdrawal successful!")

# else:
#     print("Thank you for using our bank")

# Result = Account Active
#          Wihdrawal successful!
#--------------------------------
### ??? wait , what if we have one if/elif/else then another if or even if/elif/else separate below it? 
# is there a problem if programming like that ? isn't it a check list ?

# That is a brilliant question. You are visualizing the "architecture" of code perfectly.
# The answer is: No, there is no problem at all! In fact, that is exactly how complex systems 
# (like a website's checkout page or an AI's decision-making) are built.

## When you put one if/elif/else block and then start a new if block below it, 
# you are creating "multiple independent checklists".

# 💡 Why would we do this?
# We do this when we have different categories of questions that don't depend on each other.
# Think of a Movie Theater App:
# Category 1: What is the ticket price based on age? (if/elif/else)
# Category 2: Does the user want popcorn? (if/else)
# One doesn't stop the other from happening.

# 💻 See it in VS Code (Step-by-Step)
# Let's use the variables we already know to see this "Double Checklist" in action. 
# Copy this into a new file called categories.py:

# Python
# # --- OUR DATA ---
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

# How Python reads this:
# It looks at Checklist 1. It finds the else (Adult) is true, prints it, and ignores the other age options.
# It then moves to Checklist 2. It sees a brand new if. It doesn't care what happened in the age check! 
# It checks the coupon, sees it's True, and prints the discount.

# ✏️ Exercise 2.8: The "Online Store" Challenge (Checklist)
# Let's try coding a "Double Checklist" yourself to lock this in.

# In VS Code:
# Create a variable order_total = 150.
# Create a variable shipping_type = "Express".
# Block 1 (Tax Check):
# If order_total > 100, print "High Value Tax Applied".
# Else, print "Standard Tax Applied".
# Block 2 (Shipping Check - Separate):
# If shipping_type == "Express", print "Shipping in 1-2 days".
# Else, print "Shipping in 5-7 days".

# When you run this, do you see one message from the Tax check AND one message from the Shipping check? 
# This proves you can stack as many "logic blocks" as you want! 
# Would you like to try one more complex version of this, or are you ready to move to Loops?

# order_total = 150
# shipping_type = "Express"
# #block 1
# if order_total > 100:
#     print ("High Value Tax Applied")
# else:
#     print("Standard Tax Applied")
# #block 2
# if shipping_type == "Express":
#     print("Shipping in 1-2 days")
# else:
#     print("Shipping in 5-7 days")

#Result = High Value Tax Applied
#         Shipping in 1-2 days
#----------------------------------

###???? can these independent checklists be dependent on each other? 
# like lets say the output of the first is needed used by the second one?

# You have just hit on the exact way that data analysis and AI pipelines are built!
# The answer is yes. In fact, this is how we "pass the baton" from one piece of logic to another. 
# To do this, we usually use a Variable to store the result of the first checklist, 
# and then the second checklist looks at that variable.

###------- 💻 How it Works in VS Code (The "Baton Pass") or (Connected ifs, where the result of one is used in the next if)
# Imagine you are building a website's checkout.
# Checklist 1: Calculates the price.
# Checklist 2: Uses that price to decide if the user gets free_shipping.
# Copy this into a new file called baton_pass.py:

# # --- INITIAL DATA ---
# item_type = "Electronics"
# order_total = 0 # We start at 0

# --- CHECKLIST 1: Set the Price ---
# if item_type == "Electronics":
#     order_total = 150
# else:
#     order_total = 50

# # --- CHECKLIST 2: Check for Free Shipping (Dependent on Checklist 1) ---
# if order_total > 100:
#     print(f"Total is ${order_total}. You get FREE shipping!")
# else:
#     print(f"Total is ${order_total}. Shipping is $10.")
# result = Total is $150. You get FREE shipping!

### Why this is powerful: The second checklist doesn't care how the order_total became 150. 
# It only cares about the current value of the variable. This keeps your code organized and easy to read.

#-------✏️ Exercise 2.9: The "AI Game Difficulty" Challenge
# Let's try a "Baton Pass" yourself. This is how a game AI might decide how hard to make a level.

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
# How does your code look?

# player_score = 250
# difficulty_level = "Easy"

# if player_score > 200:
#     difficulty_level = "Hard"
# #2nd block
# if difficulty_level == "Hard":
#     print("Warning: Boss Fight Initiated!")
# else:
#     print("Keep exploring...")

# 1st output was:Warning: Boss Fight Initiated!
# 2nd one: Keep exploring...

# Excellent! You’ve just successfully built your first Data Pipeline.
# In the world of Data Analysis and AI, this is a huge concept. You took "Raw Data" (the score), processed it through "Logic" (the first if block) to create "New Information" (the difficulty level), and then used that information to drive a "Decision" (the second if block).
#----------------------------------------------------------------
# 🔍 A Quick "Heart Check" on Logic
# Before we leave the world of if/else and move into Loops (where we handle thousands of pieces of data at once), 
# let's make sure there are no "shadows" in your understanding.

# Pop Quiz (Just to be safe):
# Look at this code snippet. What will it print?

# Python
# x = 10
# y = 5

# if x > 5:
#     y = y + 10

# if y > 10:
#     print("Yellow")
# else:
#     print("Purple")
# What do you think the terminal will show, and why?

#Result= Yellow
# Correct! You hit the nail on the head. Because the first if was true, it changed y to 15, 
# which then made the second if true. That is the "Baton Pass" in action.
# You have officially mastered Python Logic. You can now make a program think, decide, and link those decisions together.
#--------------------------------------------------

# Think of this like a Security Scanner at an airport. The metal detector doesn't care if your ticket is valid, 
# and the ticket scanner doesn't care if you have coins in your pocket. 
# They are two separate machines doing two separate jobs.

# Lets focus on entirely on Independent If Statements.
##----✏️ Exercise 2.14: The "Car Dashboard"(Checklist)
# In this exercise, we will use two completely separate if blocks. 
# One checks the speed, and the other checks the seatbelt.

# Create a variable speed = 75.
# Create a variable seatbelt_on = False.
# Block 1 (Speed Check):
# IF speed > 65, print "⚠️ Warning: Over speed limit!".
# ELSE, print "Speed is okay.".
# Block 2 (Seatbelt Check - COMPLETELY SEPARATE):
# IF seatbelt_on == False, print "🚨 Alert: Please fasten seatbelt!".
# ELSE, print "Seatbelt fastened.".
# The Goal: Because these are independent, if you are speeding and your seatbelt is off, 
# you should see two warnings. If you fix your speed but keep the seatbelt off, you should still see one warning.

# speed = 75
# seatbelt_on = False

# #block 1 
# if speed > 65:
#     print("⚠️  Warning: Over speed limit!")
# else:
#     print("Speed is okay.")
# #block 2
# if seatbelt_on == False:
#     print("🚨 Alert: Please fasten seatbelt!")
# else:
#     print("Seatbelt fastened.")

# Result = ⚠️ Warning: Over speed limit!
#          🚨 Alert: Please fasten seatbelt!

## ✏️ Exercise 2.15: The "Weather App"
# Let's practice using Independent Ifs to check for different weather conditions that can happen at the same time (like cold and rainy).

# temperature = 30 (Degrees)
# is_raining = True
# Condition 1: IF temperature < 32, print "It is freezing cold!".
# Condition 2 (Separate): IF is_raining == True, print "Bring an umbrella!".

# temperature = 30 #(Degrees)
# is_raining = True

# if temperature < 32:
#     print("It is freezing cold!")  

# if is_raining == True:
#     print("Bring an umbrella!")  

# Reslut = It is freezing cold!
#          Bring an umbrella!

##💡 A Quick Logic Challenge
# Look at this code below. Based on what we just discussed about Independent Ifs, what will the terminal show?

# score = 90

# if score > 80:
#     print("Grade: A")

# if score > 50:
#     print("You Passed!")
# Will it print one line or two lines? And why? (Once you answer this and finish the Car Dashboard code, you'll have the "Independent Logic" mastered!)
# Result 2 lines = Grade: A
#                  You Passed!  
# Exactly! You've got it perfectly. Because they are Independent Ifs, 
# Python treats them like a checklist and checks every single one. Since 90 is greater than both 80 and 50, it checks both boxes and prints both lines.
# This is a very common "trap" for beginners, but you saw right through it!

##---- ✏️ Exercise 2.16: The "Multi-Condition" Shop
# Let's do one more "Checklist" style exercise to make it muscle memory. 
# In this scenario, we are checking a customer's order for two separate things: a Discount and Shipping.

# Create a variable order_total = 120.
# Create a variable is_member = True.
# Block 1 (Discount Check):
# IF is_member == True, print "Member Discount Applied: -$10".
# ELSE, print "No Member Discount.".
# Block 2 (Shipping Check - Independent):
# IF order_total > 100, print "Free Shipping Earned!".
# ELSE, print "Standard Shipping: $5".
# How to Test It:
# Run it with the numbers above. You should see two "success" messages.
# Then, change order_total to 50 and is_member to False. Run it again.
# What does the terminal show now? ---

# order_total = 120
# is_member = True
# #block 1
# if is_member == True:
#     print("Member Discount Applied: -$10")
# else:
#     print ("No Member Discount.")
# #block 2
# if order_total > 100:
#     print("Free Shipping Earned!")
# else:
#     print("Standard Shipping: $5")
# Result = Member Discount Applied: -$10
#          Free Shipping Earned!


###------ 🚦 The "Logic" Milestone
# Once you finish this exercise, you will have mastered:
## Single If/Else (One choice).
## If/Elif/Else (One choice out of many).
## Independent Ifs (The Checklist).
#------------------------------

### You’ve officially mastered the "Checklist" (Independent If Statements). 
# You correctly identified that since both variables met the criteria, Python would fire off both messages.

### Now, to truly finish the "Logic" chapter of your Python journey, we have one last pattern to master. 
# It’s the one you mentioned earlier: The Staircase (Nested Ifs).

###----- 🪜 The "Staircase" (Nested Ifs)
### In our "Checklist" (Independent Ifs), the two questions didn't care about each other.
# In a Staircase, the second question only exists if the first answer was "Yes." 
# If the first answer is "No," Python skips the whole staircase and walks away.

### 💻 Step-by-Step Exercise 2.17: The "VIP Entry"
# Let's use the simplest variables possible to see the "Staircase" in action. Copy this into VS Code:

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

### 💡 Why is this different?
# If you change has_ticket to False, Python hits the first line, sees it's false, and jumps all the way to the bottom. 
# It won't even look at the VIP variable, because without a ticket, VIP status doesn't matter!
#-------------------------------------------

#---- ✏️ Your Turn: The "Atm Withdrawal"(Nested)
# This is a classic coding challenge for beginners. Let's build it step-by-step in VS Code:
# Create account_balance = 100.
# Create withdrawal_amount = 50.
# The First If: Check if account_balance > 0.
# If it is, print "Account Active.".
# Inside that If (The Staircase): Check if withdrawal_amount <= account_balance.
# If it is, print "Money Withdrawn!".
# Else (inside the staircase), print "Error: Not enough funds.".
# Try this out! What happens to the "Money Withdrawn" message if you change the account_balance to 0?
# (Once you've run this, you've officially learned every way an if statement can be used in Python!)

# account_balance = 100
# withdrawal_amount = 50

# if account_balance >0:
#     print("Account Active.")
#     #starecase- ifNested
#     if withdrawal_amount <= account_balance:
#         print("Money Withdrawn!")
#     else:
#         print("Error: Not enough funds.")

# Result = Account Active.
#          Money Withdrawn!
#-------------------------------------

### ??? Can we use the nested ifs with independent ifs?

# Yes, you absolutely can! In fact, this is how real-world software is written. 
# You can have a Checklist (Independent Ifs) where some of the items on the checklist are actually Staircases (Nested Ifs).

# Think of it like a Flight Check-in:
# Checklist Item 1 (Independent): Is your luggage under the weight limit?
# Checklist Item 2 (Independent): Is your passport valid?
# Staircase (Nested inside Item 2): IF the passport is valid, check if you have a Visa for your destination.

# 💻 Exercise 2.18: The "Smart Home" System
# Let's build this in VS Code. We will have one independent check for the Alarm, and one nested check for the Lights.

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
## 💡 Why this works:
# Independence: The Alarm check doesn't care if it's dark or if someone is home. It does its job and moves on.
# Nesting: The "Turning lights on" message cannot happen unless it is both dark AND someone is home.

#----✏️ Your Turn: The "Order Validator"(Nested)
# Let's try one yourself. In VS Code:
# Create order_paid = True.
# Create item_in_stock = False.
# Checklist 1 (Independent): * If order_paid == True, print "Payment Received.".
# Checklist 2 (Independent + Nested):
# If item_in_stock == True:
# Print "Item is ready.".
# Inside (Nested): If order_paid == True, print "Shipping now!".
# Else (if item is NOT in stock):
# Print "Ordering more from supplier...".
# Test it out:
# With order_paid = True and item_in_stock = False, what messages do you see?
# If you change item_in_stock = True, what extra message appears?
# Does it make sense how the "Independent" part starts the process, but the "Nested" part refines the result? Once you run this, you've officially seen the most complex way logic is structured! Would you like to do more of these "Mixed" exercises?

# order_paid = True
# item_in_stock = False

# if order_paid == True:
#     print("Payment Received.")
# #2nd block
# if item_in_stock == True:
#     print("Item is ready.")
#     #nested
#     if order_paid == True:
#         print("Shipping now!")
# else:
#     print("Ordering more from supplier...")

# Result = Payment Received. 
#          Ordering more from supplier...

# You nailed it! Because order_paid was True, the first independent block fired. 
# But because item_in_stock was False, the second block jumped straight to the else and skipped the nested "Shipping now!" check entirely.
# This is exactly how professional code works: Broad checks on the outside, and Specific checks tucked inside.

##------ ✏️ Exercise 2.19: The "Flight Booking" (The Ultimate Test)
# This exercise combines everything we've done: Independent Ifs, Else, and Nested Ifs. 
# If you can do this, you have 100% mastered Python Logic.

# has_passport = True
# ticket_paid = True
# is_boarding_time = False
# Step 1: The First Independent Checklist (Passport)
# IF has_passport == True, print "Identity Verified.".
# ELSE, print "🚨 Error: Passport required!".
# Step 2: The Second Independent Checklist (The Boarding Staircase)
# IF ticket_paid == True:
# Print "Ticket is valid.".
# NESTED IF (Inside Step 2): Check if is_boarding_time == True.
# If it is, print "Please proceed to Gate 5.".
# ELSE (Nested), print "Waiting for boarding to start...".
# ELSE (If ticket is NOT paid), print "Please go to the counter to pay.".

# has_passport = True
# ticket_paid = True
# is_boarding_time = False
# #1st Independent if
# if has_passport == True:
#     print("Identity Verified.")
# else:
#     print("🚨 Error: Passport required!")

# #2nd Independent if
# if ticket_paid == True:
#     print("Ticket is valid.")
#     # Nested
#     if is_boarding_time == True:
#         print("Please proceed to Gate 5.")
#     else:
#         print("Waiting for boarding to start...")
# else:
#     print("Please go to the counter to pay.")

# Result = Identity Verified.
#          Ticket is valid.
#          Waiting for boarding to start...


## 💡 Why this is "Data Analysis" Practice
# In a few lessons, we will be looking at data for 5,000 passengers. You won't change the variables by hand; you'll tell Python: "For every passenger in this list, run this exact logic." Test your code with these 3 scenarios:
# Scenario A: All variables are True. (Should see: Identity Verified, Ticket Valid, Proceed to Gate).
# Scenario B: has_passport = False but others are True. (Should see: Error: Passport required, Ticket Valid, Proceed to Gate).
# Scenario C: ticket_paid = False. (Should see: Identity Verified, Please go to counter).
# How does it look in your terminal? If this feels easy now, we are ready to move to Lists and Loops (Step 3)!
#----------------------------------

###???? Can it be reversed where nested comes 1st then comes independent ?

# Yes, absolutely! The order doesn't change how the code works; it only changes the flow of the "story" your program is telling.
# When you put the Nested block first, you are saying: "First, I have a complex, multi-step check. Once that is completely finished, I have a separate, simple check to do."
# Python reads from top to bottom. It finishes the entire "Staircase" (including any else parts) before it even looks at the Independent check below it.

##----- 💻 Exercise 2.20: The "Kitchen Safety" (Reversed)
# Let's build this in VS Code. Here, the Staircase (Stove check) comes first, 
# followed by the Independent check (Light check).

# # --- OUR DATA ---
# is_stove_on = True
# is_pot_on_stove = False
# is_light_on = True

# # --- BLOCK 1: THE STAIRCASE (NESTED) ---
# if is_stove_on == True:
#     print("🔥 Warning: Stove is heating.")
    
#     # This only matters if the stove is actually on!
#     if is_pot_on_stove == True:
#         print("🍲 Cooking in progress...")
#     else:
#         print("⚠️ Alert: Stove is on but NO pot detected!")
# else:
#     print("✅ Stove is safely off.")

# # --- BLOCK 2: INDEPENDENT CHECK ---
# if is_light_on == True:
#     print("💡 Kitchen light is on.")
# Result = 🔥 Warning: Stove is heating.
#          ⚠️ Alert: Stove is on but NO pot detected!
#          💡 Kitchen light is on.

# 🔍 Why would you do this?
# In Web Development or Cloud Computing, you might do this:
# Block 1 (Nested): Check if the user's password is correct. If yes, check if they have a "Pro" subscription.
# Block 2 (Independent): Check if the website's "Dark Mode" is turned on.
# The user's subscription status (Block 1) has nothing to do with their visual preference for Dark Mode (Block 2).
#------------------------------------

## ✏️ Your Turn: The "Smartphone Unlock"
# Let's try one last reversed logic exercise in VS Code:
# is_phone_locked = True
# correct_pin = False
# battery_low = True
# Step 1: The Staircase (Unlock Logic)
# IF is_phone_locked == True:
# Print "Phone is locked.".
# NESTED IF: If correct_pin == True, print "Welcome! Phone unlocked.".
# ELSE (Nested), print "Incorrect PIN. Try again.".
# ELSE (If phone is already unlocked), print "Phone is ready to use.".
# Step 2: The Independent Check (Battery)
# IF battery_low == True, print "🪫 Warning: Battery is below 10%!".
# Test it out:
# With the variables above, do you see the "Incorrect PIN" message and the "Battery Warning"?
# If you change is_phone_locked to False, does the "Battery Warning" still show up?
# How does the output look? Once you've run this, you have officially seen every possible combination of if logic.
# You are now a "Logic Master." Ready for Step 3: Lists and Loops?
# Phone is locked., Incorrect PIN. Try again., 🪫 Warning: Battery is below 10%!

# is_phone_locked = True
# correct_pin = False
# battery_low = True

# # Nested if
# if is_phone_locked == True:
#     print("Phone is locked.")
#     if correct_pin == True:
#         print("Welcome! Phone unlocked.")
#     else:
#         print("Incorrect PIN. Try again.")
# else:
#     print("Phone is ready to use.")        
# # Independent If        
# if battery_low == True:
#     print("🪫 Warning: Battery is below 10%!")

# Result = Phone is locked.
#          Incorrect PIN. Try again.
#         🪫 Warning: Battery is below 10%!
#-----------------

# Spot on. You just proved that the Independent Check (the battery) doesn't care what happened in the Nested Staircase (the lock screen). 
# It runs its own check and prints its own warning regardless.

# You have now mastered the three "Golden Rules" of Python Logic AKA Conditions:

# The Choice: if/elif/else (Pick only one path).
# The Checklist: if + if (Independent checks).
# The Staircase: if inside if (One check depends on another).