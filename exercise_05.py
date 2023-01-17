# Ali Mohammed

# initialize two lists 
v1 = []
v2 = [] 
# ask user to input 5 integers for first list
for i in range(5):
    v1.append(int(input("Enter a number for the first list: "))) 

# ask user to input 5 integers for second list
for i in range(5):
    v2.append(int(input("Enter a number for the second list: "))) 

v3 = [] # create new list

for i in v1:
    if i in v2:
       if i not in v3:
           v3.append(i)
#print all three lists
print("First List: ",v1)
print("Second List: ",v2)
print("Common List: ",v3)