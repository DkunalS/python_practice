# basic method
def checkPallindrome(str):
    return str == str[::-1]

def checkSymrical(str):
    length = len(str)
    mid = length//2
    if length%2 == 0:
        return str[:mid] == str[mid:]
    else:
        return str[:mid] == str[mid + 1 :]
    
str = "abcdeffedcba"

if  checkSymrical(str):
    print(f"String {str} is symmetrical")
else:
    print(f"String {str} is not Symmetrical")

if checkPallindrome(str):
    print(f"String {str} is pallindorme")
else:
    print(f"String {str} is not pallindrome") 

# Using slicing

orig_String = "abdeffedcba"
reverse_String = orig_String[::-1]
if orig_String == reverse_String:
    print("String is symmetrical")
else:
    print("String is not symmetrical ")