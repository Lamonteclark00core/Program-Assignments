#Lamonte Clark |Lab| Intro to Python
# ------------------------------------------
# Ticket 1 - Check a list of ages
# ------------------------------------------

print("=== Ticket 1 ===")

ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")


# ------------------------------------------
# Ticket 2 - While Loop
# ------------------------------------------

print("\n=== Ticket 2 ===")

keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter an age: "))

    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")

    keep_checking = input("Check another age? (yes/no): ").lower()


# ------------------------------------------
# Ticket 3 - while True
# ------------------------------------------

print("\n=== Ticket 3 ===")

while True:
    user_input = input("Enter an age or type 'stop': ")

    if user_input.lower() == "stop":
        print("Goodbye!")
        break

    age = int(user_input)

    if age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")


# ------------------------------------------
# Ticket 4 - Function
# ------------------------------------------

print("\n=== Ticket 4 ===")


def can_access(age):
    return age >= 13


ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")


# ------------------------------------------
# Ticket 5 - Signup Report
# ------------------------------------------

print("\n=== Ticket 5 ===")


def signup_report(signups):
    approved = 0

    print("--- StreamPass Signup Report ---")

    for number, age in enumerate(signups, start=1):

        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")

    print(f"\nApproved: {approved} out of {len(signups)}")


signups = [22, 10, 15, 8, 19, 13]

signup_report(signups)