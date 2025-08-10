import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class LLMWrapper:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY in environment variables")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-pro")

    def fetch_jobs_from_gemini(self, user_text, location="", job_type="Any", max_results=7):
        prompt = f"""
        You are an AI job search assistant.
        Based on the following profile, return {max_results} relevant job recommendations.

        Profile:
        {user_text}

        Preferred location: {location or "Any"}
        Job type: {job_type}

        Output in JSON array format with fields:
        title, company, location, type, description, url.
        """
        response = self.model.generate_content(prompt)
        return response.text



'''import os
#import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env variables if present
load_dotenv()

class LLMWrapper:
    def __init__(self):
        self.gemini_key = os.getenv('GEMINI_API_KEY')
        self.gemini_model = os.getenv('GEMINI_MODEL', 'gemini-pro')  # default to gemini-pro
        self.openai_key = os.getenv('OPENAI_API_KEY')

        # Configure OpenAI if key is present
        """if self.openai_key:
            openai.api_key = self.openai_key"""

        # Configure Gemini if key is present
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key)

    def build_recommendation_prompt(self, user_text: str, job_row: dict) -> str:
        prompt = (
            f"You are a helpful career assistant.\n"
            f"Candidate details: {user_text}.\n\n"
            f"Job posting:\n"
            f"Title: {job_row.get('title')}\n"
            f"Company: {job_row.get('company')}\n"
            f"Location: {job_row.get('location')}\n"
            f"Description: {job_row.get('description')}\n\n"
            "Explain in 2-3 short bullet points why this role is a good fit for the candidate, "
            "and give a short suggested one-line tweak to their resume/skills to improve match. "
            "Keep it concise (~50-100 words). Also produce a match percentage (0-100)."
        )
        return prompt

    def generate(self, prompt: str) -> str:
        """
        Generates a response using Gemini if configured, otherwise OpenAI.
        """
        # Gemini branch
        if self.gemini_key:
            try:
                model = genai.GenerativeModel(self.gemini_model)
                response = model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                return f"⚠️ Gemini API Error: {e}"

        # OpenAI branch
        elif self.openai_key:
            try:
                resp = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=220,
                    temperature=0.35,
                    n=1
                )
                return resp.choices[0].text.strip()
            except Exception as e:
                return f"⚠️ OpenAI API Error: {e}"

        # No API key
        else:
            return "❌ No LLM API configured. Set GEMINI_API_KEY (and optionally GEMINI_MODEL) or OPENAI_API_KEY."
'''