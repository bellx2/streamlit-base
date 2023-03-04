import streamlit as st

st.title('Stremalit Main Page')
st.write('This is the main page of the app')
img = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'])
if img is not None:
    st.image(img)
