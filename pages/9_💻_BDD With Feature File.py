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
    switch_page("BDD Feature File Page")



os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]



st.title('Generate Test Scripts for Test Cases That Already Have a BDD Feature/ Scenario File.')
st.write('Please fill the details below with respect to the test script you want to be generated')
if 'response' in st.session_state:
    tcResponse = st.session_state.response
    st.write('Please copy the test cases you want from the previously generated test cases below.')
    st.code(tcResponse)


scenario_template: str = """I want to generate cucumber scenario for below test case. Below I mention test case and API details.

Test case type - {testCaseType}\n
Tag name - {tagName} \n
Test case - {testCase}\n

Details:
API Endpoint - {apiEndpoint}\n
HTTP Method of API - {httpMethod}\n
Mandatory Header Parameters - {mandatoryHeaderParams}\n
Non-Mandatory Header Parameters - {nonMandatoryHeaderParams}\n
Mandatory Request Payload Parameters - {mandatoryRequestPayloadParameters}\n
Non-Mandatory Request Payload Parameters - {nonMandatoryRequestPayloadParameters}\n

Think you are a QA engineer. I need to genarate cucumber scenario for above test case, as a professional QA engineer. Please mainly focus about above mention test case and i need to genarate cucumber scenarion only for that test case. When you write cucumber scenario, please follow coding best practices, coding standards, exception handling as a QA engineer.
Only output the test scenario document.
"""

step_def_template: str = """
I want to generate java cucumber step definition for below cucumber feature file. Below I mention test case, API details and cucumber scenario.

Test case type - {testCaseType}\n
Tag name - {tagName} \n
Test cases - {testCase}\n

Details:
API Endpoint - {apiEndpoint}\n
HTTP Method of API - {httpMethod}\n
Mandatory Header Parameters - {mandatoryHeaderParams}\n
Non-Mandatory Header Parameters - {nonMandatoryHeaderParams}\n
Mandatory Request Payload Parameters - {mandatoryRequestPayloadParameters}\n
Non-Mandatory Request Payload Parameters - {nonMandatoryRequestPayloadParameters}\n
Cucumber scenario - {scenario}

Think you are a QA engineer. I need to genarate java cucumber step definition for above test case, as a professional QA engineer. Please mainly focus about above mention cucumber scenario and i need to genarate java cucumber step definition only for that cucumber scenario. When you write java cucumber step definition, please follow coding best practices, coding standards, exception handling as a QA engineer."""

sample_step_def: str = """
**Feature: Scheduling a Meeting**

**Scenario: Schedule a Meeting with Valid RM and Customer**

**Given**
- A valid RM and customer exist in the system
- The API endpoint is https://localhost/api/v1/test
- The HTTP method of the API is POST
- The mandatory header parameters are Country code and business code
- The mandatory request payload parameters are Banker ID, Customer ID, Banker First Name, Customer First Name, Host Type, Start Time and End Time

**When**
- A meeting is scheduled with the valid RM and customer using the API

**Then**
- The API responds with a success status code
- The meeting is successfully scheduled in the system

**Examples:**
| Country code | Business code | Banker ID | Customer ID | Banker First Name | Customer First Name | Host Type | Start Time | End Time |
|---|---|---|---|---|---|---|---|---|
| IN | 1234 | 123456 | 654321 | John | Mary | Zoom | 2023-03-08T10:00:00 | 2023-03-08T11:00:00 |

**Scenario Outline:**

**Given**
- A valid RM and customer exist in the system
- The API endpoint is https://localhost/api/v1/test
- The HTTP method of the API is POST
- The mandatory header parameters are Country code and business code
- The mandatory request payload parameters are Banker ID, Customer ID, Banker First Name, Customer First Name, Host Type, Start Time and End Time

**When**
- A meeting is scheduled with the valid RM and customer using the API with the following data:

| Country code | Business code | Banker ID | Customer ID | Banker First Name | Customer First Name | Host Type | Start Time | End Time |
|---|---|---|---|---|---|---|---|---|
| <countryCode> | <businessCode> | <bankerId> | <customerId> | <bankerFirstName> | <customerFirstName> | <hostType> | <startTime> | <endTime> |

**Then**
- The API responds with a success status code
- The meeting is successfully scheduled in the system

**Examples:**
| countryCode | businessCode | bankerId | customerId | bankerFirstName | customerFirstName | hostType | startTime | endTime |
| IN | 1234 | 123456 | 654321 | John | Mary | Zoom | 2023-03-08T10:00:00 | 2023-03-08T11:00:00 |
| US | 5678 | 234567 | 765432 | Jane | Michael | Google Meet | 2023-03-09T12:00:00 | 2023-03-09T13:00:00 |
"""
on = st.toggle('Populate fields with a sample scenario')
if on:
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', value= 'Positive Test Case',key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_input('Tag Name', placeholder='Enter the name of the tag',value='DevEnv', key = 'tagName', help="Enter the tag name that is used to group the test cases")
        st.text_area('Test Cases', placeholder='Please Type the Test Case', value= 'Verify that a meeting can be scheduled successfully with a valid RM and customer.',key = 'testCase', height=150, help="Please Enter the Test Case to be tested here.")
        st.text_input('API Endpoint', placeholder='Enter the API Endpoint', value= 'https://localhost/api/v1/test',key = 'apiEndpoint', help="Please Enter the URL of the API to be tested in this field.")
        st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', value= 'POST',key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
        st.text_input('Mandatory Header Parameters', placeholder='',value= 'Country code and Business Code ', key = 'mandatoryHeaderParams')
        st.text_input('Non-Mandatory Header Parameters', placeholder='', value= 'UUID',key = 'nonMandatoryHeaderParams')
        st.text_input('Mandatory Request Payload Parameters', placeholder='',value= 'Banker ID, Customer ID, Banker First Name, Customer First Name, Host Type, Start Time and End Time ', key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='',value= 'Banker Last Name and Customer Last name ', key = 'nonMandatoryRequestPayloadParameters')
        st.text_area('Enter the Cucumber Feature File/ Scenario', placeholder='', value=sample_step_def, key = 'scenario', help="Copy the Cucumber Scenario File/ Feature File", height=500)
        submitted = st.form_submit_button("Generate")

else: 
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_input('Tag Name', placeholder='Enter the name of the tag', key = 'tagName', help="Enter the tag name that is used to group the test cases")
        st.text_area('Test Cases', placeholder='Please Type the Test Case', key = 'testCase', help="Please Enter the Test Case to be tested here.", height=150)
        st.text_input('API Endpoint', placeholder='Enter the API Endpoint', key = 'apiEndpoint', help="Please Enter the URL of the API to be tested in this field.")
        st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
        st.text_input('Mandatory Header Parameters', placeholder='', key = 'mandatoryHeaderParams')
        st.text_input('Non-Mandatory Header Parameters', placeholder='', key = 'nonMandatoryHeaderParams')
        st.text_input('Mandatory Request Payload Parameters', placeholder='', key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='', key = 'nonMandatoryRequestPayloadParameters')
        st.text_area('Enter the Cucumber Feature File/ Scenario', placeholder='', key = 'scenario', help="Copy the Cucumber Scenario File/ Feature File", height=500)
        submitted = st.form_submit_button("Generate")

if submitted: 

    cucumber_td_template = PromptTemplate.from_template(step_def_template)
    cucumber_td_template.input_variables=['testCaseType','tagName','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters','language','scenario']

    cucumber_step_formatted_prompt = cucumber_td_template.format(
        testCaseType = st.session_state.testCaseType,
        tagName = st.session_state.tagName,
        testCase = st.session_state.testCase,
        apiEndpoint = st.session_state.apiEndpoint,
        httpMethod = st.session_state.httpMethod,
        # mainBusinessObjective = st.session_state.mainBusinessObjective,
        # subBusinessObjective = st.session_state.subBusinessObjective,
        # testScenarioCombination = st.session_state.testScenarioCombination,
        mandatoryHeaderParams = st.session_state.mandatoryHeaderParams,
        nonMandatoryHeaderParams = st.session_state.nonMandatoryHeaderParams,
        mandatoryRequestPayloadParameters = st.session_state.mandatoryRequestPayloadParameters,
        nonMandatoryRequestPayloadParameters = st.session_state.nonMandatoryRequestPayloadParameters,
        # mandatoryResponsePayloadParameters = st.session_state.mandatoryResponsePayloadParameters,
        # nonMandatoryResponsePayloadParameters = st.session_state.nonMandatoryResponsePayloadParameters,
        # language = st.session_state.language
        scenario = st.session_state.scenario
            )

    llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

    if(len(cucumber_step_formatted_prompt) != 0):
            response_2 = llm(cucumber_step_formatted_prompt)
            st.code(response_2)
