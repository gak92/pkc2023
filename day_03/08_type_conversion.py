# Type Conversion
x = 10
y = 19.7
z = "Hello"

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Implicit Conversion
x = x + y
print(x, "type of x now: ", type(x))

# Explicit Conversion
age = input("What is your age: ")
print(age, "age type: ", type(age))

# age = int(age)
# print(age, "age type after conversion: ", type(age))


age = float(age)
print(age, "age type after conversion: ", type(age))