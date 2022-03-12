import streamlit as st
from streamlit_webrtc import webrtc_streamer #https://github.com/whitphx/streamlit-webrtc

st.title ("A.I. Gym Trainer 💪")
st.markdown("Hello there, thank you for using our AI gym trainer program. \nJust like a personal gym trainer, we aim to help you keep track of the number of exercise repetition you performed, along with a pose correction feedback mechanism to correct your pose if needed. \nAt the end of your exercise, a chart will be displayed to show you your performance throughout the exercise. 📈\nExercises supported: Squats, Arm Curl, Situp")
st.caption("Note. This is a Monash University final year project completed by Kai Lin Wong, Eu Yang Chai and Kee Hong Tan;")
st.caption(under the supervision of Dr Raphael Phan; completed in year 2021.")
           
st.subheader("this is the subheader")

webrtc_streamer(key="example")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)


