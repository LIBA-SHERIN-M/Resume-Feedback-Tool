import streamlit as st
from resume_utils import extract_text_from_pdf, analyze_resume

st.set_page_config(page_title="Resume Feedback Tool", page_icon="🧾")
st.title("🧾 Resume Feedback Tool")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    # Save uploaded file temporarily to read it with pdfplumber
    with open("temp_uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract and analyze resume
    text = extract_text_from_pdf("temp_uploaded_resume.pdf")
    score, feedback = analyze_resume(text)

    st.subheader(f"📊 Resume Score: {score}/3")

    if feedback:
        st.write("### 📝 Suggestions:")
        for f in feedback:
            st.write("- " + f)
    else:
        st.success("✅ Looks great!")
