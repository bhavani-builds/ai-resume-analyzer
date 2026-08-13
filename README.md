# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built with Python that extracts information from resumes, identifies technical skills, analyzes job descriptions, and calculates how well a resume matches a target job.

## 🚀 Project Workflow

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Text Cleaning
    ↓
Skill Extraction
    ↓
Job Description Analysis
    ↓
Resume vs Job Matching
    ↓
Match Score
    ↓
Missing Skills
```

## 📂 Project Structure

```text
ai-resume-analyzer/
│
├── 01_pdf_text_extraction/
│   └── extract_text.py
│
├── 02_text_cleaning/
│   └── clean_text.py
│
├── 03_skill_extraction/
│   └── skill_extractor.py
│
├── 04_job_description/
│   └── job_analyzer.py
│
├── 05_resume_job_matching/
│   └── resume_matcher.py
│
└── README.md
```

## ✨ Features

* 📄 Extract text from PDF resumes
* 🧹 Clean and preprocess resume text
* 🔍 Automatically detect technical skills
* 💼 Analyze job descriptions
* 🔗 Compare resume skills with job requirements
* 📊 Calculate resume-job match percentage
* ❌ Identify missing skills
* 📝 Generate a matching report

## 🛠️ Technologies

* Python
* PyMuPDF
* Regular Expressions
* Pandas
* Scikit-learn
* NumPy
* Matplotlib

## 🔄 Current Progress

```text
01  PDF Text Extraction       ✅
02  Text Cleaning             ✅
03  Skill Extraction          ✅
04  Job Description Analysis  ✅
05  Resume Job Matching       ✅
06  Match Score Visualization ⏳
07  Missing Skills Analysis   ⏳
08  ML Resume Classification  ⏳
09  Resume Dashboard          ⏳
```

## 🎯 Example Output

```text
RESUME vs JOB MATCH

✅ MATCHING SKILLS

✓ Python
✓ C
✓ Machine Learning
✓ MATLAB
✓ Git
✓ GitHub

❌ MISSING SKILLS

✗ SQL
✗ TensorFlow
✗ Docker

Resume Match Score: 75.00%
```

## 🔮 Future Improvements

* AI-based semantic matching
* NLP-based skill extraction
* Resume ranking
* Job recommendation
* Skill gap analysis
* Interactive web dashboard
* Resume improvement suggestions
* Machine Learning based resume classification

## 👨‍💻 Project

Built as a practical Python + AI project to explore **Natural Language Processing, Machine Learning, and automated resume analysis**.
