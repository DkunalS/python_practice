
# num = int(input("Enter the number for fibonacci series: "))

# for i in range(0, num):


def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

# Get the number of terms from the user
n = int(input("Give the number of terms: "))

# Display the Fibonacci sequence of the given term
print("Fibonacci Sequence:")
print(fibonacci(n))