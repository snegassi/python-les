

# what is the .get in server.get('id', 'Unknown') ? have we worked on it?

# Gemini said
# Great catch! We actually haven't officially covered .get() yet—you just spotted a Senior-Level Dictionary Trick.

# In IT, if you try to access a key that doesn't exist (like server["id"]), Python crashes with a KeyError. The .get() method is like a "Safety Valve" built directly into dictionaries.

# 🛡️ What is .get()?
# Instead of forcing the "drawer" open, .get() gently asks: "Is there an 'id' in here? If not, please just give me this default value instead of crashing."

# 🔍 How it Works
# The syntax is: dictionary.get(key, default_value)

# The Key: The name of the data you want (e.g., "id").

# The Default: What to return if the key is missing.

# Compare these two in VS Code:

# The "Dangerous" Way (Crashes if missing):

# Python
# server = {"status": "online"}
# print(server["id"]) # 🚨 CRASH! KeyError
# The "Safe" Way (Never crashes):

# Python
# server = {"status": "online"}

# # It looks for "id". Since it's missing, it prints "Unknown"
# print(server.get("id", "Unknown")) 

# # If the key IS there, it ignores the default!
# server_2 = {"id": "Srv-99"}
# print(server_2.get("id", "Unknown")) # Prints "Srv-99"
# --------------------------------------------
# 🛠️ Why I used it in your Exercise
# Look at Server-03 in your inventory:
# {"id_label": "Srv-03", "usage": "MAX"}

# Notice that the person who made this data accidentally typed "id_label" instead of "id".

# If we used server["id"], the print statement at the very bottom of your loop would crash before showing you the error message!

# By using .get("id", "Unknown"), we ensure the print always works, even if the data is messy.

# ❓ Check-in
# Can you see how .get() is like a "Mini Try/Except" block specifically for dictionaries?

# If you used server.get("usage", 0), what would happen if a server was missing the "usage" key?