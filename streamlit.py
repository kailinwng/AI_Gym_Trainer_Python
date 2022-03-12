import streamlit as st
from streamlit_webrtc import webrtc_streamer #https://github.com/whitphx/streamlit-webrtc


#https://github.com/whitphx/streamlit-webrtc-example/blob/main/app.py

st.title ("A.I. Gym Trainer 💪")
st.markdown("Hello there, thank you for using our AI gym trainer program.")
st.markdown("\nJust like a personal gym trainer, this program helps you keep track of the number of exercise repetition you performed, along with a pose correction feedback mechanism to correct your pose if needed.")
st.markdown("\nAt the end of your exercise, a chart will be displayed to show you your performance throughout the exercise. 📈")
st.markdown("\nExercises supported: Squats, Arm Curl, Situp")

st.caption("Note. This is a Monash University final year project completed by Kai Lin Wong, Eu Yang Chai and Kee Hong Tan; under the supervision of Dr Raphael Phan; completed in year 2021.")
st.caption("Github link: https://github.com/kailinwng/AI_Gym_Trainer_Python")   

st.header("Instructions:")
instruction = "<p color:Red>Make sure that you have enabled the camera on your computer before proceeding! 💻</p>"
st.markdown(instruction, unsafe_allow_html=True)


webrtc_streamer(key="frame")

