# 🤖 AI-Based Job Recommendation System

> **An AI-powered recruitment platform that intelligently matches candidates with suitable job opportunities using NLP, TF-IDF, and Cosine Similarity.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Web%20Framework-green?logo=django)](https://www.djangoproject.com/)
[![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Cosine%20Similarity-orange)](https://scikit-learn.org/)
[![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)](https://www.sqlite.org/)
[![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-yellow)](https://developer.mozilla.org/)

---

## 🌟 Project Overview

The **AI-Based Job Recommendation System** is a full-stack web application designed to automate the recruitment and job-matching process.

The system uses **Natural Language Processing (NLP)** to compare candidate resumes with job descriptions and calculates a **similarity score** using **TF-IDF and Cosine Similarity**.

This enables companies to automatically identify candidates whose resumes are most closely aligned with their job requirements.

---

## 🚀 Key Features

| 👤 Candidate              | 🏢 Company                | 🤖 AI Matching     |
| ------------------------- | ------------------------- | ------------------ |
| Secure Registration/Login | Secure Registration/Login | TF-IDF             |
| Candidate Profile         | Post Jobs                 | Cosine Similarity  |
| Resume Information        | Manage Jobs               | Matching Score     |
| Browse Jobs               | View Candidates           | Candidate Ranking  |
| Job Recommendations       | Find Suitable Candidates  | Automated Matching |

---

## 🧠 AI-Powered Recommendation

### 🔥 Resume → Job Matching Pipeline

```text
📄 Candidate Resume
        ↓
🧹 Text Preprocessing
        ↓
🔢 TF-IDF Vectorization
        ↓
💼 Job Description
        ↓
🔢 TF-IDF Vectorization
        ↓
📐 Cosine Similarity
        ↓
📊 Matching Score
        ↓
🏆 Candidate Ranking
```

### 📌 TF-IDF

**TF-IDF (Term Frequency-Inverse Document Frequency)** converts resume and job-description text into numerical vectors based on the importance of words.

### 📌 Cosine Similarity

The system measures the similarity between the resume and job description using:

$$
Cosine\ Similarity(A,B)=
\frac{A\cdot B}{||A||\,||B||}
$$

A **higher similarity score** indicates greater textual similarity between the candidate's resume and the job description.

---

## 💡 Example

### 💼 Job Description

```text
Python Django Developer

Required Skills:
Python, Django, SQL, REST API, Git
```

### 👨‍💻 Candidate Resume

```text
Python Developer experienced in Django,
SQL, REST API development and Git.
```

### 🤖 System Output

```text
Candidate A → 86% Match
Candidate B → 71% Match
Candidate C → 54% Match
```

The system uses these scores to **rank candidates according to resume-job textual similarity**.

---

## 🛠️ Technology Stack

### 🎨 Frontend

* **HTML5**
* **CSS3**
* **JavaScript**

### ⚙️ Backend

* **Python**
* **Django**

### 🧠 Artificial Intelligence

* **Natural Language Processing (NLP)**
* **TF-IDF Vectorization**
* **Cosine Similarity**

### 🗄️ Database

* **SQLite**

---

## 🔐 User Roles

### 👨‍💻 Candidate

* Register and Login
* Manage candidate profile
* Provide resume information
* Browse available jobs
* Receive relevant job recommendations

### 🏢 Company

* Register and Login
* Create job vacancies
* Manage job postings
* Automatically find suitable candidates
* View candidate matching scores

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/hussain09941/recruitment_ai_agent.git
```

### 2️⃣ Navigate to Project

```bash
cd recruitment_ai_agent
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django scikit-learn
```

---

## 🗄️ Database Configuration

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Project

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 📊 Core Matching Logic

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [resume_text, job_description]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

similarity = cosine_similarity(
    vectors[0:1],
    vectors[1:2]
)

score = similarity[0][0]
```

The calculated similarity score is used for **candidate-job matching and ranking**.

---

## 🎯 Project Objectives

* 🚀 **Automate** the recruitment screening process
* 🤖 Apply **NLP techniques** to recruitment
* 📄 Compare resumes with job descriptions automatically
* 🏆 Identify highly matched candidates
* 🔎 Help candidates discover relevant jobs
* ⚡ Reduce manual candidate screening effort
* 🌐 Build a complete **AI-enabled Django web application**

---

## 🔮 Future Enhancements

* 📄 Automatic PDF/DOCX resume parsing
* 🧠 BERT/Transformer-based semantic matching
* 🔍 Automatic skill extraction
* 📊 Recruiter analytics dashboard
* 📧 Email notifications
* 🎯 Personalized job recommendations
* 🗄️ PostgreSQL/MySQL integration
* ☁️ Cloud deployment

---

## 👨‍💻 Author

### **Jabir Hussain**

**MCA | NIT Patna**

🔗 **GitHub:**
https://github.com/hussain09941

---

## 📌 Project Highlights

> ⭐ **Full-Stack Django Application**
> ⭐ **AI-Based Resume–Job Matching**
> ⭐ **NLP with TF-IDF**
> ⭐ **Cosine Similarity-Based Ranking**
> ⭐ **Candidate & Company Authentication**
> ⭐ **Automated Candidate Recommendation**

---

## 📄 License

This project is developed for **educational and academic purposes**.
