# small helpers for cleaning text
import re

def clean_text(t: str) -> str:
    t = re.sub(r"\s+"," ",t)
    return t.strip()