import re
productCatagory = input("What is the product catagory code?\n>")
specificProduct = input("What is the specific product code?\n>")

firstPart = re.compile("([A-Z]){1,2}([0-9]{1,2})")
lastPart = re.compile("[0-9][A-Z](P|Q|R|Z)")

m = firstPart.match(productCatagory)
n = lastPart.match(specificProduct)

print(f"Product catagory is: {m}, product code is: {n}\n")
if m:
    if n:
        print("This is a valid code")
    else:
        print("Not a valid specific product code")
else:
    print("Not a valid product catagory code")