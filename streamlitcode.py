import streamlit as st
import pandas as pd

movies_file_path = 'D:/CSV/Movies.csv'
posters_file_path = 'D:/CSV/PosterPath.csv'


df1 = pd.read_csv(movies_file_path)
df2 = pd.read_csv(posters_file_path)


df2 = pd.concat((df1, df2), axis=1)

mood_to_genre = {
    'Energetic': 'Action',
    'Excited': 'Horror',
    'Adrenaline-seeking': 'Thriller',
    'Curious': 'Adventure',
    'Explorative': 'Science Fiction',
    'Lighthearted': 'Comedy',
    'Cheerful': 'Comedy',
    'Nostalgic': 'Animation',
    'Reflective': 'Drama',
    'Warm': 'Family',
    'Romantic': 'Romance',
    'Imaginative': 'Fantasy',
    'Intellectual': 'History',
    'Artistic': 'Music',
    'Inquisitive': 'Mystery',
    'Serious': 'War',
    'Casual': 'TV Movie',
}


st.title("Movie Recommendation App Based on your Mood")


user_mood = st.selectbox("Select your mood:", list(mood_to_genre.keys()))

genre = mood_to_genre.get(user_mood)

if genre:
    
    filtered_movies = df2[df2['genres'].str.contains(genre, na=False)]
    if not filtered_movies.empty:

        recommended_movies = filtered_movies[['title', 'release_date', 'user_score', 'poster_path']].sample(5).sort_values(by="user_score",ascending=False)

        st.subheader("Recommended Movies:")
        for _, row in recommended_movies.iterrows():
            st.image(row['poster_path'], width=150, caption=row['title'])
            st.write(f"**Title:** {row['title']}")
            st.write(f"**Release Date:** {row['release_date']}")
            st.write(f"**User Score:** {row['user_score']}")
            st.write("---")
    else:
        st.warning(f"Sorry, we couldn't find any movies in the '{genre}' genre.")
else:
    st.error("Invalid mood input. Please choose from the given options.")
