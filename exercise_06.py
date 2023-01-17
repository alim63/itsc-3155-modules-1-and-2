# Ali Mohammed

array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]    

row = int(input("Enter a row num from 1 to 5: "))
col = int(input("Enter a col num from 1 to 5: "))

array[row-1][col-1] = 1
for x in array:
  for i in x:
    print(i,end="")
  print()