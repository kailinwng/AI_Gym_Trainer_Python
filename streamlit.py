import streamlit as st
from streamlit_webrtc import webrtc_streamer #https://github.com/whitphx/streamlit-webrtc

st.title ("A.I. Gym Trainer 💪")
st.markdown("Hello there, thank you for using our AI gym trainer program.")
st.markdown("Just like a personal gym trainer, this program helps you keep track of the number of exercise repetition you performed, along with a pose correction feedback mechanism to correct your pose if needed.")
st.markdown("At the end of your exercise, a chart will be displayed to show you your performance throughout the exercise. 📈")
st.markdown("\nExercises supported: Squats, Arm Curl, Situp")
st.caption("Note. This is a Monash University final year project completed by Kai Lin Wong, Eu Yang Chai and Kee Hong Tan;")
st.caption("under the supervision of Dr Raphael Phan; completed in year 2021.")
           
st.subheader("this is the subheader")

webrtc_streamer(key="frame")

