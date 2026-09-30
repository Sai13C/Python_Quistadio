# Movie Collection

movies = {
    "owner": input("Enter your name: "),
    "favorite_movies": []
}

print("\nEnter 3 favorite movies:")

for i in range(3):
    movie = input("Enter movie: ")
    movies["favorite_movies"].append(movie)

print("\n--- Movie Collection ---")
print("Owner:", movies["owner"])

print("Favorite Movies:")
for movie in movies["favorite_movies"]:
    print("-", movie)
