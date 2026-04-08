
# lists are simmilar to strings, but list is mutable (can changed the items) unlike string whic is immutable (can not be changed the items)
a = [4,6,7,8] # list a
a[2]=10
print(a) # output [4, 6, 10, 8], the index 2 which was 7 got changed to 10
z= "cat"
w=z[1] 
print(w)# output error as it is string, we can't change the items inside, the value here is considered as one value together
y= range(5) # output range(0, 5) weird but 
print(list(range(5)))# output [0, 1, 2, 3, 4] which is correct 