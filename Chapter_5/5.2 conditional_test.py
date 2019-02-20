str1 = "Jack"
str2 = "John"
if str1 == str2:
    print("str1 == str2")
else:
    print("str1 != str2")

str3 = "jack"
if str1.lower() == str3:
    print("str1 == str3")
else:
    print("str1 != str3")

if 24 < 24.5:
    print("24 < 24.5")
else:
    print("24 > 24.5")

if 26 < 30 and 35 > 30:
    print("Test True")

if 30 > 34 or 60 < 64:
    print("Test True")

numbers = [25,27,30,10]
if 10 in numbers:
    print("10 in numberlists")
if 65 not in numbers:
    print("65 not in numberlists")         