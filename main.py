from resume_utils import extract_text_from_pdf, analyze_resume  

if __name__ == "__main__":
    resume_path = "data/sample_resume.pdf"
    
    try:
        text = extract_text_from_pdf(resume_path)
        score, suggestions = analyze_resume(text)

        print(f"\n📄 RESUME SCORE: {score}/3")
        if suggestions:
            print("⚠️ Suggestions:")
            for s in suggestions:
                print("-", s)
        else:
            print("✅ Looks great!")
    except FileNotFoundError:
        print(f"❌ File not found: {resume_path}")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

