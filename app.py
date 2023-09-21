import streamlit as st
import pickle
import pandas as pd

def recommend(song):
       music_index = music[music['title'] == song].index[0]
       distances = similarity[music_index]
       music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

       recommended_music=[]
       for i in music_list:
            recommended_music.append(music.iloc[i[0]].title)
       return recommended_music



m_list= pickle.load(open('movie_list.pkl','rb'))
music=pd.DataFrame(m_list)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Divyanshi\'s Recommender System")

selected_music_name=st.selectbox(
 'PLEASE ENTER A MOVIE YOU LIKE',
 music['title'].values)

if st.button('Recommend'):
    recommendations= recommend(selected_music_name)
    for i in recommendations:
        st.write(i)
