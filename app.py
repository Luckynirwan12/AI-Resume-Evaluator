import os
import io
import base64
import pdf2image
import fitz
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load Environment Variable
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel()
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Give the percentage match first, then list missing keywords, followed by final evaluation summary.
"""

input_prompt3 = """
You are a career development expert. Review the resume in the context of the provided job description and 
suggest personalized and actionable skill improvements. Focus on technical, soft, and domain-specific skills 
the candidate should develop to better match the role.
"""

## Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("👩‍💻 AI Resume Evaluator")
st.markdown("### 📌 Step 1: Paste Job Description")
input_text = st.text_area("Job Description", key="input")

st.markdown("### 📌 Step 2: Upload Your Resume")
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully.")
    # --- Show buttons only when file is uploaded ---
    col1, col2, col3 = st.columns(3)
    with col1:
        submit1 = st.button("📄 About Resume")
    with col2:
        submit2 = st.button("📊 ATS Match Report")
    with col3:
        submit3 = st.button("🧠 Skill Suggestions")

    # --- Define prompts (you probably already have this earlier) ---
    input_prompt1 = """Your HR review prompt here..."""
    input_prompt2 = """Your ATS match prompt here..."""
    input_prompt3 = """Your skill improvement prompt here..."""

    # --- Button actions ---
    if submit1:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("About Resume")
        st.write(response)

    if submit2:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("ATS Match Report")
        st.write(response)

    if submit3:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Skill Suggestions")
        st.write(response)

else:
    st.info("⬆️ Please upload your resume (PDF) to get started.")

