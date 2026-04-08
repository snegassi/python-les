
# okay just a question is there other ticket that python knows besides KeyError and ValueError ?

# Gemini said
# Oh, absolutely! Python has a whole "filing cabinet" of different tickets (called Built-in Exceptions). In IT and AI development, you’ll usually run into about 5 or 6 "usual suspects."

# Think of these as the different departments in an IT Help Desk.

# 🏢 The "Common Tickets" Catalog
# Ticket Name	When Python issues it	Real-World IT Example
# TypeError	You tried to do something to a data type that isn't allowed.	Trying to add a number to a string: 5 + "10"
# IndexError	You tried to access a list item that doesn't exist.	Asking for the 10th server in a list of only 3.
# ZeroDivisionError	You tried to divide a number by 0.	Calculating uptime when "Total Days" is 0.
# FileNotFoundError	You tried to open a file that isn't there.	Your script tries to read config.txt but it's missing.
# AttributeError	You tried to use a feature/function that doesn't exist for that object.	Trying to "Uppercase" an Integer (you can only uppercase strings).
# ----------------------------------------------------------
# 🛠️ How to "Catch" All of Them
# In your AI Agent or Website code, you can list as many as you want!

# Try this in VS Code:

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
# 💡 The "Master Key": Exception as e
# Notice the last one: except Exception as e:.

# Exception is the "Grandparent" of all tickets. It catches any error that you didn't specifically name above it.
# as e saves the specific error message into a variable called e so you can print it out and see exactly what happened.

# ❓ Check-in
# If you tried to run print(10 / 0), which ticket from the table above would Python create?
# Does it make sense why we don't just use except Exception for everything? (Hint: It’s because we want to give the user a helpful specific message like "Check your Wi-Fi" vs. just saying "Something broke").
# Once you feel comfortable with the "Ticket Names," we are officially ready for Option B: Libraries! Should we start with the os library to manage your PC files, or a "Web" library?
# --------------------------------------------------------------------------------------

# You said
# lets work on all of this make them more relalistic problems and test me ?

# Gemini said
# This is the "Final Exam" for your Logic & Error Handling phase. To make this realistic for an IT Support Analyst transitioning into AI,
#  I’ve built a scenario that mimics a real automation script you might write to audit a fleet of servers.

# 🏢 The Scenario: The "AI-Ready" Inventory Audit
# You are writing a script that prepares server data for an AI agent. 
# The AI needs the RAM value as an integer to calculate performance.

# The Problems in the Data:

# Srv-01: Perfect data.
# Srv-02: The "ram_gb" key is missing (KeyError).
# Srv-03: The RAM is listed as "16GB" (a string with letters), so int() will fail (ValueError).
# Srv-04: The RAM is listed as 0 (Zero), which will break your "Usage Ratio" math (ZeroDivisionError).

# ✏️ The Challenge
# Copy this data into VS Code and fill in the try/except blocks to handle all four servers without the script crashing.
# Python
# servers = [
#     {"id": "Srv-01", "ram_gb": 32, "used_gb": 16},
#     {"id": "Srv-02", "status": "Online"}, 
#     {"id": "Srv-03", "ram_gb": "16GB", "used_gb": 8},
#     {"id": "Srv-04", "ram_gb": 0, "used_gb": 0}
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
#     except KeyError:
#         return "❌ Error: Missing RAM data."
    
#     # 1. Add an except for when the value isn't a clean number
#     # 2. Add an except for when the RAM is 0
#     # 3. Add a "Catch-All" for anything else unexpected

# for s in servers:
#     # Use .get() here for the ID just in case the 'id' key is missing too!
#     name = s.get("id", "Unknown Server")
#     result = audit_server(s)
#     print(f"{name}: {result}")
# 🧪 Technical Questions (Test your Knowledge)
# Before you run the code, try to answer these based on our "Ticket System" discussion:

# Srv-03 has ram_gb: "16GB". Which "Ticket" will Python create when it tries to run int("16GB")?
# In Srv-04, the RAM is 0. Which specific "Ticket" prevents the math from working?
# Why did we put ram = s["ram_gb"] inside the try block instead of outside?
# If you add a 5th server: {"id": "Srv-05", "ram_gb": 64, "used_gb": "NONE"}, which error will trigger when it tries to do the math? (Hint: Look at the Common Tickets table from our last chat).


servers = [
    {"id": "Srv-01", "ram_gb": 32, "used_gb": 16},
    {"id": "Srv-02", "status": "Online"}, 
    {"id": "Srv-03", "ram_gb": "16GB", "used_gb": 8},
    {"id": "Srv-04", "ram_gb": 0, "used_gb": 0}
]

def checking_server(s):
    try:
        # Step-1: Get the value, using server and key AND in way checking the key ? if its available hence if not keyError
        ram=s["ram_gb"] 
    
        # Step-2: Change the value to usable value,On the way while checking if it produces Value or Not, Hence ValueError
        ram_int = int(ram) 

        # STEP 3: Calculate usage % (used / total)
        ratio = s["used_gb"] / ram_int

    # Now Errors
    
    except KeyError:
        return "Key Error, or key not available"
    except ValueError:
        return "Value is not available or mixed up with letters"
    except ZeroDivisionError:
        return " Can't divide a number(used_gb) to zero(ram_int)"
    except Exception as e:
        return " this issue is weird {e}"

for s in servers:
    # Using .get("id","unknown") get the key name, if not to know that its Unknown
    name = s.get("id", "Unknown")
    result = checking_server(s)
    print(f"{name}: {result}")