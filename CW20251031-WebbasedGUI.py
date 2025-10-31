import streamlit as st
from PIL import Image

col1, col2 = st.columns((4,5))

with col1:
    st.title("My Resume")
    st.header("Michael Walker")

with col2:
    image = Image.open('dog.jpg')
    st.image(image, width=300)

st.divider()

st.markdown("**About Me**")
st.text("I am a student at JBU currently pursuing cybersecurity.")

st.divider()

st.markdown("**Education**")
st.text("North Arkansas College: 2016-2018, Certificate of Proficiency in Workforce Technology")
st.text("Work Study with Forge Institute in Little Rock, AR, Oct 2024-Jan 2025, Cybersecurity")

st.divider()

st.markdown("**Work Experience**")
st.text("United States Marine Corps: Jan 2020-Jan 2025, Electro-Optical Ordinance Technician")
st.text("HCW: Feb 2025-Sep 2025, Overnight Engineer")