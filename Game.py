games = []

print("Enter your 5 favorite games:")

for i in range(5):
    game = input("Enter game: ")
    games.append(game)

print("\nYour favorite games are:")

for game in games:
    print("-", game)
