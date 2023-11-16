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


st.title('Generate Test Scripts for API Testing')
st.write('Please fill the details below with respect to the test script you want to be generated')


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
Think you are a QA engineer. You need to mainly consider above mentioned test case and generate a {language} script according to that testcase, as a professional QA engineer. When you write script please follow coding best practices, coding standards, exception handling as a QA engineer.
"""

scenario_template: str = """I want to generate cucumber scenario for below test case. Below I mention test case and API details.

Test case type - {testCaseType}\n
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



# def generate():
#     api_ts_template = PromptTemplate.from_template(template)
#     api_ts_template.input_variables=['testCaseType','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','testScenarioCombination','mandatoryHeaderParams','respectiveMandatoryParam','nonMandatoryHeaderParams','respectiveNonMandatoryParam','mandatoryRequestPayloadParameters']

#     formatted_prompt = api_ts_template.format(
#         testCaseType = st.session_state.testCaseType,
#         testCase = st.session_state.testCase,
#         apiEndpoint = st.session_state.apiEndpoint,
#         apiName = st.session_state.apiName,
#         httpMethod = st.session_state.httpMethod,
#         mainBusinessObjective = st.session_state.mainBusinessObjective,
#         subBusinessObjective = st.session_state.subBusinessObjective,
#         testScenarioCombination = st.session_state.testScenarioCombination,
#         mandatoryHeaderParams = st.session_state.mandatoryHeaderParams,
#         respectiveMandatoryParam = st.session_state.respectiveMandatoryParam,
#         nonMandatoryHeaderParams = st.session_state.nonMandatoryHeaderParams,
#         respectiveNonMandatoryParam = st.session_state.respectiveNonMandatoryParam,
#         mandatoryRequestPayloadParameters = st.session_state.mandatoryRequestPayloadParameters,
#         nonMandatoryRequestPayloadParameters = st.session_state.nonMandatoryRequestPayloadParameters
#     )

    

#     llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

#     if(len(fprompt) != 0):
#         response = llm(fprompt)
#         st.code(response)

# Test Scenario Combination - {testScenarioCombination}\n
with st.form('api_ts_gen'):
    st.text_input('Test Case Type', placeholder='Enter Test Case Type', key = 'testCaseType',help="Enter the type of the test case here. Ex: Positive, Negative etc.")
    st.text_input('Test Case', placeholder='Please Type the Test Case', key = 'testCase', help="Please Enter the Test Case to be tested here.")
    st.text_input('API Endpoint', placeholder='Enter the API Endpoint', key = 'apiEndpoint', help="Please Enter the URL of the API to be tested in this field.")
    st.text_input('API Name', placeholder='Enter API Name', key = 'apiName', help="Please Enter the Name of the API Endpoint here.")
    st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
    st.text_input('Type of End Users', placeholder='Enter the type of End Users', key = 'endUserType', help="Enter the type of the End Users as per their roles." )
    st.text_input('Main Business Objective of API', placeholder='', key = 'mainBusinessObjective', help="Enter the Primary Business Objective to be tested." )
    st.text_area('Sub Business Objectives of API', placeholder='', key = 'subBusinessObjective', help="Enter Sub Business Objectiives to be tested. These objectives should be secondary objectives than the Primary Objective.")
    # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
    st.text_input('Mandatory Header Parameters', placeholder='', key = 'mandatoryHeaderParams')
    st.text_input('Non-Mandatory Header Parameters', placeholder='', key = 'nonMandatoryHeaderParams')
    st.text_input('Manatory Request Payload Parameters', placeholder='', key = 'mandatoryRequestPayloadParameters')
    st.text_input('Non-Manatory Request Payload Parameters', placeholder='', key = 'nonMandatoryRequestPayloadParameters')
    st.text_input('Manatory Response Payload Parameters', placeholder='', key = 'mandatoryResponsePayloadParameters')
    st.text_input('Non-Manatory Response Payload Parameters', placeholder='', key = 'nonMandatoryResponsePayloadParameters')
    st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber'),key = 'language',index=0)
    submitted = st.form_submit_button("Generate")

    if submitted: 
        if st.session_state.language == 'Cucumber' :

            cucumber_ts_template = PromptTemplate.from_template(scenario_template)
            cucumber_ts_template.input_variables=['testCaseType','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters','language']

            cucumber_scenario_formatted_prompt = cucumber_ts_template.format(
                testCaseType = st.session_state.testCaseType,
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
            cucumber_td_template.input_variables=['testCaseType','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters','language','response']

            cucumber_step_formatted_prompt = cucumber_td_template.format(
                testCaseType = st.session_state.testCaseType,
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



        else : 

            api_ts_template = PromptTemplate.from_template(template)
            api_ts_template.input_variables=['testCaseType','testCase','apiEndpoint','apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','mandatoryHeaderParams','nonMandatoryHeaderParams','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters','language']

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
                nonMandatoryResponsePayloadParameters = st.session_state.nonMandatoryResponsePayloadParameters,
                language = st.session_state.language
            )

            

            llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

            if(len(formatted_prompt) != 0):
                response = llm(formatted_prompt)
                st.code(response)
