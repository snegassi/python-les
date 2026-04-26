
# Gemini said
# I love the persistence. If you want to build AI Agents, you have to be comfortable with the "Messy Middle"—
# where data isn't just missing or wrong, but it’s nested deep inside other things.

# In a real IT environment, you rarely get a simple dictionary. 
# You get a List of Dictionaries that contain other Lists.

# 🕸️ The "Deep Audit" Challenge (Nested Data)
# Imagine you are auditing a Cloud Network. Each "Site" has a list of "Servers," 
# and each server has its own data. This is exactly how data from a Website API or an AI would look.

# The Data:

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
#         "servers": [] # This site is empty!
#     },
#     {
#         "site_name": "London"
#         # The "servers" key is MISSING entirely! (KeyError Trap)
#     }
# ]

#----✏️ The Tricky Exercise
# Write a script that loops through the Sites, then loops through the Servers inside each site, and adds up the Total CPU for that location.

# Your logic needs to handle:
# ** Londres (KeyError):** What if the "servers" key is missing?
# App-02 (ValueError): What if a CPU is a string like "HIGH"?
# New York (IndexError/Logic): What if the list is empty?

#----🛠️ Here is your "Starter Code" (Fill in the blanks)
# Python
# for site in network_sites:
#     print(f"--- Checking Site: {site['site_name']} ---")
#     total_cpu = 0
    
#     try:
#         # STEP 1: Get the server list
#         server_list = site["servers"]
        
#         for s in server_list:
#             try:
#                 # STEP 2: Add up the CPU
#                 total_cpu += int(s["cpu"])
#             except ValueError:
#                 print(f"  ⚠️ Skipping {s['name']}: CPU data is text.")

#         print(f"Total Site Load: {total_cpu}%")

#     except KeyError:
#         print("  ❌ Error: No 'servers' list found for this site.")

#     print("\n") # Just adds a space between sites
# 🕵️ Why is this "Boss Level"?
# Notice there are two try/except blocks.
# The Outer one catches if the "Site" is broken (Missing the whole list).
# The Inner one catches if a "Server" is broken (Bad CPU data).

network_sites = [
    {
        "site_name": "Toronto",
        "servers": [
            {"name": "App-01", "cpu": 40},
            {"name": "App-02", "cpu": "HIGH"} # ValueError Trap
        ]
    },
    {
        "site_name": "New York",
        "servers": [] # This site is empty!
    },
    {
        "site_name": "London"
        # The "servers" key is MISSING entirely! (KeyError Trap)
    }
]

