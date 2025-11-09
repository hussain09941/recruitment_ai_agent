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

        else:
            return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

    # Clean extracted text
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
