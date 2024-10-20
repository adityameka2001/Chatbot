import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def load_manual():
    """Loads and returns the contents of the USCIS manual."""
    manual_path = "data/uscis_manual.pdf"
    return extract_text_from_pdf(manual_path)
