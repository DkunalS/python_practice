num1 = float(input("Enter the number: "))
num2 = float(input("Enter the number: "))
operator = input("Enter the operator: ")

if operator == '+':
    print("result is: "num1 + num2)
elif operator == '-':
    print("result is: "num1 - num2)
elif operator == '*':
    print("result is: "num1 * num2)
elif operator == '/':
    print("result is: "num1 / num2)
else:
    print("You have entered wrong opeartion")