
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

### 🚀 Step 5.3: The "List of Dictionaries" (Real Data)
### In IT Support, you never have just one ticket. You have a List of tickets. 
### This is where your two skills (Lists + Dictionaries) merge. 
# And to access the dictionary one by one from the list we use For-loop. Moreover, the list with dictionary insdie it is now the Raw Data.

# Python
# # A List of Dictionaries, where the list with dictionary insdie it is now the Raw Data.
# all_tickets = [
#     {"id": 101, "issue": "Blue Screen", "status": "Open"},
#     {"id": 102, "issue": "Password Reset", "status": "Closed"},
#     {"id": 103, "issue": "No Internet", "status": "Open"}
# ]

# # 1. Access the first ticket's issue
# print(f"Ticket 1 Issue: {all_tickets[0]['issue']}")

# # 2. Loop through them(the list one by one for the dictionaries)!
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

# the list with dictionary insdie it is now the "Raw Data".
# laptops = [
#     {"id": "L01", "os": "Windows 11"},
#     {"id": "L02", "os": "Windows 10"},
#     {"id": "L03", "os": "Windows 11"}
# ]

# for laptop in laptops:
#     if laptop['os'] != "Windows 11":
#         print(f"🚨 OS Upgrade needed for Laptop: {laptop['id']}")

# Result = 🚨 OS Upgrade needed for Laptop: L02
#------------------------------

## In IT, we rarely check just one thing. Usually, it’s a combination: "Is the OS old "AND" is the RAM too low?"
## To do this, we use the "and" keyword. This acts like a double-lock on a door—both conditions must be True for the code inside to run.

## ✏️ Exercise 5.4: The "Hardware Refresh" Audit
# Your company is upgrading. You only want to replace laptops that are both running an old OS and have low RAM.

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
# The Logic: Only Laptops 01 and 04 should match both rules. (Laptop 03 has Windows 10, but its RAM is 16, so it's "safe" for now).
# The Brackets: Remember that device is your temporary name for the dictionary you are currently holding.
# How many laptops ended up in your to_replace list? Once you run this, you're doing exactly what a System Administrator does to generate a budget report!

# the list with dictionary insdie it is now the "Raw Data".
# inventory=[
#  {"id": "L01", "os": "Windows 10", "ram": 8},
#  {"id": "L02", "os": "Windows 11", "ram": 8},
#  {"id": "L03", "os": "Windows 10", "ram": 16},
#  {"id": "L04", "os": "Windows 10", "ram": 4}
# ]

# to_replace = []

# for device in inventory:
# #    if device['os'] == "Windows 10" and device['ram'] < 16: # (Using "and" is Simple way, since "and" is very strict when matching,for clarification read below at the Fix)
#     if "Windows 10" in device['os'] and device['ram'] < 16: # (Using "in" is Best way, since it considers even if there's a small typo or extra space, for clarification read below at the Fix)
#         print(f"⚠️ High Priority Replace: {device['id']}")
#         to_replace.append(device["id"]) ## Since THE Print is Inside the For-loop. It prints one at a time for each device to_replace it finds.
#         print(f"{to_replace}")

# print(f"Total laptops to order: {len(to_replace)}") ### Since the print is Outside the for- loop/ If. It prints the Count (len) of Final Result of to_replace in the End "Once". 
# print(f"The Laptops tha need to replaced = {to_replace}") ### Since the print is Outside the for- loop/ If. It prints the Final Result of to_replace in the End "Once".

# Result = ⚠️ High Priority Replace: L01
#          ['L01']
#          ⚠️ High Priority Replace: L04
#          ['L01', 'L04'] # these 4 above results are from the inside-loop, where they were produced in pair in every single loop.
#          Total laptops to order: 2 # this result is "final/commulative one" frm the Outside-loop fr Counting the PCs
#          The Laptops tha need to replaced = ['L01', 'L04'] # this result is "final/commulative one" frm the Outside-loop fr listing/printing the PCs

####This is a classic "IT Support" moment! Your logic is perfect, but you’ve been hit by a String Mismatch.
### In Python, a string must be a 100% exact match, including every single letter. Look very closely at these two lines:

# Your Data: {"os": "Windows 10" ...} (with an s)
# Your If Statement: if device["os"] == "Window 10" (without the s)

# Because "Window 10" is not the same as "Windows 10," the computer says, 
# "Nope, that's not a match!" and skips over the code inside your if statement. 
# This is why your to_replace list is coming back empty.

### 🛠️ The Fix
# Change "Window 10" to "Windows 10" in your if statement:

# Python
# if device["os"] == "Windows 10" and device["ram"] < 16:

#### 💡 Why This Happens (and how to avoid it)
# In professional IT scripts, we often use the ".lower()"" method or the "in" keyword to prevent these tiny "typo" bugs from breaking our audits.

# Try this "Bulletproof" Version in VS Code:

# Python
### Using 'in' is safer than '==' because it catches "Windows 10" 
## even if there's a small typo or extra space. So ### Using "if" with "in"
# if "Windows 10" in device["os"] and device["ram"] < 16:
#--------------------------------------

## 😈 Step 5.5: The "Tricky" Audit (The Nested Logic Trap)
# Ready for a challenge? This one uses "or" and "not".

# "or" means if EITHER thing is true, the door opens.
# "not" flips the answer (True becomes False).

# The Scenario: You are managing a server room. 
# You need to flag any server that is either overheating OR has a status that is NOT "Active".

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

# ❓ Check-in
# Does it make sense that or is "friendlier" than and? (It only needs one thing to be true to trigger the code).
# Do you see why S4 gets flagged twice as hard, but still only needs to be caught once?

# servers =[
#    {"id": "S1", "temp": 80, "status": "Active"}, #(80 is fine)
#    {"id": "S2", "temp": 110, "status": "Active"}, # (Too hot!)
#    {"id": "S3", "temp": 75, "status": "Maintenance"},# (Not Active!)
#    {"id": "S4", "temp": 120, "status": "Offline"},
# ]

# for server in servers:
#     if server['temp'] > 100 or server['status'] != "Active":  # != "Active" equals == "Not Active"/ Not Active
#         print(f"{server['id']=} has problems with either Overheating:{server['temp']=} or Not Active:{server['status']=}")
#         #print(f"{server['id']} has problems with either Overheating:{server['temp']} or Not Active:{server['status']}") # I like this better since it describs the issue in which human can understand

# Result = server['id']='S2' has problems with either Overheating:server['temp']=110 or Not Active:server['status']='Active'
#          server['id']='S3' has problems with either Overheating:server['temp']=75 or Not Active:server['status']='Maintenance'
#          server['id']='S4' has problems with either Overheating:server['temp']=120 or Not Active:server['status']='Offline'
#----------------------------

####💡 A "Master" Level Trick: The "In" List
# Since you are an IT Support Analyst, you will often have more than one "bad" status. 
# For example, what if you wanted to flag "Maintenance", "Offline", and "Error"?

## Instead of writing a very long if statement with five ors, you can check if a value is in a "Bad List."

# Try reading this snippet (just to see the logic):

# Python
### bad_statuses = ["Maintenance", "Offline", "Error", "Decommissioned"]
### Using "if" with "in"
# if s['status'] in bad_statuses:
#     print("Found a problematic status!")
# This keeps your code clean and easy to update. If a new "bad" status is added next year, 
# you just add it to the bad_statuses list at the top!

### ???? Can you show me with real example???
# Since you are an IT Support Analyst with experience in Tier 1 and Tier 2 support, 
# let's look at a "Boss Level" real-world example: The Automated Onboarding Audit.
# Imagine a new batch of employees just started. Some are in IT and need high-power laptops, and some are in Sales and just need a standard setup. 
# You need to find any "Mismatches" where an employee has the wrong equipment.

## ✏️ Boss Level Exercise: The Onboarding Audit
# In this scenario, we are looking for Error Cases. A "Mismatch" happens if:

# The user is in "IT" but has less than 16 GB of RAM.
# -- OR --
# The user is in "Sales" but has a "MacBook" (your company policy only allows Windows for Sales).

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
# The elif: This stands for "Else If." It allows you to check a different rule if the first one wasn't met. 
# It keeps your code from checking "Sales" rules for "IT" people.

# Data Integrity: This script would save you hours of manual spreadsheet checking.

# employees = [
#      {"name": "Alice", "dept": "IT", "ram": 32, "device": "MacBook"},   # OK
#      {"name": "Bob", "dept": "IT", "ram": 8, "device": "Windows"},     # ERROR (Low RAM for IT)
#      {"name": "Charlie", "dept": "Sales", "ram": 16, "device": "MacBook"}, # ERROR (Mac for Sales)
#      {"name": "David", "dept": "Sales", "ram": 8, "device": "Windows"} # OK
#  ]

# flagged_users = []
# for person in employees:
#     if person["dept"] == "IT" and person["ram"] < 16:
#         print(f"⚠️ {person['name']} (IT) needs a RAM upgrade!")
#         flagged_users.append(person["name"])

#     elif person["dept"] == 'Sales' and person['device'] == "MacBook":
#         print(f"⚠️ {person['name']} (Sales) has unauthorized hardware!")
#         flagged_users.append(person["name"])
# print(f"{flagged_users=}")

# Result = ⚠️ Bob (IT) needs a RAM upgrade!
#          ⚠️ Charlie (Sales) has unauthorized hardware!
#          flagged_users=['Bob', 'Charlie']

### You’ve officially reached "Power User" status. 
# That script is a perfect example of how an IT professional uses Python to solve business problems.

# By using if and elif together, you created a Decision Tree. 
# The computer looked at Alice, saw she was in IT but had enough RAM, 
# then skipped the Sales check entirely because the elif told it: "Only check this if the first rule didn't apply."

### 🔍 Why This Code is Great
## Efficiency: You used e['name'] to keep your flagged_users list clean—it's just a list of strings now, 
# which is easy to read.

## Accuracy: It correctly ignored David (who is Sales with Windows) and Alice (who is IT with 32GB).

## Scalability: You could have 10,000 employees in that list, and your script would find Bob and Charlie in less than a second.
#------------------------------------------------------------------------

### As an IT Support Analyst, you often deal with "Status" messages or "Department" names that can vary. 
# Instead of writing a long, messy if statement with 50 ors, we use a List as a Filter.

# 🔍 The "In" List: How it Works
# Think of it like a VIP Guest List at a club. Instead of the bouncer asking, 
# "Are you Alice? Or are you Bob? Or are you Charlie?", the bouncer just holds a list and checks if your name is in it.

# 💻 Real-World Example: The "Bad Software" Audit
# Imagine your company has banned certain apps for security reasons (like "Torrent", "Keylogger", or "Unapproved_VPN").

## Without the "In" List (The messy way):
# if app == "Torrent" or app == "Keylogger" or app == "Unapproved_VPN":
#     print("🚨 Security Alert!")

## With the "In" List (The Master way):
# banned_apps = ["Torrent", "Keylogger", "Unapproved_VPN", "TikTok", "MineCraft"]

# current_app = "TikTok"
### Using "if" with "in"
# if current_app in banned_apps:
#     print(f"🚨 Security Alert: {current_app} is not allowed on company hardware!")
#------------------------------

# ✏️ Exercise 5.6: The "Regional Support" Filter
# You are routing support tickets. Tickets from "London", "Paris", and "Berlin" need to be sent to the EMEA Team.

# Create a list: emea_cities = ["London", "Paris", "Berlin"].
# Create a dictionary for a new ticket:
# ticket = {"id": 505, "city": "Paris"}.
# The Logic:
# IF the ticket["city"] is in emea_cities:
# Print: "Routing to EMEA Support Team..."
# ELSE:
# Print: "Routing to Global Support Team..."

# ❓ Check-in (Before we move an inch!)
# In that exercise, if you changed the city to "Toronto", which message would print?

# Can you see how easy it is to add a new city (like "Madrid") just by typing it into the emea_cities list, 
# without touching your if statement?

# emea_cities = ["London", "Paris", "Berlin"]
# # New ticket
# ticket = {"id": 505, "city": "Paris"}
# #logic
# if ticket["city"] in emea_cities:
#     print("Routing to EMEA Support Team...")
# else:
#     print("Routing to Global Support Team...")

# Result = Routing to EMEA Support Team...
#-----------------------------------

### let’s turn up the heat. In IT, data is rarely "clean." 
# You might have a list of servers where some have missing information, or a mix of "Critical" and "Warning" alerts.

# To solve this, we are going to combine Lists of Dictionaries, the "In" List trick, and Complex Logic.

## ✏️ Boss Level Exercise 5.7: The "Security Firewall" Audit
# The Scenario: You are auditing a network. You have a list of "Dangerous Protocols" that should never be open on a public-facing server.

# Your Rules:
# Dangerous Protocols: ["Telnet", "FTP", "HTTP"] (These are unencrypted).
# The Flag: A server is a "Critical Security Risk" if:
# Its protocol is in the dangerous_protocols list.
# -- AND --
# Its visibility is "Public".

# The Data:
# network_inventory = [
#     {"id": "Srv-01", "protocol": "HTTPS", "visibility": "Public"},
#     {"id": "Srv-02", "protocol": "Telnet", "visibility": "Public"},
#     {"id": "Srv-03", "protocol": "FTP", "visibility": "Private"},
#     {"id": "Srv-04", "protocol": "HTTP", "visibility": "Public"}
# ]

# dangerous_protocols = ["Telnet", "FTP", "HTTP"]

# The Task: Loop through network_inventory.
# The Logic: Use an if statement to find the servers that match both rules (In the dangerous list AND Public).
# The Action: Print a warning for the dangerous servers: f"🚨 SECURITY BREACH: {server['id']} is exposing {server['protocol']} to the Public!"

# ❓ Tricky Questions (Think before you code!):
# Server Srv-03 has "FTP" (which is dangerous). Will your code flag it? (Look at its visibility!)
# Server Srv-01 is "Public". Will your code flag it? (Look at its protocol!)

network_inventory = [
     {"id": "Srv-01", "protocol": "HTTPS", "visibility": "Public"},
     {"id": "Srv-02", "protocol": "Telnet", "visibility": "Public"},
     {"id": "Srv-03", "protocol": "FTP", "visibility": "Private"},
     {"id": "Srv-04", "protocol": "HTTP", "visibility": "Public"}
]

dangerous_protocols = ["Telnet", "FTP", "HTTP"]

for server in network_inventory:
    if server['protocol'] in dangerous_protocols and server['visibility'] == "Public":
        print(f"🚨 SECURITY BREACH: {server['id']} is exposing {server['protocol']} to the Public!")

# Result = 🚨 SECURITY BREACH: Srv-02 is exposing Telnet to the Public!
#          🚨 SECURITY BREACH: Srv-04 is exposing HTTP to the Public!

### 😈 The "Ultimate" Tricky Mix (Self-Correction)
### Sometimes in IT, data is messy. Someone might type "ftp" (lowercase) or "FTP " (with a space).

# Try this "Stress Test" in VS Code:
# Change Srv-03 in your list to: {"id": "Srv-03", "protocol": "ftp", "visibility": "Public"} (Make it lowercase and Public).
# Run your code again.

# Wait... did Srv-03 get flagged?
# If your dangerous_protocols list has "FTP" (uppercase), Python will see "ftp" (lowercase) and think they are different!

# The Trick:
# To fix this, professional IT Analysts use ".upper()" to force the data to match their list.

# Python
#      if server['protocol'].upper() in dangerous_protocols and server['visibility'] == 'Public':

# ❓ Final Check-in on Logic
# Does it make sense why Srv-03 (the lowercase one) would be "invisible" to your audit without that .upper() trick?
# Do you feel like you have the "hang" of checking multiple conditions at once now?

