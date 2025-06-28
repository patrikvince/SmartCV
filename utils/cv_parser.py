import os
from io import StringIO
from pdfminer.high_level import extract_text
import docx

def extract_text_from_pdf(file) -> str:
    text = extract_text(file)
    return text

def extract_text_from_docx(file) -> str:
    doc = docx.Document(file)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)

def extract_cv_text(uploaded_file) -> str:
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file format."
