import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Study ShareStream",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Study ShareStream")
st.write("Simple Notes + Easy Explanation + Video Learning")

# ----------------------------
# File Paths
# ----------------------------
BASE_DIR = Path(__file__).parent

# Read all PDF files from the root folder
files = list(BASE_DIR.glob("*.pdf"))

if not files:
    st.error("No PDF files found.")
    st.stop()

subjects = sorted([file.stem for file in files])

choice = st.sidebar.selectbox(
    "📘 Select Subject",
    subjects
)

# ----------------------------
# PDF Section
# ----------------------------
pdf_path = BASE_DIR / f"{choice}.pdf"

st.header(choice)

col1, col2 = st.columns([2, 1])

with col1:

    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download Notes",
            data=f,
            file_name=f"{choice}.pdf",
            mime="application/pdf"
        )

    st.info("Download the PDF and study it.")

with col2:

    explanations = {

        "Python": """
Python is a simple and powerful programming language.

It is mainly used for:

• Data Analysis

• Machine Learning

• Artificial Intelligence

• Web Development

• Automation
""",

        "DBMS": """
DBMS stands for Database Management System.

Examples:

• MySQL

• Oracle

• SQL Server

• PostgreSQL
""",

        "BigData": """
Big Data means very large amounts of data.

5 V's of Big Data:

• Volume

• Velocity

• Variety

• Veracity

• Value
"""
    }

    st.subheader("📖 Easy Explanation")
    st.write(explanations.get(choice, "Explanation Coming Soon."))

    st.subheader("📝 Important Points")

    st.markdown("""
- Read definitions
- Learn examples
- Practice MCQs
- Revise regularly
""")

    st.subheader("🎯 Exam Tips")

    st.markdown("""
- ✔ Learn diagrams
- ✔ Practice previous year papers
- ✔ Understand concepts instead of memorizing
""")

# ----------------------------
# Video Section
# ----------------------------
st.divider()
st.header("🎥 Video Explanation")

video_file = BASE_DIR / "video.csv"

if video_file.exists():

    video_df = pd.read_csv(video_file)

    row = video_df[video_df["Subject"] == choice]

    if not row.empty:
        st.video(row.iloc[0]["Video"])
    else:
        st.warning("No video available for this subject.")

else:
    st.error("video.csv not found.")

# ----------------------------
# Search
# ----------------------------
st.divider()

st.header("🔍 Search Study Material")

search = st.text_input("Enter Subject Name")

if search:

    result = [s for s in subjects if search.lower() in s.lower()]

    if result:
        st.success("Available Subjects:")
        st.write(result)
    else:
        st.error("No subject found.")
st.set_page_config()
# =========================
# PROFESSIONAL UI SECTION
# Paste this below st.set_page_config()
# =========================

import os
import streamlit as st

# ---------- SIDEBAR ----------
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

# ---------- HOME ----------
if page == "🏠 Home":

    st.title("📚 Study ShareStream")

    st.markdown("""
### Your One-Stop Learning Platform

Welcome to **Study ShareStream**.

Access quality study materials and video lectures for:

- 🐍 Python
- 💾 DBMS
- 📊 Big Data

Download PDFs and learn anytime, anywhere.
""")

    st.divider()

    # Dashboard
    pdf_count = 0

    folder = "study_material"

    if os.path.exists(folder):
        pdf_count = len([f for f in os.listdir(folder) if f.endswith(".pdf")])

    col1, col2, col3 = st.columns(3)

    col1.metric("📄 PDFs", pdf_count)
    col2.metric("🎥 Videos", 3)
    col3.metric("📚 Subjects", 3)

    st.divider()

    st.subheader("📚 Available Subjects")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("🐍 Python")

    with c2:
        st.info("📊 Big Data")

    with c3:
        st.info("💾 DBMS")

    st.divider()

    st.subheader("🔍 Search Study Material")

    search = st.text_input("Search PDF")

    if os.path.exists(folder):

        files = [f for f in os.listdir(folder) if f.endswith(".pdf")]

        if search:

            result = False

            for file in files:

                if search.lower() in file.lower():

                    st.success(file)

                    result = True

            if not result:

                st.error("No PDF Found.")

# ---------- STUDY MATERIAL ----------
elif page == "📄 Study Material":

    st.title("📄 Study Materials")

    folder = "study_material"

    if os.path.exists(folder):

        files = [f for f in os.listdir(folder) if f.endswith(".pdf")]

        if len(files) == 0:
            st.warning("No PDF available.")

        for file in files:

            filepath = os.path.join(folder, file)

            size = os.path.getsize(filepath) / 1024

            with st.expander(f"📄 {file}"):

                st.write(f"📦 File Size : {size:.2f} KB")

                with open(filepath, "rb") as pdf:

                    st.download_button(
                        "📥 Download PDF",
                        pdf,
                        file_name=file,
                        mime="application/pdf"
                    )

    else:

        st.error("study_material folder not found.")

# ---------- VIDEOS ----------
elif page == "🎥 Video Lectures":

    st.title("🎥 Video Lectures")

    st.video("https://www.youtube.com/watch?v=rfscVS0vtbw")

    st.video("https://www.youtube.com/watch?v=kBdlM6hNDAE")

    st.video("https://www.youtube.com/watch?v=HXV3zeQKqGY")

# ---------- ABOUT ----------
elif page == "👨‍💻 About":

    st.title("👨‍💻 About Study ShareStream")

    st.write("""
### 📚 Study ShareStream

Study ShareStream is a free learning platform developed using **Python** and **Streamlit**.

### 🚀 Features

✅ Download Study Material

✅ Video Lectures

✅ Search PDFs

✅ Simple User Interface

### 🛠 Technologies Used

- Python
- Streamlit
- Pandas

### 👨‍💻 Developed By

**Dhruv Panchal**

### 🎯 Purpose

To provide students with easy access to study materials from one place.
""")

# ---------- FOOTER ----------
st.divider()

st.markdown(
"""
<center>

Made with ❤️ by <b>Dhruv Panchal</b>

<br>

© 2026 Study ShareStream

</center>
""",
unsafe_allow_html=True
)
