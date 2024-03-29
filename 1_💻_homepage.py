import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from dotenv import load_dotenv
import os


st.set_page_config(
    page_title="Test Case Generator",
    page_icon="🖥️",
    initial_sidebar_state="collapsed"
    
)

st.title("Test Case Generator")
model = 'GPT-3.5 Turbo'
st.selectbox('Select the LLM Model to be used',('GPT-3.5 Turbo', 'Google Gemini Pro'),key = 'llmModel',index=0)
st.session_state.model = model
st.write('Please Select the type of tests you want to run')



col1,col2=st.columns(2)

with col1:
    if st.button('API Tests'):
        switch_page("API Tests")

with col2:
    if st.button('User Interface Tests'):
        switch_page("User Interface tests")


