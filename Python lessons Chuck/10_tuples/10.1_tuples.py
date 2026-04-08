

"""
Think of Tuples and Sets as the specialized cousins of the List. 
While a List is like a flexible "do-anything" bucket, 
Tuples and Sets are designed for very specific jobs.

1.The Tuple: The "Locked" ListA Tuple is exactly like a list, but with one major rule:
You cannot change it. Once you create it, you can't add, remove, or sort it.

 It is "immutable."Syntax: Uses parentheses ( ) instead of square brackets [ ].

 Empty: tup = tuple() or tup = ()When to use a Tuple?
 Constants: When you have data that should never change 
 (like the coordinates of a city or the days of the week).

 Speed: Because they are locked, Python processes tuples faster than lists.
 Dictionary Keys: Since they can't change, you can actually use a tuple as a key in a dictionary
(you can't do that with a list!).

2. The Set: The "Unique" CollectionA Set is a collection that is unordered and only allows unique items. 
If you try to add the same thing twice,the set simply ignores the second one.
Syntax: Uses curly braces { } (just like a dictionary, 
 but with no colons).Empty: MUST use s = set(). 
 (Using {} creates an empty dictionary!)When to use a Set?

 Removing Duplicates: If you have a list of 1,000 emails and you only want the unique ones, 
 just do set(my_list).
 Membership Testing: If you need to check "Is this word in my massive collection?",
a set is nearly instant, whereas a list has to check every single item one by one.

#my_tup = (1, 2, 3)
empty_tup = ()

# Sets
my_set = {1, 2, 3}
empty_set = set() # Remember: {} is a dictionary!

"""

name = input("Enter file:")
"""
If you type mbox-short.txt as input, it uses that file.
If you are tired of typing and just hit Enter (leaving the input empty), 
the length of the string name is 0.Since $0 < 1$, 
the if statement triggers and automatically fills in "mbox-short.txt" for you.
"""
if len(name) < 1: name = "mbox-short.txt" # Shortcut for testing
handle = open(name)

counts = dict()

# STAGE 1 & 2: Filter and Tally
for line in handle:
    if not line.startswith("From "): 
        continue
    
    # Get the time string (e.g., '09:14:16')
    words = line.split()
    time = words[5]
    
    # "Split the split" to get the hour
    # '09:14:16' becomes ['09', '14', '16']
    hour_parts = time.split(':')
    hour = hour_parts[0]
    
    # Update the dictionary tally
    counts[hour] = counts.get(hour, 0) + 1

# STAGE 3: Sort using Tuples
# We create a list to hold the tuples so we can use .sort()
lst = list()
for key, val in counts.items():
    new_tup = (key, val) # Packaging into a "locked" tuple
    lst.append(new_tup)

lst.sort() # Sorts by the first item (the hour)

# STAGE 4: Print
for key, val in lst:
    print(key, val)