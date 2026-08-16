import streamlit as st
import fitz
import re


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# SKILL DATABASE
# ==========================================

skills = [
    "python",
    "c",
    "java",
    "sql",
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "opencv",
    "scikit-learn",
    "matlab",
    "vlsi",
    "embedded systems",
    "pcb design",
    "cadence",
    "proteus",
    "git",
    "github",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "mongodb",
    "docker",
    "aws"
]


# ==========================================
# SKILL CATEGORIES
# ==========================================

skill_categories = {

    "Programming": [
        "python",
        "c",
        "java",
        "sql",
        "javascript"
    ],

    "AI / ML": [
        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "opencv",
        "scikit-learn"
    ],

    "Data Science": [
        "numpy",
        "pandas",
        "matplotlib",
        "scipy"
    ],

    "ECE / VLSI": [
        "matlab",
        "vlsi",
        "embedded systems",
        "pcb design",
        "cadence",
        "proteus"
    ],

    "Web / Software": [
        "html",
        "css",
        "react",
        "node.js",
        "mongodb"
    ],

    "Tools / Cloud": [
        "git",
        "github",
        "docker",
        "aws"
    ]
}


# ==========================================
# RECOMMENDATIONS
# ==========================================

recommendations = {

    "python":
        "Practice Python programming and problem solving.",

    "sql":
        "Learn SQL queries, joins, grouping and database design.",

    "machine learning":
        "Study classification, regression and model evaluation.",

    "deep learning":
        "Learn neural networks, CNNs and model training.",

    "tensorflow":
        "Build and train neural networks using TensorFlow.",

    "vlsi":
        "Strengthen digital design, CMOS and Verilog concepts.",

    "embedded systems":
        "Practice microcontrollers, sensors and embedded C.",

    "pcb design":
        "Practice schematic capture, PCB layout and routing.",

    "git":
        "Practice branching, merging and collaborative Git workflows.",

    "docker":
        "Learn containers, images and application deployment.",

    "aws":
        "Learn basic AWS cloud services and deployment."
}


# ==========================================
# FUNCTIONS
# ==========================================

def extract_pdf_text(uploaded_file):

    document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:

        text += page.get_text()

    document.close()

    return text


def find_skills(text):

    text = text.lower()

    found = []

    for skill in skills:

        pattern = (
            r"\b"
            + re.escape(skill)
            + r"\b"
        )

        if re.search(
            pattern,
            text
        ):

            found.append(skill)

    return found


def calculate_match(
    resume_skills,
    job_skills
):

    if not job_skills:

        return 0, [], []

    matching = [
        skill
        for skill in job_skills
        if skill in resume_skills
    ]

    missing = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    score = (
        len(matching)
        / len(job_skills)
    ) * 100

    return score, matching, missing


# ==========================================
# HEADER
# ==========================================

st.title(
    "🤖 AI Resume Analyzer"
)

st.write(
    "Analyze your resume, compare it with a job description, "
    "identify skill gaps and receive improvement recommendations."
)


st.divider()


# ==========================================
# INPUT
# ==========================================

left, right = st.columns(2)


with left:

    st.subheader(
        "📄 Resume"
    )

    uploaded_resume = st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )


with right:

    st.subheader(
        "💼 Job Description"
    )

    job_description = st.text_area(
        "Paste the job description",
        height=220,
        placeholder="Paste the complete job description here..."
    )


# ==========================================
# ANALYZE
# ==========================================

analyze = st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
)


if analyze:

    if uploaded_resume is None:

        st.warning(
            "Please upload a resume PDF."
        )

        st.stop()


    if not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

        st.stop()


    # --------------------------------------
    # Extract resume text
    # --------------------------------------

    resume_text = extract_pdf_text(
        uploaded_resume
    )


    # --------------------------------------
    # Extract skills
    # --------------------------------------

    resume_skills = find_skills(
        resume_text
    )

    job_skills = find_skills(
        job_description
    )


    # --------------------------------------
    # Match skills
    # --------------------------------------

    match_score, matching, missing = (
        calculate_match(
            resume_skills,
            job_skills
        )
    )


    # ======================================
    # ATS SCORE
    # ======================================

    if job_skills:

        ats_score = (
            len(matching)
            / len(job_skills)
        ) * 100

    else:

        ats_score = 0


    # ======================================
    # SECTION SCORE
    # ======================================

    resume_lower = resume_text.lower()

    sections = [
        "education",
        "skills",
        "projects",
        "experience",
        "internship",
        "certification",
        "achievement"
    ]

    sections_found = sum(
        section in resume_lower
        for section in sections
    )

    section_score = (
        sections_found
        / len(sections)
    ) * 100


    # ======================================
    # FINAL SCORE
    # ======================================

    final_score = (
        match_score * 0.45
        + ats_score * 0.30
        + section_score * 0.25
    )


    # ======================================
    # RESULTS
    # ======================================

    st.divider()

    st.header(
        "📊 Resume Analysis Results"
    )


    # ======================================
    # SCORE CARDS
    # ======================================

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "🏆 Final Score",
            f"{final_score:.1f}/100"
        )


    with col2:

        st.metric(
            "💼 Job Match",
            f"{match_score:.1f}%"
        )


    with col3:

        st.metric(
            "📋 ATS Score",
            f"{ats_score:.1f}%"
        )


    with col4:

        st.metric(
            "📑 Section Quality",
            f"{section_score:.1f}%"
        )


    # ======================================
    # MATCHING SKILLS
    # ======================================

    st.subheader(
        "✅ Matching Skills"
    )


    if matching:

        st.success(
            " • ".join(
                skill.title()
                for skill in matching
            )
        )

    else:

        st.info(
            "No matching skills detected."
        )


    # ======================================
    # MISSING SKILLS
    # ======================================

    st.subheader(
        "❌ Missing Skills"
    )


    if missing:

        st.error(
            " • ".join(
                skill.title()
                for skill in missing
            )
        )

    else:

        st.success(
            "Excellent! No detected skill gaps."
        )


    # ======================================
    # RESUME SKILLS
    # ======================================

    st.subheader(
        "🧠 Skills Found in Resume"
    )


    if resume_skills:

        st.write(
            " • ".join(
                skill.title()
                for skill in resume_skills
            )
        )


    # ======================================
    # SKILL GAP RECOMMENDATIONS
    # ======================================

    st.subheader(
        "🎯 Recommended Improvements"
    )


    if missing:

        for skill in missing:

            message = recommendations.get(
                skill,
                f"Build practical projects and gain experience with {skill.title()}."
            )

            st.write(
                f"**{skill.title()}** → {message}"
            )

    else:

        st.success(
            "Your detected skills cover the job requirements well."
        )


    # ======================================
    # SECTION ANALYSIS
    # ======================================

    st.subheader(
        "📑 Resume Sections"
    )


    for section in sections:

        if section in resume_lower:

            st.write(
                f"✅ {section.title()}"
            )

        else:

            st.write(
                f"❌ {section.title()}"
            )


    # ======================================
    # FINAL FEEDBACK
    # ======================================

    st.divider()

    st.header(
        "💡 Overall Feedback"
    )


    if final_score >= 85:

        st.success(
            "🔥 Excellent resume! "
            "Your resume strongly matches the target job."
        )

    elif final_score >= 70:

        st.success(
            "🚀 Good resume! "
            "A few improvements could make it stronger."
        )

    elif final_score >= 50:

        st.warning(
            "⚠️ Moderate resume. "
            "Focus on missing skills and important resume sections."
        )

    else:

        st.error(
            "📈 Your resume needs improvement. "
            "Focus on relevant skills, projects and job keywords."
        )
