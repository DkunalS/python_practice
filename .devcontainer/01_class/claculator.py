
# def calculator()
num1 = float(input("Enter the number: "))
num2 = float(input("Enter the number: "))
operator = input("Enter the operator: ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':15
    print(num1 / num2)
else:
    print("You have entered wrong opeartion")