import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from langchain.prompts import PromptTemplate
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



st.title('Generate BDD Feature File and Step Definitions')
st.write('Please fill the details below with respect to the test script you want to be generated')
if 'response' in st.session_state:
    tcResponse = st.session_state.response
    st.write('Please copy the test cases you want from the previously generated test cases below.')
    st.code(tcResponse)


scenario_template: str = """I want to generate cucumber scenario for below test case. Below I mention test case and API details.

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

Think you are a QA engineer. I need to genarate cucumber scenario for above test case, as a professional QA engineer. Please mainly focus about above mention test case and i need to genarate cucumber scenarion only for that test case. When you write cucumber scenario, please follow coding best practices, coding standards, exception handling as a QA engineer.
Only output the test scenario document.
"""

step_def_template: str = """
I want to generate java cucumber step definition for below cucumber scenario. Below I mention test case, API details and cucumber scenario.

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
Cucumber scenario - {response}

Think you are a QA engineer. I need to genarate java cucumber step definition for above test case, as a professional QA engineer. Please mainly focus about above mention cucumber scenario and i need to genarate java cucumber step definition only for that cucumber scenario. When you write java cucumber step definition, please follow coding best practices, coding standards, exception handling as a QA engineer."""

on = st.toggle('Populate fields with a sample scenario')
if on:
    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', value= 'Positive Test Case',key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_input('Tag Name', placeholder='Enter the name of the tag',value='DevEnv', key = 'tagName', help="Enter the tag name that is used to group the test cases")
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
        submitted = st.form_submit_button("Generate")

else:

    with st.form('api_ts_gen'):
        st.text_input('Test Case Type', placeholder='Enter Test Case Type', key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
        st.text_input('Tag Name', placeholder='Enter the name of the tag', key = 'tagName', help="Enter the tag name that is used to group the test cases")
        st.text_area('Test Cases', placeholder='Please Type the Test Case', key = 'testCase', help="Please Enter the Test Case to be tested here.")
        st.text_input('API Endpoint', placeholder='Enter the API Endpoint', key = 'apiEndpoint', help="Please Enter the URL of the API to be tested in this field.")
        st.text_input('API Name', placeholder='Enter API Name', key = 'apiName', help="Please Enter the Name of the API Endpoint here.")
        st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
        st.text_input('Type of End Users', placeholder='Enter the type of End Users', key = 'endUserType', help="Enter the type of the End Users as per their roles." )
        st.text_input('Main Business Objective of API', placeholder='',value= mainBusinessObject, key = 'mainBusinessObjective', help="Enter the Primary Business Objective to be tested." )
        st.text_area('Sub Business Objectives of API', placeholder='',value= subBusinessObject, key = 'subBusinessObjective', help="Enter Sub Business Objectiives to be tested. These objectives should be secondary objectives than the Primary Objective.")
        # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Mandatory Header Parameters', placeholder='',value= mandatoryHeaderPar, key = 'mandatoryHeaderParams')
        st.text_input('Non-Mandatory Header Parameters', placeholder='', value= nonMandatoryHeaderPar,key = 'nonMandatoryHeaderParams')
        st.text_input('Mandatory Request Payload Parameters', placeholder='',value= mandatoryRequestpayloadPar, key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='',value= nonMandatoryRequestpayloadPar, key = 'nonMandatoryRequestPayloadParameters')
        st.text_input('Mandatory Response Payload Parameters', placeholder='', key = 'mandatoryResponsePayloadParameters')
        st.text_input('Non-Mandatory Response Payload Parameters', placeholder='', key = 'nonMandatoryResponsePayloadParameters')
        # st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber'),key = 'language',index=0)
        submitted = st.form_submit_button("Generate") 

if submitted: 
    cucumber_ts_template = PromptTemplate.from_template(scenario_template)
    cucumber_ts_template.input_variables=['testCaseType', 'tagName', 'testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters']

    cucumber_scenario_formatted_prompt = cucumber_ts_template.format(
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
    )

    llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

    if(len(cucumber_scenario_formatted_prompt) != 0):
        global response_1 
        response_1 = llm(cucumber_scenario_formatted_prompt)
        st.code(response_1)

    cucumber_td_template = PromptTemplate.from_template(step_def_template)
    cucumber_td_template.input_variables=['testCaseType','tagName','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters','language','response']

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
        response = response_1
    )
    

    if(len(cucumber_step_formatted_prompt) != 0):
        response_2 = llm(cucumber_step_formatted_prompt)
        st.code(response_2)


st.cache_data.clear()







