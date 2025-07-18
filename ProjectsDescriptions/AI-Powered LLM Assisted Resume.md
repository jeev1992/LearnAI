# 🧠 AI-Powered LLM-Assisted Resume/ATS Scoring Assistant

## 📘 Project Description

The **AI-powered Resume/ATS Scoring Assistant** streamlines the hiring process by leveraging Large Language Models (LLMs) like OpenAI's GPT-4 to analyze, score, and improve resumes based on specific job descriptions. This tool offers both recruiters and applicants a smarter, faster, and more transparent evaluation of qualifications and alignment with job requirements.

## 🎯 Objectives

- Automate resume screening and scoring
- Provide actionable feedback for resume improvement
- Identify the best-fit candidate for a job
- Ensure alignment with job descriptions and requirements
- Seamlessly integrate with existing ATS platforms

## 🔍 Key Features

- **Resume Upload and Parsing**: Upload resumes (PDF, DOCX) and extract structured data such as work history, education, and skills.
- **Job Description Input**: Paste or select job descriptions for comparison.
- **Resume Scoring**: Score resumes based on keyword match, skill relevance, formatting, and overall fit.
- **LLM-Generated Feedback** *(Extra)*: Personalized resume critique with specific suggestions for improvement.
- **Dashboard & Analytics** *(Extra)*: Visual tools to review candidate scores and filter top talent.
- **ATS Integration** *(Extra)*: REST APIs allow connection to existing applicant tracking systems.

## 🧰 Tech Stack Overview

| Component    | Technology                          |
|--------------|-------------------------------------|
| Frontend     | React or Streamlit                  |
| Backend      | Flask, Django, or Node.js           |
| Database     | MongoDB                             |
| LLM/NLP      | OpenAI GPT-4 / Gemini Pro + LangChain |
| Deployment   | Docker + AWS                        |
| CI/CD        | GitHub Actions                      |

## 🚀 Deliverables

- A working, full-stack application
- LLM-integrated resume parser and scorer
- Frontend interface for uploading resumes and viewing scores
- Documentation and user manual
- Deployment-ready Docker and CI/CD setup

---

## 🔧 Tech Stack

- **Frontend**: React (though I’ll mention how to switch to Streamlit)
- **Backend**: Flask (you can ask for a Django or Node.js version anytime)
- **Database**: MongoDB via pymongo
- **LLM**: OpenAI GPT-4 via LangChain
- **CI/CD**: GitHub Actions
- **Deployment**: Docker and AWS

---

## 🧱 Folder Structure

```
resume-ats-assistant/
│
├── backend/
│   ├── app.py
│   ├── langchain_utils.py
│   ├── parser.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker-compose.yml
└── README.md
```

---

## Backend (Flask + Langchain + MongoDB)

#### `app.py`

```python
from flask import Flask, request, jsonify
from pymongo import MongoClient
from parser import parse_resume
from langchain_utils import score_resume

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client.resume_db

@app.route("/upload", methods=["POST"])
def upload_resume():
    resume_file = request.files['resume']
    job_description = request.form['job_description']
    parsed_resume = parse_resume(resume_file)
    
    score, feedback = score_resume(parsed_resume, job_description)
    
    db.resumes.insert_one({
        "parsed_resume": parsed_resume,
        "job_description": job_description,
        "score": score,
        "feedback": feedback
    })
    
    return jsonify({"score": score, "feedback": feedback})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
```

#### `langchain_utils.py`

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model_name="gpt-4", temperature=0.2)

def score_resume(resume_data, job_description):
    prompt = f"""
    Resume: {resume_data}
    Job Description: {job_description}
    Score this resume out of 100. Provide detailed feedback on how to improve it.
    """
    response = llm([HumanMessage(content=prompt)])
    text = response.content
    score_line = next((line for line in text.split('\\n') if 'score' in line.lower()), None)
    score = int(''.join(filter(str.isdigit, score_line))) if score_line else 0
    return score, text
```

#### `parser.py`

```python
import fitz  # PyMuPDF for PDF

def parse_resume(file):
    text = fitz.open(stream=file.read(), filetype="pdf").get_page_text(0)
    return text
```

#### `requirements.txt`

```
Flask
pymongo
langchain
openai
PyMuPDF
```

---

## Frontend (React)

#### `App.jsx`

```jsx
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('job_description', jd);

    const res = await axios.post('/upload', formData);
    setResult(res.data);
  };

  return (
    <div>
      <h2>Resume Scorer</h2>
      <input type="file" onChange={e => setResume(e.target.files[0])} />
      <textarea placeholder="Paste Job Description" value={jd} onChange={e => setJd(e.target.value)} />
      <button onClick={handleUpload}>Score Resume</button>
      {result && (
        <div>
          <p><strong>Score:</strong> {result.score}</p>
          <pre>{result.feedback}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
```

---

## 🐳 Docker Setup

#### `backend/Dockerfile`

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

#### `frontend/Dockerfile`

```Dockerfile
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

#### `docker-compose.yml`

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    depends_on:
      - mongo

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"

  mongo:
    image: mongo
    ports:
      - "27017:27017"
```

---

## 🛠 GitHub Actions CI

#### `.github/workflows/ci.yml`

```yaml
name: Resume ATS App CI

on:
  push:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    services:
      mongo:
        image: mongo
        ports: ['27017:27017']

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install backend dependencies
      run: |
        cd backend
        pip install -r requirements.txt

    - name: Lint Backend
      run: |
        cd backend
        flake8 .

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '20'

    - name: Install frontend dependencies
      run: |
        cd frontend
        npm ci

    - name: Lint Frontend
      run: |
        cd frontend
        npm run lint
```

---

## 🧪 Optional: Streamlit Frontend

#### `streamlit_app.py`

```python
import streamlit as st
import requests

st.title("Resume Scoring Assistant")

jd = st.text_area("Paste Job Description")
resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Submit") and resume and jd:
    files = {"resume": resume}
    data = {"job_description": jd}
    response = requests.post("http://localhost:5000/upload", files=files, data=data)
    res = response.json()
    st.write("Score:", res['score'])
    st.write("Feedback:", res['feedback'])
```

