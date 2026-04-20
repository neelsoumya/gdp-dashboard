import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to Streamlit! 👋")

# Get user input
name = st.text_input("What's your name?")
age = st.slider("How old are you?", 0, 120, 25)

# Display results
if name:
    st.write(f"Hello {name}! You are {age} years old.")
    st.balloons()
