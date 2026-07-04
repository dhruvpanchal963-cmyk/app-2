import streamlit as st
import pandas as pd
from pathlib import Path

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Study ShareStream",
    page_icon="📚",
    layout="wide"
)

# -------------------------------
# PATHS
# -------------------------------
BASE_DIR = Path(__file__).parent

# Read all PDFs from current folder
pdf_files = sorted(BASE_DIR.glob("*.pdf"))
subjects = [pdf.stem for pdf in pdf_files]

# -------------------------------
# SIDEBAR
# -------------------------------
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

# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    st.title("📚 Study ShareStream")

    st.write("### One Place for Notes, Videos & Exam Preparation")

    col1, col2, col3 = st.columns(3)

    col1.metric("📄 PDFs", len(subjects))
    col2.metric("🎥 Videos", len(subjects))
    col3.metric("📚 Subjects", len(subjects))

    st.divider()

    if len(subjects) == 0:
        st.error("No PDF files found.")
        st.stop()

    choice = st.selectbox(
        "📘 Select Subject",
        subjects
    )

    pdf_path = BASE_DIR / f"{choice}.pdf"

    if pdf_path.exists():

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                "📥 Download Notes",
                pdf,
                file_name=pdf_path.name,
                mime="application/pdf"
            )

    explanations = {

        "Python": """
Python is an easy programming language.

Topics:
• Variables
• Loops
• Functions
• OOP
• File Handling
""",

        "BDMS": """
DBMS stands for Database Management System.

Topics:
• Database
• ER Diagram
• SQL
• Normalization
""",

        "Big data": """
Big Data means extremely large datasets.

5 V's

• Volume
• Velocity
• Variety
• Veracity
• Value
"""
    }

    st.subheader("📖 Easy Explanation")

    st.write(
        explanations.get(
            choice,
            "Explanation Coming Soon."
        )
    )

    st.subheader("📝 Exam Tips")

    st.markdown("""
- ✔ Read definitions
- ✔ Practice diagrams
- ✔ Solve previous year papers
- ✔ Revise regularly
""")
    # =====================================================
# STUDY MATERIAL PAGE
# =====================================================

elif page == "📄 Study Material":

    st.title("📄 Study Materials")

    if len(pdf_files) == 0:

        st.warning("No PDF files found.")

    else:

        for pdf in pdf_files:

            with st.expander(f"📄 {pdf.stem}"):

                st.write(f"**File Name:** {pdf.name}")

                size = pdf.stat().st_size / 1024

                st.write(f"**File Size:** {size:.2f} KB")

                with open(pdf, "rb") as f:

                    st.download_button(
                        label=f"📥 Download {pdf.stem}",
                        data=f,
                        file_name=pdf.name,
                        mime="application/pdf",
                        key=pdf.stem
                    )

    st.divider()

    st.subheader("🔍 Search Study Material")

    search = st.text_input("Enter Subject Name")

    if search:

        result = [
            s for s in subjects
            if search.lower() in s.lower()
        ]

        if result:

            st.success("Available Subjects")

            for subject in result:
                st.write(f"✅ {subject}")

        else:

            st.error("No Subject Found")
            # =====================================================
# VIDEO LECTURES PAGE
# =====================================================

    video_file = BASE_DIR / "video.csv"

    if video_file.exists():

        try:

            video_df = pd.read_csv(video_file)

            # Remove extra spaces from column names
            video_df.columns = video_df.columns.str.strip()

            # Check required columns
            if "Subject" not in video_df.columns or "Video" not in video_df.columns:
                st.error("video.csv must contain 'Subject' and 'Video' columns.")
                st.stop()

            # Remove spaces from subject names
            video_df["Subject"] = video_df["Subject"].astype(str).str.strip()

            st.subheader("Select a Subject")

            subject = st.selectbox(
                "📘 Subject",
                video_df["Subject"].tolist()
            )

            row = video_df[video_df["Subject"] == subject]

            if not row.empty:

                st.success(f"Now Playing: {subject}")

                st.video(row.iloc[0]["Video"])

            else:

                st.warning("No video available for this subject.")

        except Exception as e:

            st.error(f"Error reading video.csv: {e}")

    else:

        st.error("video.csv not found in the project folder.")
        # =====================================================
# VIDEO LECTURES PAGE
# =====================================================

elif page == "🎥 Video Lectures":

    st.title("🎥 Video Lectures")

    video_file = BASE_DIR / "video.csv"

    if video_file.exists():

        try:

            video_df = pd.read_csv(video_file)

            # Remove extra spaces from column names
            video_df.columns = video_df.columns.str.strip()

            # Check required columns
            if "Subject" not in video_df.columns or "Video" not in video_df.columns:
                st.error("video.csv must contain 'Subject' and 'Video' columns.")
                st.stop()

            # Remove spaces from subject names
            video_df["Subject"] = video_df["Subject"].astype(str).str.strip()

            st.subheader("Select a Subject")

            subject = st.selectbox(
                "📘 Subject",
                video_df["Subject"].tolist()
            )

            row = video_df[video_df["Subject"] == subject]

            if not row.empty:

                st.success(f"Now Playing: {subject}")

                st.video(row.iloc[0]["Video"])

            else:

                st.warning("No video available for this subject.")

        except Exception as e:

            st.error(f"Error reading video.csv: {e}")

    else:
        
        st.error("video.csv not found in the project folder.")
        # =====================================================
# ABOUT PAGE
# =====================================================

elif page == "👨‍💻 About":

    st.title("👨‍💻 About Study ShareStream")

    st.markdown("""
# 📚 Study ShareStream

Study ShareStream is an educational platform developed using **Python** and **Streamlit**.

## 🚀 Features

✅ Download Study PDFs

✅ Watch Video Lectures

✅ Search Subjects

✅ Clean User Interface

---

## 📚 Subjects

- 🐍 Python
- 💾 BDMS
- 📊 Big Data

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas

---

## 👨‍💻 Developed By

**Dhruv Panchal**

---

## 🎯 Purpose

To help students access notes and videos from one place.
""")

    st.divider()

    st.subheader("📞 Contact")

    st.write("📧 Email : dhruvpanchal963@gmail.com")

    st.write("💻 GitHub : https://github.com/")

    st.write("🔗 LinkedIn : https://linkedin.com/")
st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <h3>📚 Study ShareStream</h3>
        <p>Made with ❤️ using Streamlit</p>
        <p><b>Developed by Dhruv Panchal</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
