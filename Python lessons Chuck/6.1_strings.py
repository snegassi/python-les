'''
# Apparently string is an object, which means object have methods 
# (createdby ".somethin()"after the  variable name) and can find the methods by dir(name of the variable)
name= "Daniel"
up = name.upper()
print(up)
print(dir(name))
'''

"""
Question
Write code using find() and string slicing (see section 6.10) to extract the number at the end
 of the line below. Convert the extracted value to a floating point number and print it out.
  
text = "X-DSPAM-Confidence:    0.8475"
"""

text = "X-DSPAM-Confidence:    0.8475"

x=text.find("0")

y=text.find("5",x)

z=text[x:y+1] #+1 is one more from y 

a= float(z)
print(x)
print(y)
print(z)
print(a)

"""
OR best way
# 1. Find the position of the colon
pos = text.find(':') # this part makes it best because it findes the colon & on the next linesplits it right from :, & selects the right from : by 1 and to the left by 0

# 2. Slice from the colon (+1) to the end of the string
# 3. Convert to float (Python's float() automatically ignores the extra spaces)
value = float(text[pos+1:])

print(value)
"""