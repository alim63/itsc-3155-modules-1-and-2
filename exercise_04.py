# Ali Mohammed

n=int(input("Enter a number: ")) # enter input 
v = [] # list to store the input values
for i in range(1,n+1): # loop take input of n elements
    print("Enter number ",i,":", end = " ")
    v.append(float(input()))#add number to list

#calculate mean
mean = 0
for i in v:
    mean += i
mean /= n

# print the list
print('List:',v)

print("Average: " + str(mean)) # prints mean