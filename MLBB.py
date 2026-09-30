# Game Player Information

roles = ("Tank", "Fighter", "Mage", "Marksman", "Support")

player = {
    "name": input("Enter your name: "),
    "ign": input("Enter your game name: "),
    "role": input("Enter your role: ")
}

print("\n--- Player Information ---")
print("Name:", player["name"])
print("IGN:", player["ign"])
print("Role:", player["role"])

print("\n--- Available Roles ---")

for role in roles:
    print("-", role)
