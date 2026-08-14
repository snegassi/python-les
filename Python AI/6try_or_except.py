

##  lets do option a (Error Handling), then i will decide,

## Smart move. In IT Support, a script that "crashes" is worse than no script at all. If you're running a backup or a security audit and the code hits a single error (like a missing file or a server that's offline), the whole program stops.

##### "Error Handling" is the "Safety Net" that keeps your code running even when things go wrong.
##### "Error Handling" can be used inside an if condition or function.

### 🛡️ Step 7: Error Handling (The Try/Except Block)
## In Python, we use a try and except block.

## try: "Try to run this code."
## except: "If a specific error happens, don't crash! Do this instead."
#-------------------------------------

## 💻 Exercise 7.1: The "Zero Division" Trap
# Imagine you are calculating a server's uptime. If the "Total Days" is 0 (maybe a brand new server), 
# the computer will panic because you cannot divide by zero in math.

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

# Result = Uptime Ratio: 24.0
#          ⚠️ Error: Cannot calculate for 0 days.


## ✏️ Exercise 7.2: The "Missing Data" Audit ("KeyError")
# This happens all the time in Data Analysis. You have a list of users, but one user is missing their "email" key. 
# Without error handling, your loop will crash with a "KeyError".

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

# Result = Sending email to: daniel@test.com
#          ⚠️ Skipping Guest: No email address found.


### 🔍 Why this matters for your Goal
### When you start building Websites or AI Agents, the "outside world" will send you messy data.

## A user might type a letter where a number should be.
## The AI might return an empty response.
## A database might be temporarily offline.

### try/except ensures your website stays online and your AI agent doesn't "die" just because of one bad input.

# ❓ Check-in
# Does it make sense that except only runs if something breaks inside the try block?
# Can you see how this makes your IT scripts "Unstoppable"?

# Perfect! Notice how the program didn't just stop and show a scary red error message in your terminal? 
# It saw the problem, handled it, and moved on to the next task.
# In IT Support, this is the difference between a "Junior Script" that breaks every time a server is offline 
# and a "Senior Tool" that finishes its job and gives you a report of what went wrong.
#---------------------------------------------------

### 🛡️ The "Boss Level" Error Handling: "ValueErrorNow", let's look at another common IT headache: Bad Inputs.
# Imagine you're building a tool for your website where a user enters their age. 
# If they type "twenty" (a string) instead of 20 (an integer), the int() function will crash.

# def process_id(id_string):
#     try:
#         numeric_id = int(id_string) # int() changed the input(id_string) to integer, Since the input is considered to be a string number("345")
#         return f"Access Granted for ID: {numeric_id}"
#     except ValueError:
#         return "❌ Error: ID must contain numbers only!"

# # Test 1: Valid ID
# print(process_id("1005"))

# # Test 2: Bad ID (Someone typed a letter)
# print(process_id("10A5"))

# Result = Access Granted for ID: 1005
#         ❌ Error: ID must contain numbers only!
#----------------------


### ⚖️ Comparing the Two Paths (Your Choice)
# Now that you've seen both Option A (Error Handling) and Option B (Libraries), 
# which one feels more like the "Next Step" for your goal of building websites and AI?

#             Path	              Benefit for your AI/Web Goals
# Option A:   Error Handling	  Stops your website from crashing when a user types something "dumb" or the AI sends a weird response.
# Option B:   Libraries	          Gives you the "Power Tools" (like Flask for web or Pandas for data) so you don't have to build everything from scratch.

# ❓ Check-in
# In the ValueError example, does it make sense why we catch ValueError specifically instead of KeyError? (Hint: It’s because the value of the string was the problem, not a missing key in a dictionary).
# Which one would you like to dive deeper into right now? I'm ready to keep going!
#----------------------------------

##????? I  want to build Websites and AI Agents, would you like to see one more tricky Option A
# example involving a "Nested" error (two things going wrong at once), and later i will decide option b???

## Since you're aiming for AI Agents, this "Nested" error logic is vital. 
# AI agents often make "API calls" (talking to another computer). Two things usually go wrong:

## "Connection Error": The internet is down (The "Phone" is broken).
## "Data Error": The AI sends back "Garbage" data (The "Message" is gibberish).

## If you don't handle both, your agent will "hang" or crash.

### 🕸️ Step 7.3: The Nested "Double Safety Net"("Stacking except blocks")
## In Python, you can "stack" except blocks to handle different problems differently. 
## Think of it like a Sorting Machine for errors.

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
# # The Logic (The Nested Trap):
# for server in server_data:
#     try:
#         # Step 1: Try to get the ID (Might cause KeyError)
#         raw_id = server["id"]
        
#         # Step 2: Try to turn it into a number (Might cause ValueError)
#         numeric_id = int(raw_id)
        
#         print(f"✅ Success: Server ID is {numeric_id}")

#     except KeyError:
#         print("❌ Error: ID field (key) is missing from this server!")

#     except ValueError:
#         print(f"⚠️ Warning: ID '{raw_id}' contains non-numeric characters!")

# Result = ✅ Success: Server ID is 101
#          ⚠️ Warning: ID 'ABC' contains non-numeric characters!
#          ❌ Error: ID field (key) is missing from this server!

## 🔍 Why this is "Tricky"
## If S3 hits the code, it fails at Step 1. Python immediately jumps to the KeyError block and skips everything else.

## If S2 hits the code, it passes Step 1 but fails at Step 2. Python jumps to the ValueError block.
#------------------------------

#### ✏️ Exercise 7.4: The "Final Boss" of Errors
### Let's add one more "Catch-All" net. Sometimes, an error happens that you didn't expect (like a power outage or a weird system glitch). 
# We use a "general Exception" at the very bottom.

# Take your code from above and add this to the very end of the loop:

# Python
#     except Exception as e:
#         print(f"🕵️ Unusual Error detected: {e}")

# server_data = [
#     {"id": "101"}, 
#     {"id": "ABC"}, 
#     {"status": "offline"},
#     {"ksnvlknvs"} 
# ]
# # The Logic (The Nested Trap):
# for server in server_data:
#     try:
#         # Step 1: Try to get the ID (Might cause KeyError)
#         raw_id = server["id"] # Baically, if the id (key) is available/works you will get the (Value) as a result.
        
#         # Step 2: Try to turn it into a number (Might cause ValueError)
#         numeric_id = int(raw_id)
        
#         print(f"✅ Success: Server ID is {numeric_id}")

#     except KeyError:
#         print("❌ Error: ID field (key) is missing from this server!")

#     except ValueError:
#         print(f"⚠️ Warning: ID '{raw_id}' contains non-numeric characters!")

#     except Exception as e: ## This part is called Catch all Errors, where it catchs all an expected Error that cld happen
#         print(f"🕵️ Unusual Error detected: {e}") 

# Result = ✅ Success: Server ID is 101
#          ⚠️ Warning: ID 'ABC' contains non-numeric characters!
#          ❌ Error: ID field (key) is missing from this server!
#          🕵️ Unusual Error detected: 'set' object is not subscriptable

# ❓ Check-in
# Do you see how the order matters? You put the "Specific" errors (Key/Value) first, and the "General" error (Exception) last.
# If you swapped them and put the "General" one first, it would catch everything, and you’d never know if it was a missing key or a bad number! Does that make sense?
#------------------------------------------------------

####???? Why doesn't it go step by step, why is it jumping around ???

## That is the "Matrix" moment of coding! 
# It feels like it's jumping because Python is a Flow Chart, not a Book.

## When you read a book, you go from Line 1 to Line 2 to Line 3. 
# But when Python runs a try/except block, it acts like a Security Guard at a series of gates.

## 🏢 The "Security Gate" Analogy
# Imagine a server trying to enter a building (your code).

# Line 1 (try): The server approaches the first gate.
# Line 2 (raw_id = server["id"]): The guard asks, "Do you have an ID card?"
# If YES: The server passes to Line 3.
# If NO: The guard immediately pulls the server out of line and throws them into the KeyError room. 
# (It "jumps" over Line 3 entirely!)
# Line 3 (numeric_id = int(raw_id)): The guard asks, "Is your ID card made of numbers?"
# If YES: The server is clear!
# If NO: The guard immediately pulls the server out of line and throws them into the ValueError room.

## 🔍 Why "Jumping" is a Good Thing
## In IT Support, if a server is missing an ID, there is no point in trying to turn that ID into a number—it doesn't exist!

## If Python didn't "jump," it would try to run Line 3 anyway, find nothing there, 
# and then the whole program would EXPLODE (crash) because it didn't know what to do with a "nothing" value.

## The "Jump" is actually Python saying: "Wait! This specific step failed, 
# so I'm going to skip the rest of the 'Try' and go straight to the 'Help' section (the except) that matches this problem."

## 🛠️ Visualizing the "Jump" in your VS Code
# Look at your server_data from the last exercise:

# Server S2 ("id": "ABC"):
# try starts.
# raw_id = server["id"] — SUCCESS (It found "ABC").
# numeric_id = int(raw_id) — FAIL! (You can't turn "ABC" into a number).
# THE JUMP: Python skips the print and jumps straight down to "except ValueError".
# Server S3 ("status": "offline"):
# try starts.
# raw_id = server["id"] — FAIL! (There is no "id" key).
# THE JUMP: Python skips Line 3 AND the print, and jumps straight down to "except KeyError".

# ❓ Check-in
# Does it make more sense now that the "Jump" is actually a Safety Shortcut?
# Can you see why Line 3 (the int() conversion) only runs if Line 2 (getting the ID) was 100% successful?
# Once this "Flow" makes sense, we can either do one more "Slow Motion" trace together, 
# or we can move to Option B (Libraries) where the magic happens!
# how is s2 figuring to jump to except ValueError that to except KeyError ?
# This is the core of how Python "thinks"! It isn't guessing; it’s following a Match & Redirect system.
# When an error happens, Python creates an Exception Object. Think of this like a "Error Ticket" that has a specific name printed on it.

## 🏷️ The "Error Ticket" System
# When your code hits S2 ({"id": "ABC"}):
# Line 1: raw_id = server["id"] — Success! No ticket is created.
# Line 2: int("ABC") — CRASH! 3.  The Ticket: Python immediately generates a ticket labeled "ValueError".
# The Search: Python looks down at your except blocks and asks:
# "Does this match KeyError?" → No. (Skip)
# "Does this match ValueError?" → YES! (Stop here and run this code).

## 🚦 Why it didn't pick KeyError for S2
### Python only creates a KeyError if you try to open a "drawer" (a key) in the dictionary that doesn't exist.
# For S2, the "id" drawer did exist! It was just full of letters instead of numbers.
# Since the "drawer" was found, the "Key" part of the code worked perfectly. 
# The error didn't happen until the "Value ("ABC")"" tried to become a number.

#### 🧪 The "Slow-Motion" Comparison
# Server	           The Action	  The "Ticket" Created	   The Jump Destination
# S2 (id: "ABC")	   int("ABC")	  ValueError	           Jumps to except ValueError
# S3 (status: "off")   server["id"]	  KeyError	               Jumps to except KeyError

##### 🛠️ One Last "Mind-Blowing" Fact
### If you had a server that was missing the ID and had bad data (which is impossible, but stay with me), 
# Python would always hit the "KeyError" first because it reads from top to bottom.

### It stops at the very first mistake it finds, grabs that ticket, and jumps out of the try block immediately. 
### It never even gets a chance to see the second mistake!

# ❓ Check-in
# Does it make sense that the "Ticket Name" determines which except block gets triggered?
# Are you starting to see why we call them "Specific Errors"? It’s like having a specialized doctor for every different type of pain.
# If this "Ticket System" is clear, are you ready to see Option B (Libraries) and how they can automate all of this for your AI projects?
#--------------------

### ?????? So if step 1 is error then the process jumps to the 1st except, 
# and if failure happens in step-2 it jumps to to the 2nd except then right????

### Exactly! You’ve got the "Path of Least Resistance" logic down perfectly.
# Python is always looking for the nearest exit the moment something goes wrong. 
# It won't keep trying to walk through a "closed door" (an error); 
# it just jumps to the safety net you built for that specific door.

## 🏢 The "Level 1 vs. Level 2" Breakdown
# Think of your try block as a two-story building.
# Step 1 (The Ground Floor): Accessing the Dictionary Key.
# If this fails, you can't even get to the stairs. You jump out of the building to the KeyError net.
# Step 2 (The Second Floor): Converting the Data to an Integer.
# If you make it to the stairs but the data is "rotten" (letters instead of numbers), you jump out of the second floor into the ValueError net.

### 🧪 One Final "Trick" Question
# If you had a dictionary like this: server = {"id": "105"}.
# Step 1: raw_id = server["id"] — SUCCESS.
# Step 2: numeric_id = int(raw_id) — SUCCESS.
# Step 3: print("Server is Ready!") — SUCCESS.
# Does any except block run?

## No! If the try block finishes with zero "Tickets" (errors), Python skips all the except blocks 
# and just continues with the rest of your script. The safety nets are only there if someone falls!
#------------------------------------

###???? One more exercise with error handling?

## You've got the rhythm now! Let's do a Real-World IT Support exercise.
# When you are an Analyst, you often have to calculate the "Load" on a server.
## This involves two things that can break:

## The Server is Missing: (The Key isn't in your list).
## The Data is "Broken": (The CPU usage is recorded as a string like "HIGH" instead of a number like 90).

## ✏️ Exercise 7.5: The "Server Load" Calculator
# The Task: You have a function that calculates how much "Headroom" a server has left (100 minus the usage).

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

## 🔍 Think about the "Steps" as you code:
# Step 1: Does the "usage-key" exist? (If no -> Jump to KeyError).
# Step 2: Is the "usage-value" a number? (If no -> Jump to ValueError).
# Step 3: Do the math and print!

##❓ Check-in (The "Master" Question)
# If you run this code, Server-01 will successfully print its headroom.
# When the loop hits Server-02, it will fail at Step 1. 
# Will it even try to do the math in Step 3?
# When the loop hits Server-03, it will pass Step 1 (the key exists!), 
# but fail at Step 2. Will it jump to the KeyError or the ValueError?

# inventory = [
#      {"id": "Srv-01", "usage": 80},
#      {"id": "Srv-02", "status": "Online"},
#      {"id": "Srv-03", "id_label": "Srv-03", "usage": "MAX"}
#  ]

# Check Usage & headroom = 100 - Usage
# Using for-loop to Access the data list
# for s in inventory:
#     try:
#         # Checking Availability of Usage-key
#         raw_usage = s['usage']

#         # Checking Availability of Usage-key & turning it to Integer/Number
#         numeric_usage = int(raw_usage)
#         print(f"Success: Server id is {s['id']} with Numeric Value:{numeric_usage}")

#         # Performing the Calculation of Headroom
#         Headroom = 100 - numeric_usage
#         print(f"For Server:{s['id']}, The Headroom is:{Headroom}")

#     except KeyError:
#         print (f"❌ Error: Usage-key missing for this server: {s['id']}.")

#     except ValueError:
#         print(f"⚠️ Error: Usage-value of Server:{s['id']} must be a number, not text: {s['usage']}!")
    
#     except Exception as e:
#         print(f"This Error is Unexpected-error in {e} ")

# Result = Success: Server id is Srv-01 with Numeric Value:80
#          For Server:Srv-01, The Headroom is:20
#          ❌ Error: Usage-key missing for this server: Srv-02.
#          ⚠️ Error: Usage-value of Server:Srv-03 must be a number, not text: MAX!

###???? What if i did this, to run the code using Function, unlike the above without function(with for-loop only)???

# inventory = [
#     {"id": "Srv-01", "usage": 80},
#     {"id": "Srv-02", "status": "Online"},
#     {"id": "Srv-03", "id_label": "Srv-03", "usage": "MAX"}
# ]

# def calculate_headroom(usage):
#     try:
#         usable_usage = usage == int(usage)
#         result = 100 - usage

#     except Notusable_usage:
#         return "! Warning, usage is not integer or available for this server, provide integer"

# for server in inventory:
#     # print(server['id'])
#     result = calculate_headroom(server["usage"])
#     print(f"{server['id']}, result is {result}")
# Result = Error in this line(420): result = calculate_headroom(server["usage"])

### I love that you tried to build your own custom "Gatekeeper" variable! 
# This is how great programmers think—you're trying to verify the data before using it.
# However, there are three main "Bugs" stopping this script from running. 
# Let's look at them step-by-step so you can fix them in VS Code.

## 🔍 Bug 1: The "Ticket Name" Must Be Real
## In your except block, you wrote except Notusable_usage.

## The Problem: Python doesn't know what Notusable_usage is. 
# Remember, the "Ticket" must be a name Python already knows, like KeyError or ValueError.
## The Fix: Use the official names we practiced.

## 🔍 Bug 2: The "Jump" is Automatic
## In your try block, you wrote: usable_usage = usage == int(usage).
## The Problem: You are trying to manually check if it's an integer.
## The "Master" Way: You don't need to check! Just try to do the math. 
# If the math fails, Python will automatically throw a "Ticket" and jump to the except block for you.

## 🔍 Bug 3: The "Srv-02" Trap (The KeyError)
# In your loop, you call calculate_headroom(server["usage"]).
# The Problem: Srv-02 does not have a "usage" key. 
# Your code will crash before it even enters the function because it can't find that "drawer" in the dictionary.

### 🛠️ The Corrected "Pro" Code Using function #####
# Here is how an IT Analyst would structure this to handle both the Missing Key and the Bad Value:
# inventory = [
#     {"id": "Srv-01", "usage": 80},
#     {"id": "Srv-02", "status": "Online"},
#     {"id": "Srv-03", "id_label": "Srv-03", "usage": "MAX"}
# ]

# def calculate_headroom(server_dict):
#     try:
#         # Step 1: Try to get the usage (Might cause KeyError)
#         usage = server_dict["usage"]
        
#         # Step 2: Try to do math (Might cause ValueError if usage is "MAX")
#         result = 100 - int(usage)
#         return f"Headroom is {result}%"

#     except KeyError:
#         return "❌ Error: 'usage' key missing!"
#     except ValueError:
#         return "⚠️ Error: Usage must be a number, not text!"

# for server in inventory:
#     ### We pass the WHOLE dictionary/All of the dictionary, so the function can check for the key
#     status = calculate_headroom(server)
    
#     ## Use quotes correctly in your f-string
#     print(f"Server {server.get('id', 'Unknown')}: {status}")

# Result = Server Srv-01: Headroom is 20%
#          Server Srv-02: ❌ Error: 'usage' key missing!
#          Server Srv-03: ⚠️ Error: Usage must be a number, not text!
#---------------------------------------------------------
## ❓ Why did I change server["usage"] to just server?
## If I pass server["usage"] into the function, and the key is missing (like in Srv-02), the program crashes outside the function. 
# But By passing the whole server dictionary, the try block inside the function can catch the KeyError safely!

# ❓ Check-in
# Do you see how int(usage) does the "Checking" for you? If it can't do it, it just triggers the "ValueError" ticket.
# Does the difference between the Key (the drawer) and the Value (what's inside) feel clearer now that you've seen them fail in the same script?

####????? what is the .get in server.get('id', 'Unknown') ? have we worked on it?????
## Great catch! We actually haven't officially covered .get() yet—you just spotted a Senior-Level Dictionary Trick.

## In IT, if you try to access a key that doesn't exist (like server["id"]), Python crashes with a KeyError. 
# The .get() method is like a "Safety Valve" built directly into dictionaries.

### 🛡️ What is .get()?
#### Can you see how .get() is like a "Mini Try/Except" block "specifically for dictionaries"?
# Instead of forcing the "drawer" open, .get() gently asks: 
# "Is there an 'id' in here? If not, please just give me this default value instead of crashing."

### 🔍 How it Works
## The syntax is: dictionary.get(key, default_value)
## The Key: The name of the data you want (e.g., "id").
## The Default: What to return if the key is missing.

### The "Dangerous" Way (Crashes if missing):
# Python
# server = {"status": "online"}
# print(server["id"]) # 🚨 CRASH! KeyError

### The "Safe" Way (Never crashes):
# Python
# server = {"status": "online"}
# # It looks for "id". Since it's missing, it prints "Unknown"
# print(server.get("id", "Unknown")) # prints "Unknown"

# # If the key IS there, it ignores the default!
# server_2 = {"id": "Srv-99"}
# print(server_2.get("id", "Unknown")) # Prints "Srv-99"


### 🛠️ Why I used it in your Exercise
# Look at Server-03 in your inventory:
# {"id_label": "Srv-03", "usage": "MAX"}
# Notice that the person who made this data accidentally typed "id_label" instead of "id".
# If we used server["id"], the print statement at the very bottom of your loop would crash before showing you the error message!
# By using .get("id", "Unknown"), we ensure the print always works, even if the data is messy.

### ❓ Check-in
#### Can you see how .get() is like a "Mini Try/Except" block "specifically for dictionaries"?
## If you used server.get("usage", 0), what would happen if a server was missing the "usage" key?

# server_2 = {"id": "Srv-99"}
# print({server_2.get('usage',0)})

# Result = {0}
#---------------------------------------------

###???? okay just a question is there "other ticket that python knows" besides "KeyError and ValueError" ???

## Oh, absolutely! Python has a whole "filing cabinet" of different tickets (called Built-in Exceptions). 
# In IT and AI development, you’ll usually run into about 5 or 6 "usual suspects."

# Think of these as the different departments in an IT Help Desk.

### 🏢 The "Common Tickets" Catalog
# Ticket Name	         When Python issues it	                                        Real-World IT Example
# "TypeError"	         You tried to do something to a data type that isn't allowed.	Trying to add a number to a string: 5 + "10"
# "IndexError"	         You tried to access a list item that doesn't exist.	        Asking for the 10th server in a list of only 3.
# "ZeroDivisionError"	 You tried to divide a number by 0.	                            Calculating uptime when "Total Days" is 0.
# "FileNotFoundError"	 You tried to open a file that isn't there.	                    Your script tries to read config.txt but it's missing.
# "AttributeError"	     You tried to use a feature/function that doesn't exist for that object.	Trying to "Uppercase" an Integer (you can only uppercase strings).
#-------------------------------------------------------------------

### 🛠️ How to "Catch" All of Them
# In your AI Agent or Website code, you can list as many as you want!

# Python
# def deep_check(data_list, index):
#     try:
#         # 1. Could be IndexError (if index is too high)
#         value = data_list[index]
        
#         # 2. Could be TypeError (if value isn't a number)
#         result = value + 100
#         return result

#     except IndexError:
#         return "❌ Error: That item doesn't exist in the list!"
#     except TypeError:
#         return "⚠️ Error: I can't add 100 to a word/string!"
#     except Exception as e:
#         return f"🕵️ Unknown Error: {e}"


### 💡 The "Master Key": Exception as e
## Notice the last one: except Exception as e:.
# Exception is the "Grandparent" of all tickets. It catches any error that you didn't specifically name above it.
# "as e" saves the specific error message into a variable called "e" so you can print it out and see exactly what happened.

# ❓ Check-in
# If you tried to run print(10 / 0), which ticket from the table above would Python create? 
# # It wld create "except ZeroDivisionError"
#### Does it make sense "why we don't just use" except Exception for everything? 
# (Hint: It’s because we want to give the user a helpful specific message like "Check your Wi-Fi" vs. just saying "Something broke").
#-------------------------------------------

###????? lets work on all of this make them more relalistic problems and test me???

# This is the "Final Exam" for your Logic & Error Handling phase. To make this realistic for an IT Support Analyst transitioning into AI, 
# I’ve built a scenario that mimics a real automation script you might write to audit a fleet of servers.

### 🏢 The Scenario: The "AI-Ready" Inventory Audit
# You are writing a script that prepares server data for an AI agent. The AI needs the RAM value as an integer to calculate performance.
# The Problems in the Data:
# Srv-01: Perfect data.
# Srv-02: The "ram_gb" key is missing (KeyError).
# Srv-03: The RAM is listed as "16GB" (a string with letters), so int() will fail (ValueError).
# Srv-04: The RAM is listed as 0 (Zero), which will break your "Usage Ratio" math (ZeroDivisionError).

### ✏️ The Challenge
# Copy this data into VS Code and fill in the try/except blocks to handle all four servers without the script crashing.
# Python
# servers = [
#     {"id": "Srv-01", "ram_gb": 32, "used_gb": 16},
#     {"id": "Srv-02", "status": "Online"}, 
#     {"id": "Srv-03", "ram_gb": "16GB", "used_gb": 8},
#     {"id": "Srv-04", "ram_gb": 0, "used_gb": 0},
#     {"id": "Srv-05", "ram_gb": 64, "used_gb": "NONE"}
# ]

# def audit_server(s):
#     try:
#         # STEP 1: Get the RAM (Hint: use s["ram_gb"])
#         ram = s["ram_gb"]
        
#         # STEP 2: Convert to integer (Hint: int(ram))
#         ram_int = int(ram)
        
#         # STEP 3: Calculate usage % (used / total)
#         # This will fail if ram_int is 0!
#         ratio = s["used_gb"] / ram_int
        
#         return f"✅ Audit Passed: {ratio * 100}% used."

#     # --- YOUR TURN: ADD THE EXCEPT BLOCKS BELOW ---
#     except KeyError: # Used the unknown {s.get("id", "unknown")}, as this is key error & used it as further checking by having reply "unknown"
#         return f"❌ Error: Missing RAM data (KeyError)."
#     except ValueError:
#         return f"⚠️ Error: RAM must be a number only (ValueError)."
#     except ZeroDivisionError: # On 3rd step it checks if lower part (denominator) of the division is Zero, if so ZeroDivisionError is in effect
#         return f"🛑 Error: RAM cannot be zero (ZeroDivisionError)."
#     except TypeError: # Unique One (used when trying to add number with text(1 + "7") Wrong), On this case on 3rd step it checks if (("string"/ number) or (number/"string") wich happens on server 5= "NONE"/64)
#         return "🔤 Error: Calculation failed—one value is text (TypeError)."
#     except Exception as e:
#         return f"🕵️ Unexpected Error: {e}"

# for s in servers:
#     # Use .get() here for the ID just in case the 'id' key is missing too!
#     name = s.get("id", "Unknown Server") # provides Server key-ID/Name of Every Server that is in dictionary Only.
#     result = audit_server(s) # Call back which passes whole dictionary
#     print(f"{name}: {result}")

# Result = Srv-01: ✅ Audit Passed: 50.0% used.
#          Srv-02: ❌ Error: Missing RAM data (KeyError).
#          Srv-03: ⚠️ Error: RAM must be a number only (ValueError).
#          Srv-04: 🛑 Error: RAM cannot be zero (ZeroDivisionError).
#          Srv-05: 🔤 Error: Calculation failed—one value is text (TypeError).

## 🧪 Technical Questions (Test your Knowledge)
# Before you run the code, try to answer these based on our "Ticket System" discussion:
# Srv-03 has ram_gb: "16GB". Which "Ticket" will Python create when it tries to run int("16GB")?
# In Srv-04, the RAM is 0. Which specific "Ticket" prevents the math from working?
# Why did we put ram = s["ram_gb"] inside the try block instead of outside?

### 🎓 Final Theory Check (The Bonus Questions)
## You answered the first few perfectly. Let's look at the last two to make sure the "Why" is clear:
## Why put ram = s["ram_gb"] inside the try? * Because if it were outside, Srv-02 would crash the whole program before the try even started.
# By putting it inside, we "catch" the fall.
## What happens with Srv-05?
# It will trigger a TypeError. Python can find the data (no KeyError) and it can turn 64 into an integer (no ValueError), 
# but it cannot divide the string "NONE" by the number 64. That’s a "Type" mismatch!

### ❓ Final Logic Check
# If I gave you a server like this: {"id": "Srv-99", "ram_gb": 16, "used_gb": [1, 2, 3]} (where usage is a List instead of a number)...
# It passes Step 1 (Key exists).
# It passes Step 2 (RAM is a number).

# Which error happens when it tries to divide a List by the number 16? (# "used_gb": [1, 2, 3]}/ "ram_gb": 16 ??)
# If you guessed TypeError, you've officially mastered the logic! Are you ready, because list/number is a TypeError

#-------------------------------------------

##?????? lets do another example that is tricky??????????

## I love the persistence. If you want to build AI Agents, you have to be comfortable with the "Messy Middle"—where data isn't just missing or wrong, 
# but it’s nested deep inside other things.
## In a real IT environment, you rarely get a simple dictionary. You get a List of Dictionaries that contain other Lists.

### 🕸️ The "Deep Audit" Challenge (Nested Data)
## Imagine you are auditing a Cloud Network. Each "Site" has a list of "Servers," and each server has its own data. 
# Calculate the exact cpu??
## This is exactly how data from a Website API or an AI would look.

# Python (The Data to be used)
# network_sites = [
#     {
#         "site_name": "Toronto",
#         "servers": [
#             {"name": "App-01", "cpu": 40},
#             {"name": "App-02", "cpu": "HIGH"} # ValueError Trap
#         ]
#     },
#     {
#         "site_name": "New York",
#         "servers": [{"name": "App-01", "cpu": 50}] # This site is empty!
#     },
#     {
#         "site_name": "London"
#         # The "servers" key is MISSING entirely! (KeyError Trap)
#     }
# ]

#----------------------------
# This below was my 1st work, where i missed to prioritise and work with the list of servers first before moving into the data inside the server list
# total_cpu=0
# for site in network_sites:
#     print(f"Site: {site['site_name']}") # Each dictionary is now known as 'site', and we use the keys to get the value

#     for server in site['servers']:
#         try:
#            # checks if key works
#            raw_cpu= server['cpu']
#            # checks if value works
#            usable_cpu= int(raw_cpu)
#            # checks ???
#            total_cpu += usable_cpu
#            print(total_cpu)

#         except KeyError:
#             print(f"Key-Error: this Server {server['name']} does Not have Key to work with")
        
#         except ValueError:
#             print(f"Value-Error: this server {server['name']} does Not have integer Value (might be string/text)")

# print(total_cpu)

# Result (Basically Error)=  for server in site['servers']:
#                             ~~~~^^^^^^^^^^^
#                            KeyError: 'servers'

### Corrections
## You fell right into the trap! But don't worry, it's a very common scope mistake when dealing with nested loops and exception handling.

# The Core Issue
# Your code will crash with an unhandled KeyError: 'servers' when it reaches London.
# Here is exactly why:
# Your try...except block is located inside the for server in site['servers']: loop.
# When the code hits London, Python evaluates site['servers'] to try and start the loop.
# Because London is missing the "servers" key entirely, Python throws a KeyError before it can ever step inside the loop where your exception handler is waiting.
# Your current except KeyError: block is set up to catch a missing key inside a server dictionary (like if a server was missing the "cpu" or "name" key), but it can't protect against a missing key at the site level.

## The Solutions
## There are 3 clean ways to fix this.

## Option 1: The Pythonic Way (.get())
## The most elegant way to handle this in Python is using the .get() method. 
# It allows you to provide a fallback default value (like an empty list []) if the key doesn't exist.
# This prevents the crash entirely without needing a massive nested try block.

# total_cpu = 0
# for site in network_sites:
#     print(f"Site: {site['site_name']}") 

#     # .get('servers', []) returns an empty list if 'servers' is missing,
#     # safely skipping the loop for London!
#     for server in site.get('servers', []):
#         try:
#            raw_cpu = server['cpu']
#            usable_cpu = int(raw_cpu)
#            total_cpu += usable_cpu
#            print(f"Running Total: {total_cpu}")

#         except KeyError:
#             print(f"Key-Error: A server is missing the 'cpu' key.")
        
#         except ValueError:
#             print(f"Value-Error: This server ({server.get('name')}) does not have an integer CPU value.")

# print(f"Final Total CPU: {total_cpu}")

# Result = Site: Toronto
#          Running Total: 40
#          Value-Error: This server (App-02) does not have an integer CPU value.
#          Site: New York
#          Running Total: 90
#          Site: London
#          Final Total CPU: 90
#-------

## Option 2: An Explicit if Check
## If you want to explicitly log when a site is missing its servers list altogether, 
# you can check for the key before entering the loop:

# total_cpu = 0
# for site in network_sites:
#     print(f"Site: {site['site_name']}") 

#     # Check if the key exists at the site level first
#     if 'servers' not in site: # OR if not server_list: (BUT have to create: "server_list = site["servers"] " in the above line)
#         print(f"Warning: {site['site_name']} has no servers key configuration!")
#         continue ### This "continue" is very important, Skip to the next site/ goes back to the top "for site in network_sites" and starts over with the next site

#     for server in site['servers']:
#         try:
#            raw_cpu = server['cpu']
#            usable_cpu = int(raw_cpu)
#            total_cpu += usable_cpu
#            print(f"Running Total: {total_cpu}")

#         except KeyError:
#             print(f"Key-Error: A server is missing the 'cpu' key.")
        
#         except ValueError:
#             print(f"Value-Error: This server ({server.get('name')}) does not have an integer CPU value.")

# print(f"Final Total CPU: {total_cpu}")

# Result = Site: Toronto
#          Running Total: 40
#          Value-Error: This server (App-02) does not have an integer CPU value.
#          Site: New York
#          Running Total: 90
#          Site: London
#          Warning: London has no servers key configuration!
#          Final Total CPU: 90

# 💡 A Quick Bonus Note
# Inside your except ValueError: block, you wrote server['name']. If a server dictionary was completely broken and missing all keys,
#  server['name'] would throw another unhandled KeyError right inside your error handler. 
# Using server.get('name', 'Unknown') inside your print statement keeps your error handling bulletproof!
#-------------------

## Option 3:
# for site in network_sites:

#     print(f"--- Checking Site: {site['site_name']} ---")
#     total_cpu = 0

#     try:
#         # STEP 1: Get the server list
#         server_list = site["servers"]

#         for server in server_list:
#             try:
#                 # STEP 2: Add up the CPU
#                 total_cpu += int(server["cpu"])
#             except ValueError:
#                 print(f"  ⚠️ Skipping {server['name']}: CPU data is text.")
#         print(f"Total Site Load: {total_cpu}%")

#     except KeyError:
#         print("  ❌ Error: No 'servers' list found for this site.")

#     print("\n") # Just adds a space between sites

# Result = --- Checking Site: Toronto ---
#        ⚠️ Skipping App-02: CPU data is text.
#        Total Site Load: 40%

#          --- Checking Site: New York ---
#          Total Site Load: 50%

#          --- Checking Site: London ---
#          ❌ Error: No 'servers' list found for this site.


## By moving the try...except KeyError: block outside of the "for server in server_list:" loop, 
# you successfully wrapped the access to site["servers"] in a safety net.

# Why this works:
## Scope: When Python attempts server_list = site["servers"] for "London," it triggers a KeyError.
#  Because this line is inside the first try block, the exception is immediately caught by the except KeyError block, 
# skipping the loop entirely and preventing the program from crashing.

## Granularity: You have "nested" your error handling—one block to handle the Structure of the data (the site-level KeyError) and a second,
#  inner block to handle the Integrity of the data (the server-level ValueError). 
# This is considered a best practice in robust programming.

## A few small things to note:
## Variable Reset: You placed total_cpu = 0 inside your site loop. This is correct for your logic! 
# It means you are calculating the "Total Site Load" for each site individually. 
# If you wanted a Global total for all sites combined, you would need to initialize total_cpu = 0 before the for site in network_sites: loop starts.

## Robustness: In your inner except ValueError, you use s['name']. If a server dictionary was missing the name key (e.g., {"cpu": 50}),
#  your error handler itself would trigger a KeyError. Using s.get('name', 'Unknown Server') would make it even safer.

# Overall, your revised logic is solid and is the industry-standard way to handle "dirty" data.
#-------------------------------------------------------------------------------

## Let's push it to the next level. This time, we are simulating a data pipeline for an AI Customer Service Agent.
# When building AI Agents or Websites, you will constantly receive data from APIs formatted as deeply nested blocks. 
# If a single customer record has broken data, you don't want the AI to crash and drop the whole chat queue—you want it to skip the bad data, 
# report the issue, and keep helping others.

### 🕵️ The Scenario: The AI Chatbot Database AuditYou are processing a batch of user support logs. 
# You need to calculate the Average Rating a user gave to the AI across all their chats.
# The Traps in the Data:
# User 101: Perfect data.
# User 102: Completely missing the "chats" history list (KeyError).
# User 103: Has a chat list, but the rating is listed as "Five Stars" instead of a number (ValueError).
# User 104: Has a chat history list, but it is empty []. If you try to calculate the average by dividing by 0 total chats, 
# it will explode (ZeroDivisionError).

# ✏️ Your ChallengeCopy this messy dataset into VS Code. Your goal is to write a script containing an outer loop (for users) 
# and an inner loop (for their chats) with proper try/except safety blocks to handle all 4 users seamlessly.

user_logs = [
    {
        "user_id": "User-101",
        "chats": [{"session": "A", "rating": 5}, {"session": "B", "rating": 4}]
    },
    {
        "user_id": "User-102",
        "status": "Inactive" # Missing 'chats' key entirely!
    },
    {
        "user_id": "User-103",
        "chats": [{"session": "C", "rating": "Five Stars"}] # Bad data format!
    },
    {
        "user_id": "User-104",
        "chats": [] # Empty list! Will cause division by zero later.
    }
]

#-----------1st try the wrong one---------------------
# for user in user_logs:
#     print (f"--- {user.get('user_id', 'User-id Not found')}-------")
#     try:
#         # representing the chats into chats_list
#         chats_list = user.get('chats', 'Missing Chats_list') 
#         #this above didn't work because, Remember that .get() is a safety valve. If the 'chats' key is missing (like in User-102), .get() doesn't throw an error; it gently hands back the string 'Missing Chats_list'.
#         #Because no error is thrown, Python never jumps to your except KeyError: block at the bottom! Instead, it moves straight to the inner loop and tries to treat that string as a list.
#         ## To Fix it: If you want to use a try/except KeyError block, you must look up the key normally (using square brackets []) so Python actually throws the error ticket:
#         ## chats_list = user['chats'] # This will force Python to jump down to the KeyError block!
#         print (f"{chats_list}")
#         #the program will execute the loop 18 times (once for each character). In each turn, the variable "chat" will represent exactly one character.
#         for chat in chats_list:
#             try:
#                 rating_numb = chat['rating']
#                 int_rating = int(rating_numb)
#                 ## and did not do anything(like addition,multiplication or division) with this inner try(rating_numb & int_rating)

#             except KeyError:
#                 print(f"This session: {chat.get('session', 'key-Error')} Has NO key-rating")
#             except ValueError:
#                 print(f" This session:{chat.get('session', 'Value-Error')} Has No Values with Number, it's with text/string")
#         average_rating = total_rating / total_chats
#         print(f"successful: the average rating is: {average_rating}")
#     except KeyError:
#         print ("There was No Chats list found in this user-profile")
#-------------------------------------------
#-------------------------------------


for user in user_logs:
    
    # if this NEXT line is used, since it uses ".get(inthis side under quotation'' it states 1st choice, 2nd choice comes under quotation'' and if the 1st choice is not available)"
    #print(f"----------{user.get('user_id','NO USER ID FOUND')}-----")
    # if this NEXT line is used, since it's NOT ".get" which states "get me this, but if u can't find it say/reply this", SO if it finds the value of "use_id" good but if NOT it's going to need an "Error reply/response"
    print(f"----------{user['user_id']}-----") 
    
    try:
        #assing all the chats-key's multiple values/dictioneries into a single variable so as to use this variable and iteriet(to go over it one by one) which to use it in for-loop
        # if this NEXT line is used, since it's NOT ".get" which states "get me this, but if u can't find it say/reply this", SO if it finds the value of "chats" good but if NOT it's going to need an ""Error" reply/response which also requires a "try" to be complete" 
        chat_lists = user['chats']
        print(f"{chat_lists}")
        
        try:
            # this next line is going to go over each item/chats in chat_lists and represent eachthe variable 
            for chats in chat_lists:
        except
    except KeyError:
        print(f"Key-Error Found: There is NO ANY user-chat key")