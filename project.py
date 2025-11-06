# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter to keep only movies released in the 1990s (1990 to 1999)
movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Visualize the duration column to see the distribution of movie durations
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Based on the histogram, the most frequent duration is approximately 100 minutes
duration = 100

# Filter the data to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies (less than 90 minutes) there were in the 1990s
short_movie_count = 0
for label, row in action_movies_1990s.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1

# Print the count for verification (should be 7 based on the dataset)
print(short_movie_count)
