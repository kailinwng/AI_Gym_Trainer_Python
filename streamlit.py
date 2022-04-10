import streamlit as st
from streamlit_webrtc import webrtc_streamer #https://github.com/whitphx/streamlit-webrtc

#import mediapipe as mp
#import cv2
import numpy as np
import matplotlib.pyplot as plt
#import mediapipe

# draw landmarks & connections to screen
#mp_drawing = mp.solutions.drawing_utils
# import Pose model
#mp_pose = mp.solutions.pose

#https://github.com/whitphx/streamlit-webrtc-example/blob/main/app.py

st.set_page_config(page_title='A.I. Gym Trainer', page_icon="🏋️‍♂️", layout="centered",menu_items={
         #'Get Help': 'https://www.extremelycoolapp.com/help',
         #'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "This program is a Monash University final year project completed by Kai Lin Wong, Eu Yang Chai and Kee Hong Tan; under the supervision of Dr Raphael Phan; completed in year 2021. \n This Streamlit app is built by Kai Lin Wong: https://www.linkedin.com/in/kai-lin-wong31/ \nGithub link: https://github.com/kailinwng/AI_Gym_Trainer_Python"
     })

st.title ("A.I. Gym Trainer 🏋️‍♂️")
st.markdown("Hello there, thank you for using our AI gym trainer program.")
st.markdown("\nJust like a personal gym trainer, this program helps you keep track of the number of exercise repetition you performed, along with a pose correction feedback mechanism to correct your pose if needed. ✔️")
st.markdown("\nAt the end of your exercise, a chart will display your performance throughout the exercise. 📈")

st.caption("Note. This program is a Monash University final year project completed by Kai Lin Wong, Eu Yang Chai and Kee Hong Tan; under the supervision of Dr Raphael Phan; completed in year 2021.")
st.caption("This Streamlit app is built by Kai Lin Wong: https://www.linkedin.com/in/kai-lin-wong31/")
st.caption("Github link: https://github.com/kailinwng/AI_Gym_Trainer_Python")  

st.markdown("\nExercises supported: ")
gifs = ['https://images.squarespace-cdn.com/content/v1/54f9e84de4b0d13f30bba4cb/1530742878727-5TT9N6GWHG8SQUPVO1WQ/ke17ZwdGBToddI8pDm48kMh3mVmBaCAeGwqCLG3iONRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZamWLI2zvYWH8K3-s_4yszcp2ryTI0HqTOaaUohrI8PIBW4H-Ca6AoigG7Ta8YXcF_lHpbhrmZNZWbxxrH_bJLk/bodyweight+squat.gif',"https://media1.tenor.com/images/c6e16a9b9dc7d97b0d4ad78b50e7b424/tenor.gif?itemid=3579635","https://www.spotebi.com/wp-content/uploads/2014/10/biceps-curl-exercise-illustration.gif"]
capt = ['Squats','Situp','Bicep curl']
col1, col2, col3 = st.columns(3)
col1.image(gifs[0], width= 200, caption = capt[0])
col2.image(gifs[1], width= 200, caption = capt[1])
col3.image(gifs[2], width= 200, caption = capt[2])
st.caption("\nNote: Bicep curls must be done with both arms performing the same motion together.")

st.header("Let's Begin! 💦")
exc = st.radio('Pick your exercise:', ['Squats','Situp','Bicep curl'])

cam = "<p style='color:Red;'>Make sure that you have enabled the camera on your computer before proceeding! 💻</p>"
st.markdown(cam, unsafe_allow_html=True)

frame = webrtc_streamer(key="webcam")

st.metric(label="Reps Per Hour", value="0", delta="1")
st.metric(label="Calories Burned", value="0", delta="1")

if st.button("Stop exercise."):
  st.balloons()
  st.success("You did it!")
  

  
