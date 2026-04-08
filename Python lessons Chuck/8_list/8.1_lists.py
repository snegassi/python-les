

"""
Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check
 to see if the word is already in the list and if not append it to the list. 
 When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
print(line.rstrip())

Desired Output
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 
'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
"""

fname = input("Enter file name: ")
fhand = open(fname)

# 1. Create one empty list to hold all unique words
unique_words = list()

for line in fhand:
    # 2. Split the line into a list of words
    words = line.split()
    
    # 3. Look at each word in that line's list
    for word in words:
        # 4. Check if we already have it
        if word not in unique_words:
            unique_words.append(word)

# 5. Sort the final list once the loops are totally finished
unique_words.sort()

# 6. Print the result
print(unique_words)

"""
Gemini said
You are on the right track by using a nested loop (a loop inside a loop), but your current code has a few "logic knots" that are tangling things up.

The 3 Main Issues to Fix:
The Nested Loop: You are looping through line (which is a string) instead of one_list (which is your list of words).

The continue: Just like before, continue tells Python to skip everything below it. So your append and sort never actually run.

The "Sort" Timing: If you sort the list every time you add a single word, your program becomes very slow. It’s better to build the whole list first and sort it once at the very end.

The "Easiest" Code
Python
fname = input("Enter file name: ")
fhand = open(fname)

# 1. Create one empty list to hold all unique words
unique_words = list()

for line in fhand:
    # 2. Split the line into a list of words
    words = line.split()
    
    # 3. Look at each word in that line's list
    for word in words:
        # 4. Check if we already have it
        if word not in unique_words:
            unique_words.append(word)

# 5. Sort the final list once the loops are totally finished
unique_words.sort()

# 6. Print the result
print(unique_words)
Simple Explanation:
The "Big List" (unique_words): We create this outside the loop so it persists.
 If we created it inside the loop, it would reset every time we moved to a new line.

The "Split" (line.split()): This turns a string like "But soft what light" into a list: ['But', 'soft', 'what', 'light'].

The "Gatekeeper" (if word not in): This is the most important part! It prevents duplicates.
 It asks, "Hey, have I seen 'soft' before?" If the answer is no, it adds it.

The "Sort" (.sort()): Notice this is not indented. 
That means it only runs once the computer is done reading the entire file.
"""