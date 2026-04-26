
# 📐 The Anatomy of a Python Script
# In VS Code, your code should look like this:

# Python
# # --- 1. SETTING UP OUR DATA ---
# # This is a 'Comment'. It starts with # and Python ignores it. 
# # We use it to explain what the code does to other humans.

# favorite_city = "Paris"    # This is a String (Text)
# temperature = 22.5         # This is a Float (Decimal Number)
# is_sunny = True            # This is a Boolean (True/False)

# # --- 2. SHOWING THE DATA ---
# # We use the print() function to send data to the terminal.

# print(favorite_city)
# print(temperature)
# print(is_sunny)

#--------------💡 The "Pro" Concepts for Beginners----------
# To code like a professional from day one, remember these three rules:

# Snake Case: In Python, if a variable name has two words, 
## we separate them with an underscore (e.g., favorite_city, not favoritecity). It's easier to read!
## No Quotes for Numbers or Booleans: * "25" is text (you can't do math with it).
## 25 is a number (you can add/subtract it).
## True or False must always have a Capital Letter and no quotes.
## Comments are your Friend: Always use # to label your sections. 
## It helps you remember what you were thinking when you look at the code tomorrow.

#---------------- ✏️ Your Mastery Task (VS Code)-------
# Let's try one more "muscle memory" exercise before we move to math. 
# In your basics.py file, delete everything and write this from scratch:

# Create a comment at the top that says # My first Python script.
# Create a variable called my_age and set it to your age (a whole number).
# Create a variable called coding_is_fun and set it to True.
# Create a variable called price_of_coffee and set it to a decimal (like 3.50).
# Use print() for each one.

# Run it in VS Code. Did it work, or did you get a "SyntaxError"? 
# (Don't worry if you did—errors are how we learn!)

# My first Python script.

# my_age = 56
# codeing_i_fun = True
# price_of_coffee = 5.5
# print (my_age )
# print (codeing_i_fun )
# print (price_of_coffee )

# Spot on! You nailed the syntax. You used the equals sign correctly, assigned the right data types, 
# and used the print() function perfectly.

# Since you want to code like a professional, I noticed one tiny thing in your variable name: codeing_i_fun. 
# In a real project, we try to be very precise with spelling because if you try to print coding_is_fun later, 
# Python will get confused and give you an error. Accuracy is a coder's best friend!
#------------------------------------

#--------- 📊 Understanding Data Types (The "Heart" of Data Analysis)------
# Before we move to math, you need to know what you just created. In Python, every piece of data has a "Type." 
# This is crucial for Data Analysis and AI later on.

# Name	      Technical Term	       Example	   What it is
# Text	       str (String)	           "Paris"	   Anything inside quotes.
# Whole Number   int (Integer)	        56	       Numbers without decimals.
# Decimal	       float (Floating Point)	5.5	       Numbers with a decimal point.
# Logic	       bool (Boolean)	       True	Only two values: True or False.

##🔢 Step 2: Basic Math & F-Strings
# Now let's make the computer actually do something with those numbers. 
# We use standard symbols: +, -, * (multiply), and / (divide).

# To make our output look professional (like a real website or app), we use F-Strings. 
# It stands for "Formatted String." It lets us put variables directly inside a sentence.

# Copy this into your VS Code to see how it looks:

# Python
# # --- CALCULATIONS ---
# years_to_retirement = 65 - my_age  # Math!

# # --- THE PRO WAY TO PRINT (F-Strings) ---
# # Notice the 'f' before the quotes and the { } around variables
# print(f"In 10 years, I will be {my_age + 10} years old.")
# print(f"I have {years_to_retirement} years until I am 65.")

## ✏️ Exercise 1.2 (The VS Code Challenge)
# Let's practice math and F-strings. In your basics.py file:
# Create a variable coffee_price = 5.50.
# Create a variable cups_per_week = 7.
# Create a third variable called total_spent that multiplies the two (use *).
# Use an F-String to print a sentence like: I spend 38.5 dollars on coffee per week. 
# (But use your variable so it calculates automatically!)
# Does the math come out correctly in your terminal?

# coffee_price = 5.50
# cups_per_week = 7
# total_spent = coffee_price * cups_per_week
# print(f"I spend {total_spent} dollars on coffee per week.")

# Perfect! You’ve just mastered Variables, Math Operators, and F-Strings. 
# That is the foundation of every AI and Data Analysis script.
# The computer handled the calculation ($5.50 \times 7 = 38.5$) and plugged it right into your sentence.