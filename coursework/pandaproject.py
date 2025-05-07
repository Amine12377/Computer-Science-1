import pandas as pd
#creating the dataset:
movie1 = {"Name": str("Titanic"),
          "Director": str("James Cameron"),
          "Year": int(1997),
          "Genre": str("Drama"),
          "Rating": float(8.9),
          "Budget": int(200),
          "Revenue": int(2264)}
movie2 = {"Name": str("Inception"),
          "Director": str("Christopher Nolan"),
          "Year": int(2010),
          "Genre": str("Sci-Fi"),
          "Rating": float(8.8),
          "Budget": int(160),
          "Revenue": int(829)}
movie3 = {"Name": str("The Godfather"),
          "Director": str("Francis Ford Coppola"),
          "Year": int(1972),
          "Genre": str("Crime"),
          "Rating": float(9.2),
          "Budget": int(6),
          "Revenue": int(250)}
movie4 = {"Name": str("Avatar"),
          "Director": str("James Cameron"),
          "Year": int(2009),
          "Genre": str("Sci-Fi"),
          "Rating": float(7.9),
          "Budget": int(237),
          "Revenue": int(2847)}
movie5 = {"Name": str("The Dark Knight"),
          "Director": str("Christopher Nolan"),
          "Year": int(2008),
          "Genre": str("Action"),
          "Rating": float(9.0),
          "Budget": int(185),
          "Revenue": int(1006)}
movie6 = {"Name": str("Parasite"),
          "Director": str("Bong Joon-ho"),
          "Year": int(2019),
          "Genre": str("Thriller"),
          "Rating": float(8.5),
          "Budget": int(11),
          "Revenue": int(266)}
#putting them in a list:
movies = [movie1, movie2, movie3, movie4, movie5, movie6]
#creating data frame:
df = pd.DataFrame(movies)
print(df.head(2)) # displaying few rows
print(df.describe()) #Summary statistics

greater_than_8 = df[df['Rating']>8] #Showing movies with a rating greater than 8.0
print(greater_than_8)
revenue_500 = df[df['Revenue']>500] #Showing movies with a box office greater than 500 mil
print(revenue_500)

sort_year = df.sort_values(by='Year', ascending=False) #Sorting by year
print(sort_year)
sort_revenue = df.sort_values(by='Revenue') #sorting by revenue
print(sort_revenue)

average = df['Rating'].mean() #Average movie rating
print(average)
combined_budget = df['Budget'].sum() #Total combined budget
print(combined_budget)
highest_grossing_movie = df.sort_values(by='Revenue', ascending=False).iloc[0] #highest revenue film
print(highest_grossing_movie)

average_rating_genre = df.groupby("Genre")["Rating"].mean() #Average rating per genre
print(average_rating_genre)
director_revenue = df.groupby("Director")["Revenue"].sum() #Average revenue per director.
print(director_revenue)

#Extra challenge
df['Profit'] = df['Revenue'] - df['Budget'] #creating a profit column
print(df.sort_values(by='Profit', ascending=False).iloc[0]) #idnetifying highest profit