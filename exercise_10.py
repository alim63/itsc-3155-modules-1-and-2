# Ali Mohammed

string = (input("Enter a string: ")) #Prompting User to Enter string
lst = list(string) #break string variable into list of characters

x = 3 # number of element in each list

# using list comprehension to create list of list
A = [lst[i:i + x] for i in range(0, len(lst), x)]
print(A)