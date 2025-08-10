# AI-Job-Recommender-System-using-LangChain-Gemini


An AI-powered job recommendation system built with **Streamlit**, **LangChain**, and **Google Gemini API**.
Upload your resume or type in your skills, and get **personalized job or internship recommendations** along with AI-generated explanations.

<img width="1365" height="634" alt="image" src="https://github.com/user-attachments/assets/1b5f604c-257c-4430-ac13-f02275fb5cfc" />


---

## ✨ Features

* 📄 **Resume Parsing** — Upload your PDF/TXT resume and automatically extract key skills, experience, and education.
* 🔍 **AI-Powered Job Search** — Uses Retrieval-Augmented Generation (RAG) with Gemini to find relevant jobs.
* 🧠 **Context-Aware Recommendations** — Matches jobs based on your profile, skills, and preferences.
* 📍 **Location & Job Type Filters** — Choose preferred location and job type (Full-time, Part-time, Internship, Contract).
* 💬 **Natural Language Explanations** — AI explains *why* each job is a good fit for you.
* 🖥 **Interactive Web UI** — Built with Streamlit for a clean, responsive interface.

---

## 🛠 Tech Stack

* **Frontend/UI** — [Streamlit](https://streamlit.io/)
* **AI/LLM** — [LangChain](https://www.langchain.com/) + [Google Gemini API](https://ai.google.dev/)
* **Resume Parsing** — Custom parser for PDF/TXT files
* **Backend Retrieval** — JobRetriever (custom RAG pipeline)
* **Language Models** — LLMWrapper abstraction

---

## 📂 Project Structure

```
.
├── src/
│   ├── retriever.py        # Retrieves jobs from Gemini
│   ├── resume_parser.py    # Extracts text from resumes
│   ├── llm_wrapper.py      # Handles prompt building & AI calls
├── app.py                  # Streamlit app entry point
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-job-recommender.git
cd ai-job-recommender
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📌 Usage

1. **Upload Resume** — Drag and drop your PDF/TXT resume.
2. **Enter Skills** — Optionally type your skills manually.
3. **Set Preferences** — Choose location, job type, and number of recommendations.
4. **Find Jobs** — Click "Find me jobs" and let the AI work!
5. **Review Results** — Browse job cards with AI-generated explanations.

---

## 📷 Example Output

**Resume Preview:**

```
Dhruv Mehta
Data Analysis & Science
Summary:
Data professional with hands-on experience in SQL, Python, Power BI...
```

**Job Recommendation Card:**

> **1. Data Analyst — Google**
> 📍 Location: Remote | 💼 Type: Full-time
> 📝 Description: Responsible for data analysis, dashboard creation...
> 💡 *AI says:* "Your strong skills in SQL and Power BI match this role’s requirements..."

---

## 📌 To-Do / Future Improvements

* 🌐 Integrate with real-time job APIs (LinkedIn, Google Jobs)
* 📊 Add visual skill-job match scoring
* 📬 Email job recommendations
* 🔄 Multi-resume comparison
