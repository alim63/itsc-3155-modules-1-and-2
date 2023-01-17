# Ali Mohammed

arr1=[]
i = 0
l = input("Enter a number or QUIT to quit: ")
while (l != "QUIT"):
    arr1.append(int(l))
    l = input("Enter a number or QUIT to quit: ")
    
arr2=[]
for i in range(0, len(arr1)):
    if(arr1[i] % 2 == 0):
        arr2.append(arr1[i])
print("All Nums:",arr1)        
print("Even Nums:",arr2)