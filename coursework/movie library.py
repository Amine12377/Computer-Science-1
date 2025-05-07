movie_library = [] #Creating tbe library
movie_library.append({"title":"Inception",
                  "year":2010,
                  "genres":["Action", "Sci-Fi"],
                  "rating":(4.5, 1500),
                  "reviews":{"Micheal":"very good"}})
movie_library.append({
                "title":"Titanic",
                  "year":1997,
                  "genres":["Romance", "Drama"],
                  "rating":(4.7, 2000),
                  "reviews":{"Joe":"sad as hell"}
                    })
movie_library.append({
                    "title":"The Matrix",
                  "year":1999,
                  "genres":["Action", "Sci-Fi"],
                  "rating":(4.8, 1800),
                  "reviews":{"John":"cool"}
                    })
#displaying all current movies:
for movie in movie_library:
    print(f'Name: {movie["title"]}\nYear: {movie["year"]}\nGenre: {movie["genres"][0]}, {movie["genres"][1]}\nrating: {movie["rating"][0]}\nNumber of reviews: {movie["rating"][1]}\n')

#Searching movies by genres:
search = input("Enter the genre of the movie you want to search: ")
for movie1 in movie_library:
    if search in movie1["genres"]:
        print(f'Name: {movie1["title"]}\nYear: {movie1["year"]}\nGenre: {movie1["genres"][0]}, {movie1["genres"][1]}\nrating: {movie1["rating"][0]}\nNumber of reviews: {movie1["rating"][1]}\n')

#details of specific movie:
search1 = input("Enter the title for details: ")
for movie2 in movie_library:
    if search1 == movie2["title"]:
        print(f'Name: {movie2["title"]}\nYear: {movie2["year"]}\nGenre: {movie2["genres"][0]}, {movie2["genres"][1]}\nrating: {movie2["rating"][0]}\nNumber of reviews: {movie2["rating"][1]}\nreviews: {movie2["reviews"]}')

#add a review:
search2 = input("Enter the title to add a review: ")
for movie3 in movie_library:
    if search2 in movie3["title"]:
        name = input("enter your name: ")
        review = input("enter the review: ")
        movie3["reviews"][name] = review
        movie3["rating"] = (5, movie3["rating"][1])
        print(f'\nName: {movie3["title"]}\nYear: {movie3["year"]}\nGenre: {movie3["genres"][0]}, {movie3["genres"][1]}\nrating: {movie3["rating"][0]}\nNumber of reviews: {movie3["rating"][1]}\nreviews: {movie3["reviews"]}')
#average rating.
total_rating = 0
total_reviews = 0
for i in movie_library:
    rating, num_reviews = i['rating']
    total_rating += rating* num_reviews
    total_reviews += num_reviews
print(total_rating/total_reviews)



