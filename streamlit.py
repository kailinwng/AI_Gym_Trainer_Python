import streamlit as st

st.title ("A.I. Gym Trainer 💪")
st.header("this is the markdown")
st.markdown("Hello there, thank you for using our AI gym trainer program. \nJust like a personal gym trainer, we aim to help you keep track of the number of exercise repetition you performed, along with a pose correction feedback mechanism to correct your pose if needed. \nAt the end of your exercise, a chart will be displayed to show you your performance throughout the exercise. 📈\nExercises supported: Squats, Arm Curl, Situp")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)


