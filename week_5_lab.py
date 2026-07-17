1.
# game.py

scores = [95, 88, 76, 100]

print(scores[5])
# game.py

scores = [95, 88, 76, 100]

print(scores[3])   # Prints the last item
2.
print("Hello, world!"
      x = 10

if x > 5
    print("x is greater than 5")
    message = Hello, world!

print(message)
for i in range(5):
print(i)
def greeting(name):
    retrun "Hello, " + name

print(greeting("Alice"))
3.
# ZeroDivisionError

divisor = 0

if divisor != 0:
    print(10 / divisor)
else:
    print("Cannot divide by zero.")
    # TypeError

age = "25"

total = 30 + int(age)

print(total)
# IndexError

numbers = [1, 2, 3]

print(numbers[2])
# KeyError

person = {
    "name": "John",
    "age": 30
}

print(person.get("city", "Unknown"))
# NameError

age = 25

print(age)
4.
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
    name = "Charlie"

if name == "Alice" or name == "Bob":
    print("Hello, friend!")
else:
    print("Hello, stranger!")
    count = 0

while count < 5:
    print(count)
    count += 1
    5.
    def calculate_area(radius):
    print("DEBUG radius =", radius)

    area = 3.14 * radius ** 2

    print("DEBUG area =", area)

    return area

print(calculate_area(5))
6.
def get_positive_number():

    while True:

        entry = input("Enter a positive whole number: ")

        if entry.isdigit() and int(entry) > 0:
            return int(entry)

        print("Invalid input. Please enter a positive whole number.")

age = get_positive_number()

print("You entered", age)

8.
x = 10
y = 0

if y != 0:
    result = x / y
    print("Result:", result)
else:
    print("Cannot divide by zero.")
    numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
    def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5

print(calculate_area(radius))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
for i in range(5):
    print(i)
    def greet(name):
    return "Hello, " + name

print(greet("Alice"))
numbers = [1, 2, 3, 4, 5]

total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
name = input("Enter your name: ")

if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
    def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))
