# 🤖 AI Resume Evaluator
AI Resume Evaluator is a Streamlit-based web application that leverages Google Gemini to analyze resumes, compare them against job descriptions, and provide insights like HR reviews, ATS match scores, skill improvement suggestions, and missing keywords.

---

### 🚀 Features
- 📄 About Resume: Simulates a human HR’s evaluation of your resume for a given job description, highlighting strengths and weaknesses.

- 📊 ATS Match Report: Calculates a match percentage, lists missing keywords, and gives a final summary.

- 🧠 Skill Suggestions: Recommends technical, soft, and domain-specific skills to improve your chance.

---

### 🛠️ Tech Stack
- Streamlit

- Google Gemini API

- pdf2image for resume image conversion

- Python

---

### 🧪 Setup Instructions
1. Clone the repository:

       git clone https://github.com/your-username/ai-resume-evaluator.git
       cd ai-resume-evaluator

2. Install dependencies:

       pip install -r requirements.txt

3. Set up environment variables:

Create a `.env` file in the root directory with your Google Gemini API key:

     GOOGLE_API_KEY=your_google_api_key
     
🔧 Also ensure you have Poppler installed and added to your PATH (for pdf2image to work).

4. Run the Streamlit app:

       streamlit run app.py

---

### 📂 Folder Structure

├── app.py

├── requirements.txt

├── .env

---
