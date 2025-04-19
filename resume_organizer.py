import pdfplumber
from pathlib import Path

def extract_text_with_plumber(file_path: str) -> str:
    """
    Extracts raw resume text with line breaks using pdfplumber.
    Returns a string containing the entire document.
    """
    full_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)
    return "\n".join(full_text)


def rough_chunk_by_headers(text: str, header_keywords=None) -> dict:
    """
    Splits text into rough chunks based on common section headers.
    Returns a dictionary of {section_name: section_text}.
    """
    if header_keywords is None:
        header_keywords = [
            "objective", "summary", "education", "experience", "work history",
            "projects", "skills", "tools", "certifications", "achievements", "interests"
        ]

    sections = {}
    current_section = "other"
    buffer = []

    for line in text.splitlines():
        clean_line = line.strip().lower()
        if any(h in clean_line for h in header_keywords) and len(clean_line.split()) <= 5:
            if buffer:
                sections[current_section] = "\n".join(buffer).strip()
                buffer = []
            current_section = clean_line.title()
        else:
            buffer.append(line)

    if buffer:
        sections[current_section] = "\n".join(buffer).strip()

    return sections
