import os
import json
import re
import google.generativeai as genai

class JobRetriever:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY not set in environment variables")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def retrieve(self, user_text, location=None, job_type=None, top_k=10):
        filters = []
        if location:
            filters.append(f"Location: {location}")
        if job_type and job_type.lower() != "any":
            filters.append(f"Type: {job_type}")
        filters_text = "\n".join(filters) if filters else "No specific filters."

        prompt = f"""
You are a job recommendation AI.
Given the following user resume and preferences, return ONLY a valid JSON array of job postings.

Each job posting object MUST have:
"title", "company", "location", "type", "description", "url"

User resume / skills:
{user_text}

Filters:
{filters_text}

Return exactly {top_k} job postings in this JSON format:
[
  {{
    "title": "Data Scientist",
    "company": "OpenAI",
    "location": "San Francisco, CA",
    "type": "Full-time",
    "description": "Short summary of the role...",
    "url": "https://example.com/job-link"
  }}
]
Do NOT include extra text or explanations.
"""

        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            print("🔍 Raw Gemini Output:\n", response_text)  # Terminal debug

            # Try parsing directly
            try:
                jobs = json.loads(response_text)
            except json.JSONDecodeError:
                # Fallback: extract JSON array using regex
                match = re.search(r"\[\s*{.*}\s*\]", response_text, re.S)
                if not match:
                    raise ValueError(f"❌ No JSON array found in Gemini output:\n{response_text}")
                jobs = json.loads(match.group(0))

            if not isinstance(jobs, list):
                raise ValueError("❌ Gemini did not return a JSON array.")

            return jobs

        except Exception as e:
            print(f"❌ Error fetching jobs: {e}")
            return []
