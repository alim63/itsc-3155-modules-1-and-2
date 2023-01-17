# Ali Mohammed
arr=[]
for i in range(10):
    print("Enter number",i+1,":",end=" ")
    arr.append(int(input())) 
result=[]
for i in arr:
 if(arr.count(i)==1):
  result.append(i)
print("Original List:",arr)  
print("Nums that appear once: ",result)