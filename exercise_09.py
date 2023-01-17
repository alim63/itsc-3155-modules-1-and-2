# Ali Mohammed

#words string variable
words = ""
arr=[]

for i in range(1,6):
    
    word = input("Enter a word: ")
    arr.append(word)
    words = words + " "+word

print("Words:",arr)    
#printing the concatenated word
print("One String:",words)