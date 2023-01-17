
# Ali Mohammed

Str1=input('Enter a string: ')
Str2=input('Enter another string: ')
result=False
if(Str1.endswith(Str2)):
    result=True
elif(Str2.endswith(Str1)):
    result=True
print(result)