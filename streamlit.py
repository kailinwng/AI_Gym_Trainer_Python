import streamlit as st
from streamlit_webrtc import webrtc_streamer #https://github.com/whitphx/streamlit-webrtc

#https://github.com/whitphx/streamlit-webrtc-example/blob/main/app.py

st.set_page_config(page_title='A.I. Gym Trainer', page_icon="🏋️‍♂️", layout="centered")
                   #, initial_sidebar_state="auto", menu_items=None)

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
st.image(gifs, width= 200, caption = capt)
st.markdown("\nNote: Bicep curls must be done with both arms performing the same motion together.")

st.header("Let's Begin! 💦")

exc = st.radio('Pick your exercise:', ['Squats','Situp','Bicep curl'])

cam = "<p style='color:Red;'>Make sure that you have enabled the camera on your computer before proceeding! 💻</p>"
st.markdown(cam, unsafe_allow_html=True)
frame = webrtc_streamer(key="webcam")

if st.button("Stop exercise."):
  st.balloons()
  st.success("You did it!")
  

  
