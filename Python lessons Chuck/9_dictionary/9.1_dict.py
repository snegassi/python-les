
"""
Write a program to read through the mbox-short.txt and figure out 
who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.


"""
name= input("Enter the file:")
handle= open(name)

start = list() # 1. The List for collecting
sender = dict() # 2. The Dictionary for counting

# --- STEP 1: COLLECT (The File Loop) ---
for line in handle:
    if not line.startswith("From "):  # promt is specifically stating to look for "From " (for "from " with some space that's the key)and Not "From:"
        continue
    if len(line) < 3: # This line is Optional since we have the 1st "if "is already a very strong "Gatekeeper"—it won't let short lines through anyway!
        continue
    words = line.split() # Puting the split words in to a list called "words"
    email = words[1]
    start.append(email) # Just building the list of the second indexed word called email here in dictionary called "start" 
    # NO DICTIONARY WORK YET!

# --- STEP 2: COUNT (The Dictionary Loop) ---
# This starts only AFTER the file loop is totally finished
for word in start:
    sender[word] = sender.get(word, 0) + 1

#------step 3:The Winner (The "Max" Loop)----
bigword = None
bigcount = None    

for word, count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
""" for the step 1 and 2, Your logic was almost there, but the nested loop (the loop inside the loop) 
caused it to re-count the entire list over and over again. By simply moving the dictionary part out of the file loop,
 your "List First" method would work perfectly!    
 """
"""
Why the "Pro" way skips the listYou mentioned: "I was collecting into a list... then saving to sender while counting."Programmers usually skip the list because the Dictionary can do both jobs at once. A dictionary is like a list that can count.Instead of:Line $\rightarrow$ ListList $\rightarrow$ DictionaryWe just do:Line $\rightarrow$ DictionaryPythonfor line in handle:

 line in handle:

# --- STAGE 1: (collecting and counting) ---
for line in handle:
    if not line.startswith("From "): continue
    email = line.split()[1]
    sender[email] = sender.get(email, 0) + 1

    This does exactly what you wanted: 
    # It saves the item AS a key and updates the count AS the value.
    sender[email] = sender.get(email, 0) + 1

# --- STAGE 2: Finding the Maximum ---
# Notice: These lines are NOT indented. They wait for Stage 1 to finish!
bigword = None
bigcount = None    

for word, count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
"""

"""
Summary of your "Programming Journey" on this task:
The Filter: You learned to use startswith("From ") to ignore the junk.

The Extraction: You used split() and [1] to grab the email.

The Tally: You used sender.get() to count.

The Timing: You now know to un-indent the "Max Loop" so it only runs once at the very end.

You’ve basically just built a mini "Data Analysis" pipeline!
"""