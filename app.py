import streamlit as  st  # type: ignore
import os
import PyPDF2 as pypdf  

try:
    from langchain.chat_models import ChatOpenAI      # type: ignore
except ImportError:
    print("Module 'langchain.chat_models' not found.")

from dotenv import load_dotenv              # type: ignore

load_dotenv()

# Now you can create ChatOpenAI instance without hardcoding keys
# llm = ChatOpenAI()

def get_openai_response(input):
    model = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
    response = model.predict(input)
    return response

def input_pdf_text(uploaded_file):
    reader = pypdf.PdfReader(uploaded_file)
    number_of_pages = len(reader.pages)
    text = ""
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += page.extract_text()
    return text


## Prompt Template
input_prompt = """
Hey, act like a skilled or highly experienced ATS (Application Tracking System)
with a deep understanding of tech fields such as software engineering, data science,
data analysis, and big data engineering.

Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive and provide the best
possible assistance for improving the resume.

Assign a percentage match score based on the JD and
identify missing keywords with high accuracy.

resume: {text}
description: {jd}

I want the response in one single JSON-like string having the structure:
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

st.title("Smart Resume Analyzer")
st.text("Improve Your Resume ATS Match Rate with Smart Resume Analyzer")
jd = st.text_area("Enter Job Description Here", height=200)
uploaded_file = st.file_uploader("Upload Your Resume in PDF Format", type=["pdf"] , help ="Upload a PDF file containing your resume.")

submit = st.button("Submit")


if submit:
    if uploaded_file is not None :
        text = input_pdf_text(uploaded_file)
        response = get_openai_response(input_prompt.format(text=text, jd=jd))
        response = response[response.find("{"): response.rfind("}")+1]
        st.subheader("Analysis Result")
        st.text(response)
    else:
        st.warning("Please upload a PDF file containing your resume.")