import streamlit as st
import pandas as pd
from pathlib import Path
import os

st.set_page_config(
    page_title="Study ShareStream",
    page_icon="📚",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

st.sidebar.title("📚 Study ShareStream")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Study Material",
        "🎥 Video Lectures",
        "👨‍💻 About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Welcome!")

pdf_files = sorted(BASE_DIR.glob("*.pdf"))
subjects = [pdf.stem for pdf in pdf_files]

if page == "🏠 Home":

    st.title("📚 Study ShareStream")

    st.write("### Learn Smarter with Notes & Video Lectures")

    col1, col2, col3 = st.columns(3)

    col1.metric("📄 PDFs", len(subjects))
    col2.metric("🎥 Videos", len(subjects))
    col3.metric("📚 Subjects", len(subjects))

    st.divider()

    choice = st.selectbox("📘 Select Subject", subjects)

    pdf_path = BASE_DIR / f"{choice}.pdf"

    if pdf_path.exists():

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                "📥 Download Notes",
                pdf,
                file_name=f"{choice}.pdf",
                mime="application/pdf"
            )

    explanations = {

        "Python": """
Python is a simple programming language.

• Easy to Learn

• Web Development

• AI & Machine Learning

• Data Analysis
""",

        "BDMS": """
Database Management System

• MySQL

• Oracle

• SQL

• PostgreSQL
""",

        "Big data": """
Big Data refers to huge amounts of data.

5 V's

• Volume

• Velocity

• Variety

• Veracity

• Value
"""
    }

    st.subheader("📖 Easy Explanation")

    st.write(explanations.get(choice, "Explanation Coming Soon."))

    st.subheader("📝 Exam Tips")

    st.markdown("""
- ✔ Read definitions
- ✔ Practice diagrams
- ✔ Revise regularly
- ✔ Solve Previous Papers
""")
    if page == "🎥 Video Lectures":

    st.title("🎥 Video Lectures")

    video_file = BASE_DIR / "video.csv"

    if video_file.exists():

        video_df = pd.read_csv(video_file)

        video_df.columns = video_df.columns.str.strip()

        st.write("Available Subjects:")
        st.write(video_df["Subject"])

        subject = st.selectbox(
            "Choose Subject",
            video_df["Subject"]
        )

        row = video_df[video_df["Subject"] == subject]

        if not row.empty:

            st.video(row.iloc[0]["Video"])

        else:

            st.warning("No Video Found.")

    else:

        st.error("video.csv not found.")




if page == "📄 Study Material":

    st.title("📄 Study Material")

    for pdf in pdf_files:

        with st.expander(pdf.name):

            st.write(f"Subject : {pdf.stem}")

            with open(pdf, "rb") as f:

                st.download_button(
                    "📥 Download PDF",
                    f,
                    file_name=pdf.name,
                    mime="application/pdf"
                )



    st.divider()

    st.subheader("🔍 Search Study Material")

    search = st.text_input("Enter Subject Name")

    if search:

        result = [s for s in subjects if search.lower() in s.lower()]

        if result:

            st.success(result)

        else:

            st.error("No Subject Found")
            if page == "👨‍💻 About":

    st.title("👨‍💻 About")

    st.markdown("""
## 📚 Study ShareStream

Study ShareStream is a free learning platform developed using Python and Streamlit.

### 🚀 Features

✅ Download Study Notes

✅ Watch Video Lectures

✅ Search Subjects

✅ Clean & Responsive UI

### 📚 Subjects

- Python

- BDMS

- Big data

### 🛠 Technologies

- Python

- Streamlit

- Pandas

### 👨‍💻 Developer

Dhruv Panchal

### 🎯 Purpose

To help students learn quickly with notes and videos.
""")

st.divider()

st.markdown(
"""
<center>

Made with ❤️ by <b>Dhruv Panchal</b>

© 2026 Study ShareStream

</center>
""",
unsafe_allow_html=True
)
