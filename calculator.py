def add(p, q):
    return p + q
def subtraction(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p, q):
    return p / q


print("Please select an operator:")
print("Option a: Addition")
print("Option b: Subtraction")
print("Option c: Multiply")
print("Option d: Divide")
choice = input("Enter your choice here:")


num_1 = int(input("Please enter the first number here:"))
num_2 = int(input("Please enter the second number here:"))

if choice == "a":
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == "b":
    print(num_1, "-", num_2, "=", subtraction(num_1, num_2))

elif choice == "c":
    print(num_1, "x", num_2, "=", multiply(num_1, num_2))

elif choice == "d":
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("This is not a valid option")