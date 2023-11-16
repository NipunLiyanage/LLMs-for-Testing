import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from langchain import PromptTemplate
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os

st.set_page_config(
    initial_sidebar_state="collapsed",
    layout="wide"
)

if st.button('Back'):
    switch_page("API Tests")

fprompt = ""


load_dotenv()

resultStatus = True

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

st.title('Generate Test Cases for API Testing')
st.write('Please fill the details below with respect to the test case you want to be generated')

template: str = """
I want to generate Positive and negative test cases to verify the following API with define business requirement and expected result of each test cases\n
API Name - {apiName}\n
HTTP Method of API - {httpMethod}\n
Main Business Objective of API - {mainBusinessObjective}\n
Sub Business Objectives of API - {subBusinessObjective}\n
Mandatory Request Payload Parameters - {mandatoryHeaderParams}\n
Respective mandatory parameter Value - {respectiveMandatoryParam}\n
Non-Mandatory Header Parameters - {nonMandatoryHeaderParams}\n
Respective non-mandatory parameter Value - {respectiveNonMandatoryParam}\n
Mandatory Request Payload Parameters - {mandatoryRequestPayloadParameters}\n
Non Mandatory Request Payload Parameters - {nonMandatoryRequestPayloadParameters}\n
Mandatory Response Payload Parameters - {mandatoryResponsePayloadParameters}\n
Non Mandatory Response Payload Parameters - {nonMandatoryResponsePayloadParameters}\n

Think you are a QA engineer. Generate all possible positive and negative test cases list separately as a professional QA engineer to the given business objective. 
When writing the test cases, follow  QA standards, and keywords. Please write test cases as single line.
"""
# Test Scenario Combination - {testScenarioCombination}\n

# def generate():
#     api_tc_template = PromptTemplate.from_template(template)
#     api_tc_template.input_variables=['apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','testScenarioCombination','mandatoryHeaderParams','respectiveMandatoryParam','nonMandatoryHeaderParams','respectiveNonMandatoryParam','mandatoryRequestPayloadParameters']

    
#     global fprompt
#     fprompt = api_tc_template.format(
#         apiName = st.session_state.apiName,
#         httpMethod = st.session_state.httpMethod,
#         mainBusinessObjective = st.session_state.mainBusinessObjective,
#         subBusinessObjective = st.session_state.subBusinessObjective,
#         testScenarioCombination = st.session_state.testScenarioCombination,
#         mandatoryHeaderParams = st.session_state.mandatoryHeaderParams,
#         respectiveMandatoryParam = st.session_state.respectiveMandatoryParam,
#         nonMandatoryHeaderParams = st.session_state.nonMandatoryHeaderParams,
#         respectiveNonMandatoryParam = st.session_state.respectiveNonMandatoryParam,
#         mandatoryRequestPayloadParameters = st.session_state.mandatoryRequestPayloadParameters
#     )

#     # st.write(fprompt)

#     #r = Timer(2.0, setText, (fprompt))
#     #r.start()

#     llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

#     if(len(fprompt) != 0):
#         global response
#         response = llm(fprompt)
#         st.code(response)




    
with st.form('api_tc_gen'):
    st.text_input('API Name', placeholder='Enter API Name', key = 'apiName', help="Please Enter the Name of the API Endpoint here.")
    st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
    st.text_input('Type of End Users', placeholder='Enter the type of End Users', key = 'endUserType', help="Enter the type of the End Users as per their roles." )
    st.text_input('Main Business Objective of API', placeholder='', key = 'mainBusinessObjective', help="Enter the Primary Business Objective to be tested." )
    st.text_area('Sub Business Objectives of API', placeholder='', key = 'subBusinessObjective', help="Enter Sub Business Objectiives to be tested. These objectives should be secondary objectives than the Primary Objective.")
    # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
    st.text_input('Mandatory Header Parameters', placeholder='', key = 'mandatoryHeaderParams')
    st.text_input('Respective Mandatory Parameter Value', placeholder='', key = 'respectiveMandatoryParam')
    st.text_input('Non-Mandatory Header Parameters', placeholder='', key = 'nonMandatoryHeaderParams')
    st.text_input('Respective Non-Mandatory Parameter Value', placeholder='', key = 'respectiveNonMandatoryParam')
    st.text_input('Manatory Request Payload Parameters', placeholder='', key = 'mandatoryRequestPayloadParameters')
    st.text_input('Non-Manatory Request Payload Parameters', placeholder='', key = 'nonMandatoryRequestPayloadParameters')
    st.text_input('Manatory Response Payload Parameters', placeholder='', key = 'mandatoryResponsePayloadParameters')
    st.text_input('Non-Manatory Response Payload Parameters', placeholder='', key = 'nonMandatoryResponsePayloadParameters')
    submitted = st.form_submit_button("Generate")
    

    if submitted:
        api_tc_template = PromptTemplate.from_template(template)
        api_tc_template.input_variables=['apiName','httpMethod','endUserType','mainBusinessObjective','subBusinessObjective','testScenarioCombination','mandatoryHeaderParams','respectiveMandatoryParam','nonMandatoryHeaderParams','respectiveNonMandatoryParam','mandatoryRequestPayloadParameters','nonMandatoryRequestPayloadParameters','mandatoryResponsePayloadParameters','nonMandatoryResponsePayloadParameters']

    
        
        fprompt = api_tc_template.format(
            apiName = st.session_state.apiName,
            httpMethod = st.session_state.httpMethod,
            mainBusinessObjective = st.session_state.mainBusinessObjective,
            subBusinessObjective = st.session_state.subBusinessObjective,
            # testScenarioCombination = st.session_state.testScenarioCombination,
            mandatoryHeaderParams = st.session_state.mandatoryHeaderParams,
            respectiveMandatoryParam = st.session_state.respectiveMandatoryParam,
            nonMandatoryHeaderParams = st.session_state.nonMandatoryHeaderParams,
            respectiveNonMandatoryParam = st.session_state.respectiveNonMandatoryParam,
            mandatoryRequestPayloadParameters = st.session_state.mandatoryRequestPayloadParameters,
            nonMandatoryRequestPayloadParameters = st.session_state.nonMandatoryRequestPayloadParameters,
            mandatoryResponsePayloadParameters = st.session_state.mandatoryResponsePayloadParameters,
            nonMandatoryResponsePayloadParameters = st.session_state.nonMandatoryResponsePayloadParameters
    )

        # st.write(fprompt)

        #r = Timer(2.0, setText, (fprompt))
        #r.start()

        llm = OpenAI(model_name= "gpt-3.5-turbo-0613", temperature = 0.5)

        if(len(fprompt) != 0):
            global response
            response = llm(fprompt)
            st.code(response)

        if(len(response) != 0):
                resultStatus = False

    st.divider()
    st.subheader('Write Test Scripts')
    st.caption(':red[Before selecting the language, please copy the required test cases to the clipboard or note them down to write the script out of the generated test cases before clicking the button.]')

    st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber'),key = 'script_lang',index=0,disabled=resultStatus)
    scripted = st.form_submit_button("Write Test Scripts", disabled=resultStatus)

    if scripted:
        if st.session_state.script_lang == 'Cucumber' :
            switch_page("BDD Feature File Page")
        
        else :
            switch_page("API Test Script Gen")




# st.divider()
# st.caption(':red[Before selecting the language, please copy the required test cases to the clipboard or note them down to write the script out of the generated test cases before clicking the button.]')

# st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber'),key = 'script_lang',index=0,disabled=resultStatus)
# st.caption(':red[Please copy the required test cases to write the script out of the generated test cases before clicking the button.]')



# if st.session_state.script_lang == 'Cucumber' :
#     if st.button('Write the test scripts',disabled=resultStatus):
#         switch_page("BDD Feature File Page")

# else :
#     if st.button('Write the test scripts',disabled=resultStatus):
#         switch_page("API Test Script Gen")

    

# def setText(f_prompt):
#     if(len(f_prompt) != 0):
#         stx.scrollableTextbox(f_prompt)
