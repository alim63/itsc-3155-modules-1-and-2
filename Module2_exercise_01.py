# Ali Mohammed
b = input("Enter a string: ")

upper = ""
lower = ""

for ch in b:
    if ch.isupper():
        upper += ch
    elif ch.islower():
        lower += ch

result = lower + upper

print(result)