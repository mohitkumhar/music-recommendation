import streamlit as st
import pandas as pd
import pickle

# Load the data and similarity matrix
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommandation(song):
    if song not in df['song'].values:
        return [f"Song '{song}' not found in the dataset."]
    
    idx = df[df['song'] == song].index[0]
    distances = [(i, sim) for i, sim in enumerate(similarity[idx].flatten()) if i != idx]
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    songs = [df.iloc[i[0]]['song'] for i in distances[:20]]
    return songs

# Streamlit app
st.title("Song Recommendation System")

# Dropdown menu for song selection
song_list = list(df['song'].values)
selected_song = st.selectbox("Select a Song:", song_list)

# Button to get recommendations
if st.button("Get Recommendations"):
    recommendations = recommandation(selected_song)
    st.write("### Recommended Songs:")
    for idx, rec_song in enumerate(recommendations, start=1):
        st.write(f"{idx}. {rec_song}")
