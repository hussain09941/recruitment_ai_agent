import docx2txt
import PyPDF2
import re

def extract_text_from_resume(file_path):
    text = ""

    try:
        if file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""

        elif file_path.lower().endswith('.docx'):
            text = docx2txt.process(file_path) or ""

        elif file_path.lower().endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()

    except Exception as e:
        print(f"[ERROR] Reading resume failed:", e)
        return ""

    # Cleanup
    text = re.sub(r"\s+", " ", text)
    return text.strip()


import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_job(job_skills, resume_text):
    if not job_skills or not resume_text:
        return 0.0

    job_skills = job_skills.lower()
    resume_text = resume_text.lower()

    # Clean text
    job_skills = re.sub(r"[^a-zA-Z0-9\s]", " ", job_skills)
    resume_text = re.sub(r"[^a-zA-Z0-9\s]", " ", resume_text)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform([job_skills, resume_text])

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)
