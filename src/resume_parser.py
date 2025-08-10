# Simple resume parser: tries PyPDF2 for PDFs, text decode for txt. You can extend with spaCy or resume-specific parsers.
from PyPDF2 import PdfReader
import io


def parse_resume_text(file_bytes: bytes, mime_type: str):
    if mime_type == 'application/pdf' or mime_type.endswith('.pdf'):
        reader = PdfReader(io.BytesIO(file_bytes))
        text = []
        for page in reader.pages:
            text.append(page.extract_text() or "")
        return "\n".join(text)
    else:
        # assume text
        try:
            return file_bytes.decode('utf-8')
        except Exception:
            return file_bytes.decode('latin-1')