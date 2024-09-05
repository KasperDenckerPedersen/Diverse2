import re

catagoryCode = []
productCode = []

fileHandler = open('Exam-2023/codes.txt', 'r')
for code in fileHandler:
    code = code.strip()
    if ',' in code:
        catagory, product = code.split(',', 1)
        catagoryCode.append(catagory.strip())
        productCode.append(product.strip())
fileHandler.close()

firstPart = re.compile("([A-Z]){1,2}([0-9]{1,2})")
lastPart = re.compile("[0-9][A-Z](P|Q|R|Z)")

ValidCodes = []

for i in range(len(catagoryCode)):
    m = firstPart.match(catagoryCode[i])
    n = lastPart.match(productCode[i])

    if m:
        if n:
            ValidCodes.append(catagoryCode[i] + "-" + productCode[i] )
        else:
            print(f"{catagoryCode[i]}-{productCode[i]}")
            print("Is not a valid specific product code\n")
    else:
        print(f"{catagoryCode[i]}-{productCode[i]}")
        print("Is not a valid product catagory code\n")

print("All the valid codes are:")
for i in range(len(ValidCodes)):
    print(ValidCodes[i])
