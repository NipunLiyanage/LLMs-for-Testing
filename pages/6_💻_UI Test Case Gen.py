import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from langchain import PromptTemplate
from dotenv import load_dotenv
from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]
st.set_page_config(
    initial_sidebar_state="collapsed",
    layout="wide"
)

 
if st.button('Back'):
    switch_page("User Interface tests")

st.title('Generate Test Cases for Functional UI Testing')
st.write('Please fill the details below with respect to the test case you want to be generated')




template = """ 
I want to generate Positive and negative test cases to verify the following define business requirement\n
User Story Name - {userStoryName}\n
Main Business Functionality - {mainBusinessFunc}\n
Sub Business Functionalites - {subBusinessFunc}\n
Precondition - {precondition}\n
Type of End Users - {endUsersType}\n
Think you are a QA engineer. Generate all possible positive and negative test cases listed separately as a professional QA engineer to the given objective details. When writing the test cases, follow QA standards, and keywords. Please give test cases as a single line.
"""


on = st.toggle('Populate fields with a sample scenario')
if on:  
    with st.form('api_tc_gen', clear_on_submit=True):
        st.text_input('User Story Name', placeholder='Enter the User Story Name',value='ABC Application Agent gold customer Meeting Scheduling ', key = 'userStoryName',help="Please Enter the Name of the User Story here")
        st.text_area('Main Business Functionality', placeholder='', value=' The meeting details are added to the relevant agent timeline and calendar option, The meeting details are added to the relevant customer calendar option and dashboard,The agent can initiate the meeting in ABC Application, and the customer should be able to join the meeting. ',key = 'mainBusinessFunc',help="Enter the Primary Business Functionality to be tested.")
        st.text_area('Sub Business Functionalities', placeholder='', value='N/A',key = 'subBusinessFunc',help="Enter the Sub business functionalities to be tested.")
        #st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Precondition', placeholder='Precondition',value='The meeting request should come from XYZ end.', key = 'precondition', help="Please Enter the Pre Conditions that should be met.")
        st.text_input('Type of End Users', placeholder='Type of End Users', value='Two types of agents, RM and FA' ,key = 'endUsersType', help="Enter the type of the End Users as per their roles.")
        submitted = st.form_submit_button('Generate')

else: 
    with st.form('api_tc_gen', clear_on_submit=True):
        st.text_input('User Story Name', placeholder='Enter the User Story Name', key = 'userStoryName',help="Please Enter the Name of the User Story here")
        st.text_area('Main Business Functionality', placeholder='', key = 'mainBusinessFunc',help="Enter the Primary Business Functionality to be tested.")
        st.text_area('Sub Business Functionalities', placeholder='', key = 'subBusinessFunc',help="Enter the Sub business functionalities to be tested.")
        #st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Precondition', placeholder='Precondition', key = 'precondition', help="Please Enter the Pre Conditions that should be met.")
        st.text_input('Type of End Users', placeholder='Type of End Users', key = 'endUsersType', help="Enter the type of the End Users as per their roles.")
        submitted = st.form_submit_button('Generate')

if submitted: 
    ui_tc_template = PromptTemplate.from_template(template)
    ui_tc_template.input_variables = ['userStoryName','mainBusinessFunc','subBusinessFunc','precondition','endUsersType']


    formatted_prompt = ui_tc_template.format(
        userStoryName = st.session_state.userStoryName,
        mainBusinessFunc = st.session_state.mainBusinessFunc,
        subBusinessFunc = st.session_state.subBusinessFunc,
        # testScenarioCombination = st.session_state.testScenarioCombination,
        precondition = st.session_state.precondition,
        endUsersType = st.session_state.endUsersType
    )

    llm = OpenAI(model_name = "gpt-3.5-turbo-0613", temperature = 0.5)

    
    if(len(formatted_prompt) != 0):
        response = llm(formatted_prompt)
        st.code(response)


