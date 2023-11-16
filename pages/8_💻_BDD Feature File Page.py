from streamlit_extras.switch_page_button import switch_page
import streamlit as st

st.set_page_config(
    initial_sidebar_state="collapsed"

)


if st.button('Back'):
    switch_page("API Test Case Gen")

st.title("Do You Already Have a Feature File Created for the Test Cases?")

st.write('Select an Option')

col1,col2=st.columns(2)

with col1:
    if st.button('Yes, I have.'):
        switch_page("BDD With Feature File")

with col2:
    if st.button('No, I do not have.'):
        switch_page("BDD Without Feature File")