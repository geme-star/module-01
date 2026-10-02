name = input("What's your name? ")
print(f"Hello, {name}! Let's track your expense.")
print()

item = input("What did you buy? ")
amount = float(input("How much? "))

print()
print("----- EXPENSE SUMMARY -----")
print(f"{item}: ${amount}")
print("---------------------------")