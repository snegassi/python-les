
# 📦 Step 5: Dictionaries (Data with Labels)
# Up until now, we’ve used Lists []. Lists are great for a simple row of items, but in IT Support and AI, 
# we often need to store "Pairs" of information.

# For example, a User isn't just a name; they have an ID, an Email, and a Department. 
# In Python, we use a Dictionary {} to map a "Key" to a "Value."

## 💡 The Anatomy of a Dictionary
## Curly Brackets: { }
## The Key: The label (e.g., "name")
## The Value: The data (e.g., "Gemini"), but if it's number leave it without"" = 16
## The Colon: Separates them ("name": "Gemini")
## Separate the key-value pairs by comma: "name":"Gemini",

# Python
# # --- OUR DATA (The Dictionary) ---
# user_profile = {
#     "username": "IT_Pro_2026",
#     "access_level": "Admin",
#     "login_attempts": 3  # leave z number without ""
# }

# # 1. Accessing data (We use the 'Key' like an index)
# print(f"User is: {user_profile['username']}")

# # 2. Updating data
# user_profile["login_attempts"] = 4
# print(f"Updated attempts: {user_profile['login_attempts']}")

# Result = User is: IT_Pro_2026
#          Updated attempts: 4

#----------------------
## ✏️ Exercise 5.1: The "Server Info" Card
# Let's practice building a "label" for a piece of hardware.

# Create a dictionary called server:
# Set "ip" to "192.168.1.1"
# Set "status" to "Online"
# Set "ram_gb" to 16
# Task 1: Use an F-string to print: "The server at {ip} is currently {status}."
# Task 2 (The Logic Mix): Write an Independent If statement:
# IF server["ram_gb"] is less than 32, print "⚠️ Suggestion: Upgrade RAM for better performance."

# ❓ Check-in
# How does it feel using Curly Brackets {} and Colons : compared to the Square Brackets [] of a list?
# Does the idea of "Keys" (labels) make it easier to understand what the data represents compared to just a list of numbers?
# Paste your code for the "Server Info" card when you're ready!

# server = {
#     "ip" : "192.168.1.1",
#     "status" : "Online",
#     "ram_gb" : 16,
# }

# print(f"The server at {server['ip']} is currently {server["status"]}.")

# if server["ram_gb"] < 32:
#     print(f"⚠️  Suggestion: Upgrade RAM for better performance.")

# Result = The server at 192.168.1.1 is currently Online.
#          ⚠️  Suggestion: Upgrade RAM for better performance.

## One quick technical note: In some versions of Python, putting double quotes inside double quotes (like {server["ip"]}) can sometimes confuse the code editor. 
# If you ever see a red squiggly line there, a common "pro" habit is to use single quotes for the keys inside the f-string, like this:
## print(f"The server at {server['ip']} is currently {server['status']}")
#------------------------

#---------------------------------------
### 🔍 1) How does it feel using Curly Brackets {}?
### Dictionaries are usually the "Aha!" moment for IT professionals. 
### While a "List" is "just a pile of data", a "Dictionary" is a "Database Record".It tells you exactly what every number means.
#-------------------------------------------------------

## 🛠️ Step 5.2: Adding and Deleting from Dictionaries
# In IT Support, systems are dynamic. You might need to add a "Last Boot Time" to a server record or remove a "User" from a database.

## To Add/Update: Just assign a value to a new key.
## To Delete: Use the del keyword.

# Python
# device = {"type": "Laptop", "brand": "Dell"}

# # 1. Add a new piece of info
# device["os"] = "Windows 11"

# # 2. Change an existing piece of info
# device["brand"] = "Alienware"

# # 3. Remove a piece of info
# del device["type"]

# print(f"{device=}")

# Result = device={'brand': 'Alienware', 'os': 'Windows 11'}
#---------------------

## ✏️ Exercise 5.2: The "Troublesit Ticket"
# Let's simulate an IT ticketing system.

# Create a dictionary called ticket:
# "id": 101
# "issue": "Blue Screen"
# "priority": "Low"
# Task 1 (Update): The issue is serious! Change the "priority" from "Low" to "High".
# Task 2 (Add): Add a new key called "assigned_to" and set it to your name.
# Task 3 (Logic Mix): * IF the priority is "High", print: "🚨 URGENT: Ticket {id} ({issue}) is assigned to {assigned_to}!"
# ❓ Check-in
# Does it make sense how we can "grow" a dictionary by just inventing a new key (like assigned_to)?
# Can you see how this would be useful for storing information about 100 different computers in a network?

# ticket = {
#     "id": 101,
#     "issue": "Blue Screen",
#     "priority": "Low",
# }
# # Update
# ticket["priority"] = "High"
# # Add
# ticket['assigned_to'] = "Daniel"
# # logic-mix
# if ticket["priority"] == "High":
#     print(f"🚨 URGENT: Ticket {ticket['id']},({ticket['issue']}) is assigned to {ticket['assigned_to']}!")

# Result = 🚨 URGENT: Ticket 101,(Blue Screen) is assigned to Daniel!
#------------------------

# 🚀 Step 5.3: The "List of Dictionaries" (Real Data)
# In IT Support, you never have just one ticket. You have a List of tickets. 
# This is where your two skills (Lists + Dictionaries) merge.

# Python
# # A List of Dictionaries
# all_tickets = [
#     {"id": 101, "issue": "Blue Screen", "status": "Open"},
#     {"id": 102, "issue": "Password Reset", "status": "Closed"},
#     {"id": 103, "issue": "No Internet", "status": "Open"}
# ]

# # 1. Access the first ticket's issue
# print(f"Ticket 1 Issue: {all_tickets[0]['issue']}")

# # 2. Loop through them!
# for t in all_tickets:
#     if t["status"] == "Open":
#         print(f"⚠️ Action Required: Ticket {t['id']} is still Open!")

# Result = Ticket 1 Issue: Blue Screen
#         ⚠️ Action Required: Ticket 101 is still Open!
#         ⚠️ Action Required: Ticket 103 is still Open!

## ✏️ Exercise 5.3: The "Inventory Audit"
# This is a very common task for an IT Analyst. You have a list of laptops, and you need to find which ones are "Outdated."

# Create a list called laptops:
# Laptop 1: {"id": "L01", "os": "Windows 11"}
# Laptop 2: {"id": "L02", "os": "Windows 10"}
# Laptop 3: {"id": "L03", "os": "Windows 11"}
# The Loop: for laptop in laptops:
# Inside the Loop:
# IF the os is not equal to "Windows 11":
# Print: f"🚨 Upgrade needed for Laptop: {laptop['id']}"
# How many laptops in your list need an upgrade? Once you can loop through a list of dictionaries, you have officially learned the data structure that 90% of the internet is built on (it's called JSON).
# Let me know if you have questions about the "Square Brackets" next to "Square Brackets" [0]['issue'] before you start!
laptops = [
    {"id": "L01", "os": "Windows 11"},
    {"id": "L02", "os": "Windows 10"},
    {"id": "L03", "os": "Windows 11"}
]

for laptop in laptops:
    if laptop['os'] != "Windows 11":
        print(f"🚨 OS Upgrade needed for Laptop: {laptop['id']}")

# Result = 🚨 OS Upgrade needed for Laptop: L02