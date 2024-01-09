from streamlit_extras.switch_page_button import switch_page
import streamlit as st

st.set_page_config(
    initial_sidebar_state="collapsed"

)


if st.button('Back'):
    switch_page("homepage")

st.title("API Tests Generation")



st.write('Select the task')

col1,col2=st.columns(2)

with col1:
    if st.button('Write API Test Cases'):
        switch_page("API Test Case Gen")

with col2:
    if st.button('Generate Test Scripts'):
        switch_page("API Test Script Gen")
