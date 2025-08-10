import streamlit as st
from src.retriever import JobRetriever

st.set_page_config(page_title="AI Job Recommender", layout="wide")

st.title("💼 AI Job Recommender")

# Sidebar inputs
st.sidebar.header("Upload Resume")
uploaded_resume = st.sidebar.file_uploader(
    "Upload your resume (PDF or TXT)", type=["pdf", "txt"]
)
skills = st.sidebar.text_input("List your skills (comma separated)", value="")
location = st.sidebar.text_input(
    "Preferred location (city/country) — leave blank for remote/any", value=""
)
job_type = st.sidebar.selectbox("Job type", ["Any", "Full-time", "Part-time", "Contract"])
max_recommendations = st.sidebar.slider("Max recommendations", 1, 10, 5)

retriever = JobRetriever()

if st.sidebar.button("Find me jobs"):
    if not uploaded_resume:
        st.error("Please upload your resume first.")
    else:
        try:
            # Read resume text
            resume_text = uploaded_resume.read().decode("utf-8", errors="ignore")

         

            # --- Show loader while searching ---
            with st.spinner("🔍 Searching and generating recommendations..."):
                jobs = retriever.retrieve(
                    resume_text, location, job_type, max_recommendations
                )

            # --- Show jobs ---
            if not jobs:
                st.warning("No jobs found for your profile.")
            else:
                st.subheader("✅ Recommended Jobs for You")
                for job in jobs:
                    with st.container():
                        st.markdown(f"### [{job['title']}]({job['url']})")
                        st.markdown(f"**Company:** {job['company']}")
                        st.markdown(f"**Location:** {job['location']}")
                        st.markdown(f"**Type:** {job['type']}")
                        st.markdown(f"**Description:** {job['description']}")
                        st.markdown("---")

        except Exception as e:
            st.error(f"Unexpected error: {e}")
