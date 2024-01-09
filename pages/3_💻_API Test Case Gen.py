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




on = st.toggle('Populate fields with a sample scenario')
if on:
    
    with st.form('api_tc_gen'):
        st.text_input('API Name', placeholder='Enter API Name', key = 'apiName', value='ABC Application Meeting Scheduling with Banker and  Gold customer in ABC Application end',help="Please Enter the Name of the API Endpoint here.")
        st.text_input('HTTP Method of API', placeholder='Enter the HTTP Method', value='POST',key = 'httpMethod', help="Please Enter the HTTP method of the API Ex: POST, GET, DELETE, PUT etc.")
        st.text_input('Type of End Users', placeholder='Enter the type of End Users', value='Two types of Bankers RM and FA',key = 'endUserType', help="Enter the type of the End Users as per their roles." )
        st.text_input('Main Business Objective of API', placeholder='',value=' Schedule a meeting with Banker and customer with given time in ABC application', key = 'mainBusinessObjective', help="Enter the Primary Business Objective to be tested." )
        st.text_area('Sub Business Objectives of API', placeholder='', value="""RM account should be created in ABC Application end if RM is not available in ABC Application end when schedule meeting with RM and Customer, FA account should be created in ABC Application end if FA is not available in ABC Application end when schedule meeting with FA , Customer account should be created in ABC Application end if customer is not available in ABC Application end when schedule meeting with customer, If relevant RM and Customer are not mapped in ABC Application end  then Mapping should be created in between RM and customer when meeting is schedule with RM and customer,  If relevant FA and Customer are not mapped in Moxo end  then Mapping should be created in between FA and customer when meeting is schedule with FA and customer, Customer should be Mapped with FA and RM when meeting is scheduled with both RM and FA. """,key = 'subBusinessObjective', help="Enter Sub Business Objectiives to be tested. These objectives should be secondary objectives than the Primary Objective.")
        # st.text_input('Test Scenario Combination', placeholder='', key = 'testScenarioCombination')
        st.text_input('Mandatory Header Parameters', placeholder=' ',value='Country code and Business Code', key = 'mandatoryHeaderParams')
        st.text_input('Respective Mandatory Parameter Value', placeholder='',value='US and GCB', key = 'respectiveMandatoryParam')
        st.text_input('Non-Mandatory Header Parameters', placeholder='',value='UUID', key = 'nonMandatoryHeaderParams')
        st.text_input('Respective Non-Mandatory Parameter Value', placeholder='', value='123456',key = 'respectiveNonMandatoryParam')
        st.text_input('Mandatory Request Payload Parameters', placeholder='',value='Banker ID, Customer ID, Banker First Name, Customer First Name, Host Type,Start Time and End Time', key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='', value='Banker Last Name and Customer Last name ',key = 'nonMandatoryRequestPayloadParameters')
        st.text_input('Mandatory Response Payload Parameters', placeholder='',value='N/A', key = 'mandatoryResponsePayloadParameters')
        st.text_input('Non-Mandatory Response Payload Parameters', placeholder='', value='N/A',key = 'nonMandatoryResponsePayloadParameters')
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
                response = llm(fprompt)
                st.code(response)
                st.session_state['response'] = response

            if(len(response) != 0):
                    resultStatus = False

        st.divider()
        st.subheader('Write Test Scripts')
        st.caption(':red[Before selecting the language, please copy the required test cases to the clipboard or note them down to write the script out of the generated test cases before clicking the button.]')

        st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber (Feature File Already Available)','Cucumber (Generate Both Feature File and Script)'),key = 'script_lang',index=0,disabled=resultStatus)
        scripted = st.form_submit_button("Write Test Scripts", disabled=resultStatus)

        if scripted:
            if st.session_state.script_lang == 'Cucumber (Feature File Already Available)' :
                switch_page("BDD With Feature File")
            
            if st.session_state.script_lang == 'Cucumber (Generate Both Feature File and Script)' :
                switch_page("BDD Without Feature File")

            if st.session_state.script_lang == 'Java' :
                switch_page("API Test Script Gen Java")

            if st.session_state.script_lang == 'Python' :
                switch_page("API Test Script Gen Python")
            
            else :
                switch_page("API Test Script Gen")

else: 
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
        st.text_input('Mandatory Request Payload Parameters', placeholder='', key = 'mandatoryRequestPayloadParameters')
        st.text_input('Non-Mandatory Request Payload Parameters', placeholder='', key = 'nonMandatoryRequestPayloadParameters')
        st.text_input('Mandatory Response Payload Parameters', placeholder='', key = 'mandatoryResponsePayloadParameters')
        st.text_input('Non-Mandatory Response Payload Parameters', placeholder='', key = 'nonMandatoryResponsePayloadParameters')
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

                response = llm(fprompt)
                st.code(response)
                st.session_state['response'] = response

            if(len(response) != 0):
                    resultStatus = False

        st.divider()
        st.subheader('Write Test Scripts')
        st.caption(':red[Before selecting the language, please copy the required test cases to the clipboard or note them down to write the script out of the generated test cases before clicking the button.]')

        st.selectbox('Select the Test Script Language',('Python', 'Java', 'Cucumber (Feature File Already Available)','Cucumber (Generate Both Feature File and Script)'),key = 'script_lang',index=0,disabled=resultStatus)
        scripted = st.form_submit_button("Write Test Scripts", disabled=resultStatus)

        if scripted:
            if st.session_state.script_lang == 'Cucumber (Feature File Already Available)' :
                switch_page("BDD With Feature File")
            
            if st.session_state.script_lang == 'Cucumber (Generate Both Feature File and Script)' :
                switch_page("BDD Without Feature File")

            if st.session_state.script_lang == 'Java' :
                switch_page("API Test Script Gen Java")

            if st.session_state.script_lang == 'Python' :
                switch_page("API Test Script Gen Python")
            
            else :
                switch_page("API Test Script Gen")
    




