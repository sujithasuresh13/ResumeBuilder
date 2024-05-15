import streamlit as st
import openai

st.title("AI-Powered Resume Builder")

api_key = st.text_input("Enter your OpenAI API key:", type="password")

if api_key:
    openai.api_key = api_key

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    job_title = st.text_input("Job Title")
    experience = st.text_area("Work Experience")
    education = st.text_area("Education")

    if st.button("Generate Resume"):
        prompt = f"Generate a professional resume for {name} with email {email} and phone {phone}. " \
                 f"The job title is {job_title}. Here is the work experience: {experience}. " \
                 f"And here is the education: {education}."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional resume writer."},
                {"role": "user", "content": prompt},
            ],
        )

        resume = response.choices[0].message['content']
        st.header("Generated Resume")
        st.text_area("Resume", value=resume, height=400)
else:
    st.warning("Please enter your OpenAI API key.")
