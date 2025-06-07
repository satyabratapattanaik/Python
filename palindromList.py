# WAP to check if a list is Palindrom or not

List1 = [1, 2, 3, 2, 1]

copy_List1 = List1.copy()
copy_List1.reverse()

if(copy_List1 == List1):
    print("Palindrom")
else:
    print("Not a Palindrom")


List2 = [1, 2, 3]

copy_List2 = List2.copy()
copy_List2.reverse()

if(copy_List2 == List2):
    print("Palindrom")
else:
    print("Not a Palindrom")