import pdfplumber  # PDF text extractor
import spacy       # Resume analyzer
import re          # For phone number matching

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Function to analyze resume content
def analyze_resume(text):
    doc = nlp(text)

    # Count words
    word_count = len([token.text for token in doc if token.is_alpha])

    # Detect email
    has_email = any(token.like_email for token in doc)

    # Detect phone using regex
    phone_pattern = r"(\+?\d{1,3}[\s\-]?)?\(?\d{3,5}\)?[\s\-]?\d{3}[\s\-]?\d{3,4}"
    has_phone = re.search(phone_pattern, text) is not None

    feedback = []
    score = 0

    if word_count < 150:
        feedback.append("Your resume is too short.")
    else:
        score += 1

    if has_email:
        score += 1
    else:
        feedback.append("No email found.")

    if has_phone:
        score += 1
    else:
        feedback.append("No phone number found.")

    return score, feedback
