# 📄 AI Resume Screening App — NLP-Powered Candidate Ranking

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![NLP](https://img.shields.io/badge/NLP-TF--IDF_+_Cosine-green?style=flat-square)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square&logo=streamlit)
![Django](https://img.shields.io/badge/Backend-Django-darkgreen?style=flat-square&logo=django)
![Status](https://img.shields.io/badge/Stage-Complete-green?style=flat-square)

---

👤 **Author:** [Ashutosh — GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/)
💼 **Portfolio:** [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/)

---

## 📋 Table of Contents

- [What This Does](#-what-this-does)
- [Real Numbers](#-real-numbers)
- [Architecture](#-architecture)
- [What I Built](#-what-i-built)
- [Scoring System](#-scoring-system)
- [Quick Start](#-quick-start)
- [Environment Variables](#-environment-variables)
- [Tech Stack](#-tech-stack)
- [Project Status](#-project-status)
- [Links](#-links)
- [Author](#-author)

---

## 🧠 What This Does

An automated resume screening system that parses candidate
PDF resumes, compares them against a job description using
NLP, ranks all candidates by match score, and identifies
skill gaps — replacing manual HR screening with data.

1. **Problem** — HR teams manually reading 100+ resumes
   per job posting is slow, biased, and inconsistent.
   Good candidates get missed. Unqualified ones slip through.
2. **Solution** — Upload a job description + multiple
   resumes → NLP pipeline scores and ranks every candidate
   by match percentage → skill gap report generated
   per candidate automatically.
3. **For** — NLP / Data Analyst / Python Developer hiring
   managers looking for real NLP pipeline + automation proof

---

## 📊 Real Numbers

| Metric | Value |
|--------|-------|
| Input | Job Description + Multiple PDF Resumes |
| Matching Method | TF-IDF + Cosine Similarity |
| Output | Ranked candidate list with match % |
| Skill Detection | Automated gap analysis per candidate |
| Backend | Django REST API |
| Frontend | Streamlit interactive dashboard |
| Resume Format | PDF (PyPDF2 extraction) |

---

## 🏗️ Architecture
```
HR Input
  ├── Job Description (text paste or .txt upload)
  └── Resume PDFs (bulk upload — multiple files)
        ↓
Resume Parser
  → PyPDF2 extracts raw text from each PDF
  → Handles multi-page resumes
  → Cleans extracted text (encoding, whitespace)
        ↓
Cosine Similarity Scoring
  → Each resume vector vs JD vector
  → Similarity score: 0.0 to 1.0
  → Converted to match percentage
        ↓
Skill Gap Analysis
  → Extract required skills from JD
  → Check presence in each resume
  → Missing skills flagged per candidate
        ↓
Streamlit Dashboard
  → Ranked table with scores
  → Per-candidate skill gap report
  → Download results as CSV

```

---

## 🔨 What I Built

### 1. Resume Parser
- PyPDF2 extracts raw text from uploaded PDF resumes
- Handles single-page and multi-page resumes
- Cleans extracted text — encoding issues, extra whitespace
- Processes multiple resumes in one batch upload
- Returns structured text per candidate

### 2. NLP Preprocessing Pipeline
- Lowercasing and punctuation removal
- NLTK English stop word removal
- WordNet lemmatization for root word normalization
- Tokenization for term frequency analysis
- Handles both JD and resume text through same pipeline
- 
### 3. Skill Gap Analysis
- Extracts required skills list from JD automatically
- Checks each resume for presence of required skills
- Returns per-candidate missing skills list
- Categorizes gaps: Critical Missing / Nice-to-Have Missing
- Helps HR give structured feedback to candidates

### 4. Candidate Ranking System
- Sorts all uploaded resumes by match percentage
- Top candidates flagged with green recommendation
- Below-threshold candidates flagged for review
- Tie-breaking by skill gap count
- Results exportable as CSV for HR records

### 5. Streamlit Dashboard
- Job description input text area
- Bulk PDF resume uploader
- Ranked candidates table with color-coded scores
- Expandable per-candidate skill gap detail
- Download ranked results as CSV
- Clean HR-friendly interface — no technical knowledge needed

---

## 📐 Scoring System

| Score Range | Label | Recommendation |
|-------------|-------|---------------|
| 80% – 100% | 🟢 Strong Match | Shortlist immediately |
| 60% – 79% | 🟡 Good Match | Review and consider |
| 40% – 59% | 🟠 Partial Match | Review with caution |
| Below 40% | 🔴 Weak Match | Likely not suitable |

---

## ⚡ Quick Start

**Prerequisites:** Python 3.11+, Git
```bash
# 1. Clone the repo
git clone https://github.com/Ashutosh-AIBOT/ai-resume-screening-app.git
cd ai-resume-screening-app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download NLTK data
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"

# 5. Set up Django database
python manage.py migrate

# 6a. Run Streamlit app (standalone mode)
streamlit run app.py

# 6b. OR run Django backend
python manage.py runserver

# 7. Open browser
# Streamlit: http://localhost:8501
# Django admin: http://localhost:8000/admin
```

---

## 🔑 Environment Variables

| Variable | What It Is | Example |
|----------|-----------|---------|
| `SECRET_KEY` | Django secret key | Random 50-char string |
| `DEBUG` | Django debug mode | `True` for dev |
| `DATABASE_URL` | Database connection | `sqlite:///db.sqlite3` |
| `APP_ENV` | Environment flag | `development` |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| NLTK | Stop words, lemmatization, tokenization |
| PyPDF2 | PDF text extraction |
| Pandas | Data manipulation and ranking |
| Streamlit | Interactive HR dashboard |
| SQLite / PostgreSQL | Candidate and job data storage |
| Git | Version control |

---

## 📁 Repository Structure
```
ai-resume-screening-app/
│
├── app.py                          # Main Streamlit dashboard
│
├── screening/
│   ├── __init__.py
│   ├── parser.py                   # PyPDF2 resume text extraction
│   ├── preprocessor.py             # NLP cleaning pipeline
│   ├── scorer.py                   # Cosine similarity scoring
│   ├── skill_gap.py                # Skill gap detection
│   └── ranker.py                   # Candidate ranking logic
│
├── requirements.txt
└── README.md
```

---

## 📊 Project Status

| Deliverable | Status |
|-------------|--------|
| Resume PDF Parser | ✅ Complete |
| Skill Gap Analysis | ✅ Complete |
| Candidate Ranking System | ✅ Complete |
| Streamlit Dashboard | ✅ Complete |

---

## 🌐 Links

| Resource | URL |
|----------|-----|
| 💼 Portfolio | [ashutosh-portfolio-kappa.vercel.app](https://ashutosh-portfolio-kappa.vercel.app/) |
| 🐙 GitHub | [github.com/Ashutosh-AIBOT](https://github.com/Ashutosh-AIBOT) |
| 🔗 LinkedIn | [linkedin.com/in/ashutosh1975271](https://www.linkedin.com/in/ashutosh1975271/) |

---

## 👤 Author

**Ashutosh**
B.Tech Electronics Engineering · CGPA 7.5 · Batch 2026
[GitHub](https://github.com/Ashutosh-AIBOT) · [LinkedIn](https://www.linkedin.com/in/ashutosh1975271/) · [Portfolio](https://ashutosh-portfolio-kappa.vercel.app/)

---

> *"100 resumes. 10 minutes. Zero bias.*
> *Let the math decide who gets the interview."*
>
> — Ashutosh, building this from zero.
```
🌐 ashutosh-portfolio-kappa.vercel.app
