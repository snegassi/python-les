
"""
Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter "mbox-short.txt" as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
print("Done")

"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname) #open does not read the file but it connects us to the file that we are workin on which is in the same folder with this coding-file.py
count = 0
numbers =0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    start=line.find(":")
    full_number=line[start+1:] # Splits the line at :, & +1 is everything to the right of the colon , and 0 is everything to the left of the colon
    f=float(full_number)
    numbers= numbers + f
    count = count + 1
    print(count, numbers)
print("Average spam confidence:",numbers / count)

"""
or the best way
fname = input("Enter file name: ")
fh = open(fname)

total = 0.0
count = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        # We split the line by the colon, taking the second part [1]
        # and stripping the whitespace away
        parts = line.split(':')
        value = float(parts[1].strip())
        
        total += value
        count += 1

if count == 0:
    print("No matching lines found.")
else:
    print("Average spam confidence:", total / count)
"""