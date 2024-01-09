import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from langchain import PromptTemplate
from dotenv import load_dotenv
from langchain.llms import OpenAI
import os


st.set_page_config(
    initial_sidebar_state="collapsed",
    layout="wide"
)

 
if st.button('Back'):
    switch_page("API Tests")

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

mainBusinessObject = ""
subBusinessObject = ""
mandatoryHeaderPar = ""
nonMandatoryHeaderPar = ""
mandatoryRequestpayloadPar = ""
nonMandatoryRequestpayloadPar = ""



if 'mainBusinessObjective' in st.session_state:
    mainBusinessObject = st.session_state.mainBusinessObjective

if 'subBusinessObjective' in st.session_state:
    subBusinessObject = st.session_state.subBusinessObjective

if 'mandatoryHeaderParams' in st.session_state:
    mandatoryHeaderPar = st.session_state.mandatoryHeaderParams

if 'nonMandatoryHeaderParams' in st.session_state:
    nonMandatoryHeaderPar = st.session_state.nonMandatoryHeaderParams

if 'mandatoryRequestPayloadParameters' in st.session_state:
    mandatoryRequestpayloadPar = st.session_state.mandatoryRequestPayloadParameters

if 'nonMandatoryRequestPayloadParameters' in st.session_state:
    nonMandatoryRequestpayloadPar = st.session_state.nonMandatoryRequestPayloadParameters





st.title('Generate Test Scripts for API Testing')
st.write('Please fill the details below with respect to the test script you want to be generated')
if 'response' in st.session_state:
    tcResponse = st.session_state.response
    st.write('Please copy the test cases you want from the previously generated test cases below.')
    st.code(tcResponse)

template: str = """
I want to generate a test script for below test case. Below I mentioned the test case and API details\n
Test case type - {testCaseType}\n
Test casesd - {testCase}\n
Details:\n
API Endpoint- {apiEndpoint}\n
API Name - {apiName}\n
HTTP Method of API - {httpMethod}\n
Main Business Objective of API - {mainBusinessObjective}\n
Sub Business Objectives of API - {subBusinessObjective}\n
Mandatory Header Parameters - {mandatoryHeaderParams}\n
Non-Mandatory Header Parameters - {nonMandatoryHeaderParams}\n
Mandatory Request Payload Parameters - {mandatoryRequestPayloadParameters}\n
Non Mandatory Request Payload Parameters - {nonMandatoryRequestPayloadParameters}\n
Mandatory Response Payload Parameters - {mandatoryResponsePayloadParameters}\n
Non Mandatory Response Payload Parameters - {nonMandatoryResponsePayloadParameters}\n
Think you are a QA engineer. You need to mainly consider above mentioned test case and generate a Python script according to that testcase, as a professional QA engineer. When you write script please follow coding best practices, coding standards, exception handling as a QA engineer.
"""


on = st.toggle('Populate fields with a sample scenario')
if on:
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', value= 'Positive Test Case',key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_area('Test Cases', placeholder='Please Type the Test Case', value= 'Verify that a meeting can be scheduled successfully with a valid RM and customer.',key = 'testCase', help="Please Enter the Test Case to be tested here.")
        st.text_input('API Endpoint', placeholder='Enter the API Endpoint', value= 'https://localhost/api/v1/test',key = 'apiEndpoint', help="Please Enter the URL of the API to be tested in this field.")
        st.text_input('API Name', placeholder='Enter API Name', key = 'apiName', value= 'ABC Meeting Scheduling with Banker and Gold customer in ABC end.',help="Please Enter the Name of the API Endpoint here.")
        st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', value= 'POST',key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
        st.text_input('Type of End Users', placeholder='Enter the type of End Users', value= 'Two types of bankers RM and FA',key = 'endUserType', help="Enter the type of the End Users as per their roles." )
        st.text_input('Main Business Objective of API',  placeholder='', value= 'Schedule a meeting with Banker and customer with given time in ABC Application application.' ,  key = 'mainBusinessObjective', help="Enter the Primary Business Objective to be tested." )
        st.text_area('Sub Business Objectives of API', placeholder='',value = """RM account should be created in ABC Application end if RM is not available in ABC Application end when schedule meeting with RM and Customer, FA account should be created in ABC Application end if FA is not available in ABC Application end when schedule meeting with FA , Customer account should be created in ABC Application end if customer is not available in ABC Application end when schedule meeting with customer, If relevant RM and Customer are not mapped in ABC Application end  then Mapping should be created in between RM and customer when meeting is schedule with RM and customer,  If relevant FA and Customer are not mapped in ABC Application end then Mapping should be created in between FA and customer when meeting is schedule with FA and customer, Customer should be Mapped with FA and RM when meeting is scheduled with both RM and FA.""",key = 'subBusinessObjective', help="Enter Sub Business Objectiives to be tested. These objectives should be secondary objectives than the Primary Objective.")
        # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Mandatory Header Parameters', placeholder='',value= 'Country code and Business Code ', key = 'mandatoryHeaderParams')
        st.text_input('Non-Mandatory Header Parameters', placeholder='', value= 'UUID',key = 'nonMandatoryHeaderParams')
        st.text_input('Mandatory Request Payload Parameters', placeholder='',value= 'Banker ID, Customer ID, Banker First Name, Customer First Name, Host Type, Start Time and End Time ', key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='',value= 'Banker Last Name and Customer Last name ', key = 'nonMandatoryRequestPayloadParameters')
        st.text_input('Mandatory Response Payload Parameters', placeholder='',value= 'N/A',  key = 'mandatoryResponsePayloadParameters')
        st.text_input('Non-Mandatory Response Payload Parameters', placeholder='', value= 'N/A',  key = 'nonMandatoryResponsePayloadParameters')
        #st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber'),key = 'language',index=0)
        submitted = st.form_submit_button("Generate")

else: 
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_area('Test Cases', placeholder='Please Type the Test Case', key = 'testCase', help="Please Enter the Test Case to be tested here.")
        st.text_input('API Endpoint', placeholder='Enter the API Endpoint', key = 'apiEndpoint', help="Please Enter the URL of the API to be tested in this field.")
        st.text_input('API Name', placeholder='Enter API Name', key = 'apiName', help="Please Enter the Name of the API Endpoint here.")
        st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
        st.text_input('Type of End Users', placeholder='Enter the type of End Users', key = 'endUserType', help="Enter the type of the End Users as per their roles." )
        st.text_input('Main Business Objective of API',  placeholder='', value= mainBusinessObject,  key = 'mainBusinessObjective', help="Enter the Primary Business Objective to be tested." )
        st.text_area('Sub Business Objectives of API', placeholder='', value= subBusinessObject, key = 'subBusinessObjective', help="Enter Sub Business Objectiives to be tested. These objectives should be secondary objectives than the Primary Objective.")
        # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Mandatory Header Parameters', placeholder='',value= mandatoryHeaderPar, key = 'mandatoryHeaderParams')
        st.text_input('Non-Mandatory Header Parameters', placeholder='', value= nonMandatoryHeaderPar,key = 'nonMandatoryHeaderParams')
        st.text_input('Mandatory Request Payload Parameters', placeholder='',value= mandatoryRequestpayloadPar, key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='',value= nonMandatoryRequestpayloadPar, key = 'nonMandatoryRequestPayloadParameters')
        st.text_input('Mandatory Response Payload Parameters', placeholder='', key = 'mandatoryResponsePayloadParameters')
        st.text_input('Non-Mandatory Response Payload Parameters', placeholder='', key = 'nonMandatoryResponsePayloadParameters')
        #st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber'),key = 'language',index=0)
        submitted = st.form_submit_button("Generate")




if submitted: 
    api_ts_template = PromptTemplate.from_template(template)
    api_ts_template.input_variables=['testCaseType','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters']

    formatted_prompt = api_ts_template.format(
        testCaseType = st.session_state.testCaseType,
        testCase = st.session_state.testCase,
        apiEndpoint = st.session_state.apiEndpoint,
        apiName = st.session_state.apiName,
        httpMethod = st.session_state.httpMethod,
        mainBusinessObjective = st.session_state.mainBusinessObjective,
        subBusinessObjective = st.session_state.subBusinessObjective,
        # testScenarioCombination = st.session_state.testScenarioCombination,
        mandatoryHeaderParams = st.session_state.mandatoryHeaderParams,
        nonMandatoryHeaderParams = st.session_state.nonMandatoryHeaderParams,
        mandatoryRequestPayloadParameters = st.session_state.mandatoryRequestPayloadParameters,
        nonMandatoryRequestPayloadParameters = st.session_state.nonMandatoryRequestPayloadParameters,
        mandatoryResponsePayloadParameters = st.session_state.mandatoryResponsePayloadParameters,
        nonMandatoryResponsePayloadParameters = st.session_state.nonMandatoryResponsePayloadParameters
    )

            

    llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

    if(len(formatted_prompt) != 0):
        response = llm(formatted_prompt)
        st.code(response)

st.cache_data.clear()