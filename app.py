from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file_fr = current_dir / "assets" / "CV_GROSPERRIN.pdf"
resume_file_en = current_dir / "assets" / "Resume_GROSPERRIN.pdf"
profile_pic = current_dir / "assets" / "pdp.png"

def load_lottieurl(url):
    r = requests.get(url, verify=False)
    if r.status_code != 200:
        return None
    return r.json()


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Mathis Grosperrin | Data Scientist"
PAGE_ICON = "assets/mg_logo.PNG"
NAME = "Hi, I'm Mathis Grosperrin :wave:"
DESCRIPTION = """
Data & AI Engineer from France, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "mathgpn@gmail.com"
# SOCIAL_MEDIA = {
#     "My LinkedIn": "https://www.linkedin.com/in/mathis-grosperrin/?originalSubdomain=fr",
#     "My GitHub": "https://github.com/MathGpn",
# }
PROJECTS = {
    "🏆 Data Battle": "https://cytech.cyu.fr/lecole-cy-tech/actualites/deux-equipes-tekiennes-en-tete-du-data-battle-nouvelle-aquitaine",
    "🏆 Winner of the local basketball cup": "https://www.larepubliquedespyrenees.fr/pyrenees-atlantiques/pau/basket-coupe-des-pyrenees-atlantiques-triomphe-de-2mbs-la-coupe-reste-dans-le-soubestre-19639581.php",
    ":basketball: Basketball stats": "https://mr-stats.frenchbasketballscouting.fr/joueur/grosperrin-mathis-11152",    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file_fr, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(resume_file_en, "rb") as pdf_file2:
    PDFbyte2 = pdf_file2.read()
profile_pic = Image.open(profile_pic)

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


# --- HERO SECTION ---
col1, col2 = st.columns([1, 1.5])
with col1:
    st.image(profile_pic, width=230)
    st.write("📫", EMAIL)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger mon CV (FR)",
        data=PDFbyte,
        file_name=resume_file_fr.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label=" 📄 Download Resume (EN)",
        data=PDFbyte2,
        file_name=resume_file_en.name,
        mime="application/octet-stream",
    )


# --- SOCIAL LINKS ---
col5, col6 = st.columns([1, 1])
with col5:
    st.image("assets/logo_link.PNG", width=45)
    st.write("[My LinkedIn](https://www.linkedin.com/in/mathis-grosperrin/?originalSubdomain=fr)")
with col6:
    st.image("assets/github_ok.PNG", width=37)
    st.write("[My GitHub](https://github.com/MathGpn)")
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
with st.container():
    st.write("---")
    st.header("Hard Skills")
    st.write("##")
    st.write(
            """
        - 👩‍💻 Programming : Python (Streamlit, FastAPI, Flask)
        - 📚 Machine Learning (Regression, Classification, Clustering)
        - :brain: Deep Learning (GenAI, Multimodal models, Reinforcement Learning)
        - 📊 Data Visualization (PowerBI)
        - 🗄️ Databases (MongoDB, MySQL)
        - :1234: Mathematics (Statistics and Probability, Optimization)
        - :male-office-worker: Project management: Team management, Agile methodology, DevOps
        - :computer: Other tools (Pack Office, ArcGis Pro, GIT, Docker)
        """
        )

    st_lottie(lottie_coding, height=200, key="coding")
# --- WORK HISTORY ---
st.write("---")
st.subheader("EXPERIENCE - MY CAREER PATH")

# --- JOB 1
col3, col4 = st.columns([1, 8])
with col3:
    st.image("assets/tte_logo.png", width=75)
with col4:
    st.write("**Data Scientist & Business Analyst | TotalEnergies Pau**")
    st.write("Sept 2023 - Present")
    st.write(
        """
    - ► Development of an application for metal resources prediction in deep groundwaters by ML/AI
    - ► Compilation of global maps, geochemical, geothermal and petrophysical data for predictive models
    - ► Training courses given on the digital tool 
    - ► Prospect resource evaluations
    - ► Development of an interactive PowerBI dashboard
    """
    )

# --- JOB 2
st.write('\n')
col3, col4 = st.columns([1, 8])
with col3:
    st.image("assets/she_logo.png", width=75)
with col4:
    st.write("**Analytical Data Engineer | Safran Helicopter Engines Bordes**")
    st.write("Sept 2022 - Sept 2023")
    st.write(
        """
    - ► ETL design and development of an NLP-based helicopter troubleshooting application 
    - ► Complete project management for the troubleshooting application
    - ► Development of a recovery system based on engine performance data
    - ► ETL performance reporting with Power BI
    """
    )

# --- JOB 3
st.write('\n')
col3, col4 = st.columns([1, 8])
with col3:
    st.image("assets/cgi_logo.png", width=75)
with col4:
    st.write("**Data Science & Operational Research | CGI Montreal**")
    st.write("April 2022 - August 2022")
    st.write(
        """
    - ► Designed a pipeline of distance/time matrixes with calculation and geocoding APIs (Bing, Google) in OOP
    - ► Performance reporting, unit testing and integration of the solution into Google OR-Tools
    - ► Customer service time prediction
    - ► Agile methodology based on Azure cloud architecture
    """
    )

st.write("---")
# --- Projects & Accomplishments ---
st.subheader("Personal projects")

st.write("**Investments** :money_with_wings:")
st.markdown("   • Stock market & Real estate")

st.write("**Video game design** :video_game:")
st.markdown("   • Unreal Engine")

st.write("**Music composition** :musical_note:")
st.markdown("   • FL Studio")

st.write("**Scripting** :robot_face:")
st.markdown("   • Creation of bots for task automation")
st.write("---")

st.subheader("Educational background")

# --- JOB 1
col3, col4 = st.columns([1, 8])
with col3:
    st.image("assets/CY_Tech.png", width=75)
with col4:
    st.write("**Engineering School in Mathematics and Computer Science | CY Tech Pau (ex EISTI)**")
    st.write("2018 - 2023")
    st.write(
        """
    - ► Common core in mathematics and a final-year specialization in computer science, artificial intelligence option
    - ► Member of the CY Tech sports office (communications manager and sports event organizer) 
    """
    )

st.write("---")
# --- Projects & Accomplishments ---
st.subheader("Accomplishments")

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write("---")

st.subheader("Interests & Leisures")

st.write("**Basketball** :basketball:")
st.markdown("- Up to national level & coaching")

st.write("**Other Sports**")
st.markdown("- Motor sports :racing_car:")
st.markdown("- Ski :skier:")
st.markdown("- Surf :surfer:")

st.write("**Discovering new cultures**")
st.markdown("- USA (West Coast, New York) :hamburger:")
st.markdown("- Canada :sunrise_over_mountains:")
st.markdown("- Japan :ideograph_advantage:")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Feel free to contact me !")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mathgpn@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()