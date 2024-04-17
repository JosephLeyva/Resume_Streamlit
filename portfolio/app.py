import streamlit as st
from pathlib import Path
from PIL import Image



# --- PATH Settings ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path().cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'JoseLeyvaCVEnglish.pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.png'


# --- General Settings ---
PAGE_TITLE = "Digital Portfolio | Jose Leyva"
PAGE_ICON = ":technologist:"
NAME = "Jose Leyva"
DESCRIPTION = "Data Scientist | Machine Learning Engineer | Software Developer"
EMAIL = "josealc1998@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/josephleyvac/",
    "GitHub": "https://github.com/josephleyva",
    "Instagram": "https://www.instagram.com/josephleyvacontreras"
}


PROJECTS = {
    "🔥 Dating App with .NET and Angular": "https://github.com/JosephLeyva/DatingApp",
    "🎵 Music Song Prediction with PySpark": "https://github.com/JosephLeyva/Proyecto-BigData",
    "🌱 Web Page for a Local Business (leeca-hmo)": "https://josephleyva.github.io/leeca-hmo/",
    "📖 Web Application for University Guidelines": "https://github.com/JosephLeyva/SistemaEventosFormativosUSON",
    "🖥️ Toy Programming Language Interpreter": "https://github.com/JosephLeyva/Proyecto-Compiladores",
    "💶 Anomaly Detection to Predict Fake Bills": "https://github.com/JosephLeyva/Anomaly-Detection-Swiss-Banknote",
    "🃏 BlackJack Game in C++": "https://github.com/JosephLeyva/BlackJack",
    "🩸 Predicting Blood Donations": "https://github.com/JosephLeyva/Proyecto-Prediccion-Donacion-Sangre-Mexico"
}

ACCOMPLISHMENTS = {
    "🏆 CENEVAL Prize for Excellent Performance": "https://www.linkedin.com/in/josephleyvac",
    "🏵️ Spot Award for Outstanding Performance": "https://www.linkedin.com/posts/josephleyvac_teamfyi-spotaward-softwaredevelopment-activity-7161501492066050048-Gl9Y?utm_source=share&utm_medium=member_desktop",
}

# Specify page title and icon
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("My Personal Portfolio")

# --- LOAD CSS, PDF AND PROFILE PIC ---
with open(css_file, 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with open(resume_file, 'rb') as f:
    resume = f.read()

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=resume,
        file_name="JoseLeyvaCVEnglish.pdf",
        mime="application/pdf",
        key="resume"
    )
    st.write("📬", EMAIL)


# --- SOCIAL MEDIA ---
st.write("### Social Media")
st.write("---")
cols = st.columns(len(SOCIAL_MEDIA))
for i, (name, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[i].markdown(f"##### [{name}]({link})", unsafe_allow_html=True)


# --- EXPERIENCE ---
st.write("#")
st.subheader("Experience and Qualifications")
st.write("---")
st.write(
    """
    - ► 3+ years of experience in software development and data science.
    - ► Strong knowledge of Python, .NET and JavaScript.
    - ► Proactive, self-taught and team player with excellent communication skills.
    - ► Good understanding of machine learning algorithms and data structures.
    """
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 👨🏽‍💻 **Programming Languages**: Python, C#, JavaScript, C++.
    - 🗄️ **Frameworks**: .NET, Angular, Node.js, Flask, Django, Airflow.
    - 🗃️ **Databases**: SQLServer, PostgreSQL, MySQL, MongoDB.
    - 🤖 **Machine Learning**: Scikit-learn, TensorFlow, PyTorch, Spark, Transformers.
    - 📊 **Data Analysis**: Pandas, NumPy, Matplotlib, Seaborn.
    - ⚙️ **Tools**: Git, Docker, Kubernetes.
    - 🎲 **Others**: Web Development, Data Structures, Algorithms.
    """
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")


# --- JOB 1 ---
st.write("#####","🧑🏻‍💻", "**Software Engineer**", "| [Pinnacle Aerospace](https://www.pinnacleaerospace.com/)")
st.write("July 2022 - Present")
st.write(
    """
    - ► Implement Web Applications, APIs and Data Pipelines for FindYourInfluence company.
    - ► Develop and maintain software for the company's internal systems.
    - ► Work with .NET, Angular, Python, Airflow, Docker and Kubernetes.
    - ► Implement Semantic Search Engine by vectorizing text data with Transformers.
    - ► Develop and maintain ETL processes for data ingestion and processing.
    - ► Implement Machine Learning Models for Predictive Analytics and Anomaly Detection.   
    """
)


# --- JOB 2 ---
st.write("#####", "👁️‍🗨️", "**Computer Vision Engineer**", "| [ECN](https://ecnautomation.com/)")
st.write("January 2022 - June 2022")
st.write(
    """
    - ► Developed Scripts for Image Processing and Computer Vision.
    - ► Implemented Machine Learning Models for Object Detection and Image Classification.
    - ► Worked with Pytorch, OpenCV and Scikit-learn. 
    - ► Programmed Scripts for Intel RealSense LiDAR Cameras.
    - ► Worked with Jetson Nano for embedded computer vision applications.
    """
)


#--- PROJECTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
st.write("##### Projects")
for name, link in PROJECTS.items():
    st.write(f"[{name}]({link})")
st.write("---")
st.write("##### Accomplishments")
for name, link in ACCOMPLISHMENTS.items():
    st.write(f"[{name}]({link})")