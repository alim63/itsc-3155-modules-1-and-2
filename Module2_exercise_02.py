# Ali Mohammed

# take user input in variable str1
str1 = input("Enter a string: ")


# find length of string 
i=len(str1)-1

# loop will run until i is less than 0
while(i>=0):
    # print the string character (last to first index)
    print(str1[i],end='')
    # decrement the value of variable i by 1 
    i = i-1