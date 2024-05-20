# import streamlit as st
# from langchain.llms import OpenAI
import openai
import streamlit as st


# st.title("AI-Powered Resume Builder")

# api_key = st.text_input('Enter your OpenAI API key:', type='password')

# if api_key:

#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     phone = st.text_input("Phone")
#     job_title = st.text_input("Job Title")
#     experience = st.text_area("Work Experience")
#     education = st.text_area("Education")

#     if st.button("Generate Resume"):
#         prompt = f"Generate a professional resume for {name} with email {email} and phone {phone}. " \
#                  f"The job title is {job_title}. Here is the work experience: {experience}. " \
#                  f"And here is the education: {education}."

#         llm = OpenAI(temperature=0.7, openai_api_key=api_key)
#         st.header("Generated Resume")
#         st.warning(prompt)
#         st.text_area("Resume", value=llm(prompt), height=400)
# else:
#     st.warning("Please enter your OpenAI API key.")




st.title('👩‍💼 Welcome to AI-Powered Resume Builder')

api_key = st.sidebar.text_input('Enter your OpenAI API key: ', type='password')

client = openai.OpenAI(
    api_key= api_key,
    base_url="https://api.aimlapi.com/",
)

def generate_response(name, email, phone, job_title, experience, education):
    prompt = f"Generate a professional resume for {name} with email {email} and phone {phone}. " \
                 f"The job title is {job_title}. Here is the work experience: {experience}. " \
                 f"And here is the education: {education}."
    chat_completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            prompt
        ],
        temperature=0.7,
        max_tokens=512,
    )
    chat_completion.choices[0].message.content

with st.form('my_form'):
    # system_instructions = st.text_area('Enter System Role:')
    # user_query= st.text_area('Enter user content:')
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    job_title = st.text_input("Job Title")
    experience = st.text_area("Work Experience")
    education = st.text_area("Education")
    
    submitted = st.form_submit_button('Submit')
   
    if submitted:
        try:
            generate_response(name, email, phone, job_title, experience, education)
        except Exception as e:
            print('Failed to generate : %s', repr(e))
