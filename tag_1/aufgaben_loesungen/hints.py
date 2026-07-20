x = "" 

if x:
    print("x ist kein leerer String")

if not x:
    print("x ist leerer String")

dirty_string = "\n42x\t"
cleaned_string = dirty_string.strip()
print(cleaned_string)