
def fact(num):
    result = 1
    for i in range (1, num +1):
        result*=i
    return result

# for i in 5
num = (input("Enter the number for Factorial"))
print(f"The factorial of {num} is {fact(num)} : ")