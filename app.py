import streamlit as st
import pdfplumber
import docx
from utils.analyze_text_spacy import extract_skills_spacy
from utils.levels import LEVEL_KEYWORDS, detect_application_level


st.set_page_config(page_title="SmartCV - Önéletrajz Elemző", layout="centered")

def cv_page():
    st.title("📄 SmartCV – AI Önéletrajz Elemző")
    st.markdown("Tölts fel egy önéletrajzot (`.pdf` vagy `.docx`), és elemezzük együtt!")

    uploaded_file = st.file_uploader("Önéletrajz feltöltése", type=["pdf", "docx"])

    if uploaded_file is not None:
        # PDF vagy DOCX szövegkinyerés (ez maradhat a régi kódod)
        text = ""
        if uploaded_file.type == "application/pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"

        st.success("Dokumentum feldolgozva ✅")

        # Kulcsszavak felismerése spaCy-vel
        soft_skills_found, hard_skills_found, tech_skills_found = extract_skills_spacy(text)
        application_level = detect_application_level(text)

        # Kiírás
        st.markdown(f"**Észlelt jelentkezési szint:** {application_level}")

        st.subheader("🔍 Felismert kulcsszavak")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**🧪 Technológiák:**")
            st.write(tech_skills_found if tech_skills_found else "—")
        with col2:
            st.markdown("**🔧 Hard skillek:**")
            st.write(hard_skills_found if hard_skills_found else "—")
        with col3:
            st.markdown("**🤝 Soft skillek:**")
            st.write(soft_skills_found if soft_skills_found else "—")

        # Session állapotban tárolás
        st.session_state["cv_skills"] = {
            "soft": soft_skills_found,
            "hard": hard_skills_found,
            "tech": tech_skills_found
        }
        st.session_state["cv_application_level"] = application_level


    
def job_posting_page():
    st.title("Álláshirdetés elemzés")
    text = st.text_area("Másold be ide az álláshirdetés szövegét:")

    if st.button("Elemzés indítása"):
        if text.strip() == "":
            st.warning("Kérlek, adj meg szöveget az elemzéshez!")
        else:
            soft_skills_found, hard_skills_found, tech_found = extract_skills_spacy(text)
            
            application_level = detect_application_level(text, LEVEL_KEYWORDS)
            st.markdown(f"**Észlelt jelentkezési szint:** {application_level}")

            st.session_state["job_skills"] = {
                "soft": soft_skills_found,
                "hard": hard_skills_found,
                "tech": tech_found
            }
            st.session_state["job_application_level"] = application_level

            # Megjelenítés
            st.write("### Talált soft skillek:", soft_skills_found)
            st.write("### Talált hard skillek:", hard_skills_found)
            st.write("### Talált technikai skillek:", tech_found)




def evaluation_page():
    st.title("Kiértékelés")

    if "cv_skills" not in st.session_state or "job_skills" not in st.session_state:
        st.warning("Először töltsd ki az önéletrajz és álláshirdetés elemzést.")
        return

    cv = st.session_state["cv_skills"]
    job = st.session_state["job_skills"]

    # Az alkalmazási szintek:
    cv_level = st.session_state.get("application_level", "Junior")
    job_level = st.session_state.get("job_application_level", "Junior")

    total_skills = set(job["soft"] + job["hard"] + job["tech"])
    matched_skills = total_skills.intersection(cv["soft"] + cv["hard"] + cv["tech"])
    missing_skills = total_skills - matched_skills

    match_percent = int(len(matched_skills) / len(total_skills) * 100)

    # Például: ha junior vagy gyakornok, akkor legyen könnyebb a küszöb
    threshold = 60
    if job_level == "Intern / Gyakornok":
        threshold = 40
    elif job_level == "Junior":
        threshold = 50
    elif job_level == "Medior":
        threshold = 60
    elif job_level == "Senior":
        threshold = 75
    elif job_level == "Lead":
        threshold = 80

    st.subheader("Találatok")
    st.markdown(f"**Megfelelés:** {match_percent}%")

    if match_percent >= threshold:
        st.success("Ajánlott jelentkezni! 🎯")
    else:
        st.error("Nem javasolt a jelentkezés 🙁")

    st.subheader("Megtalált skillek")
    st.write(", ".join(matched_skills) if matched_skills else "Nincs egyezés")

    st.subheader("Hiányzó skillek")
    st.write(", ".join(missing_skills) if missing_skills else "Nincs hiányzó skill")



page = st.sidebar.title("📄 SmartCV")
page = st.sidebar.selectbox("Navigáció", ("Önéletrajz elemzés", "Álláshirdetés", "Kiértékelés"))
if page == "Önéletrajz elemzés":
    cv_page()
elif page == "Álláshirdetés":
    job_posting_page()
elif page == "Kiértékelés":
    evaluation_page()
