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


st.title('Generate Test Scripts for Functional UI Testing')
st.write('Please fill the details below with respect to the test case you want to be generated')

template = """ 
I want to generate selenium test script for below test case. Below I mentioned the test case and business requirement.\n
Test case type - {testCaseType}\n
Test case - {testCase}\n
Business Requirement:\n
User Story Name - {userStoryName}\n
Main Business Functionality - {mainBusinessFunc}\n
Sub Business Functionalites - {subBusinessFunc}\n
Precondition - {precondition}\n
Type of End Users - {endUsersType}\n
Think you are a QA engineer. You need to mainly consider above mention test case and generate selenium script for {language} according to that testcase, as a professional QA engineer. When you write selenium script please follow coding best practices, coding standards, exception handling as a QA engineer.
"""
on = st.toggle('Populate fields with a sample scenario')
if on:
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type',value='Positive Test Case ', key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_input('Test Case', placeholder='Please Type the Test Case', value="Verify that the meeting details are added to the agent's timeline and calendar option when a meeting request is received from XYZ end.",key = 'testCase', help="Please Enter the Test Case to be tested here.")
        st.text_input('User Story Name', placeholder='Enter the User Story Name', value='ABC Agent gold customer Meeting Scheduling',key = 'userStoryName',help="Please Enter the Name of the User Story here")
        st.text_area('Main Business Functionality', placeholder='', value='The meeting details are added to the relevant agent timeline and calendar option, The meeting details are added to the relevant customer calendar option and dashboard, The agent can initiate the meeting in ABC Application, and the customer should be able to join the meeting.',key = 'mainBusinessFunc',help="Enter the Primary Business Functionality to be tested.")
        st.text_area('Sub Business Functionalities', placeholder='', value='N/A',key = 'subBusinessFunc',help="Enter the Sub business functionalities to be tested.")
        # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Precondition', placeholder='Precondition', value='The meeting request should come from XYZ end. ',key = 'precondition', help="Please Enter the Pre Conditions that should be met.")
        st.text_input('Type of End Users', placeholder='Type of End Users',value='Two types of agents, RM and FA.', key = 'endUsersType', help="Enter the type of the End Users as per their roles.")
        st.selectbox('Select the Language',('Python', 'Java'),key = 'language',placeholder='Select for which language the selenium script should be generated',index=None)
        submitted = st.form_submit_button("Generate")

else: 
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_input('Test Case', placeholder='Please Type the Test Case', key = 'testCase', help="Please Enter the Test Case to be tested here.")
        st.text_input('User Story Name', placeholder='Enter the User Story Name', key = 'userStoryName',help="Please Enter the Name of the User Story here")
        st.text_area('Main Business Functionality', placeholder='', key = 'mainBusinessFunc',help="Enter the Primary Business Functionality to be tested.")
        st.text_area('Sub Business Functionalities', placeholder='', key = 'subBusinessFunc',help="Enter the Sub business functionalities to be tested.")
        # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Precondition', placeholder='Precondition', key = 'precondition', help="Please Enter the Pre Conditions that should be met.")
        st.text_input('Type of End Users', placeholder='Type of End Users', key = 'endUsersType', help="Enter the type of the End Users as per their roles.")
        st.selectbox('Select the Language',('Python', 'Java'),key = 'language',placeholder='Select for which language the selenium script should be generated',index=None)
        submitted = st.form_submit_button("Generate")

if submitted: 
    ui_ts_template = PromptTemplate.from_template(template)
    ui_ts_template.input_variables = ['testCaseType','testCase','userStoryName','mainBusinessFunc','subBusinessFunc','precondition','endUsersType','language']

    formatted_prompt = ui_ts_template.format(
        testCaseType = st.session_state.testCaseType,
        testCase = st.session_state.testCase,
        userStoryName = st.session_state.userStoryName,
        mainBusinessFunc = st.session_state.mainBusinessFunc,
        subBusinessFunc = st.session_state.subBusinessFunc,
        # testScenarioCombination = st.session_state.testScenarioCombination,
        precondition = st.session_state.precondition,
        endUsersType = st.session_state.endUsersType,
        language = st.session_state.language
    )

    llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

    if(len(formatted_prompt) != 0):
        response = llm(formatted_prompt)
        st.code(response)
