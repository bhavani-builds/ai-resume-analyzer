import streamlit as st
import re


# ------------------------------------------
# Page configuration
# ------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# ------------------------------------------
# Title
# ------------------------------------------

st.title("🤖 AI Resume Analyzer")

st.write(
    "Analyze a resume against a target job description."
)


# ------------------------------------------
# Skill database
# ------------------------------------------

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
    "mongodb"
]


# ------------------------------------------
# Input sections
# ------------------------------------------

st.subheader("📄 Resume")

resume_text = st.text_area(
    "Paste your resume text here",
    height=250
)


st.subheader("💼 Job Description")

job_text = st.text_area(
    "Paste the job description here",
    height=250
)


# ------------------------------------------
# Analyze button
# ------------------------------------------

if st.button(
    "🔍 Analyze Resume",
    type="primary"
):

    if not resume_text or not job_text:

        st.warning(
            "Please provide both resume text and job description."
        )

    else:

        resume_lower = resume_text.lower()

        job_lower = job_text.lower()


        # ----------------------------------
        # Extract resume skills
        # ----------------------------------

        resume_skills = []

        for skill in skills:

            pattern = (
                r"\b"
                + re.escape(skill)
                + r"\b"
            )

            if re.search(
                pattern,
                resume_lower
            ):

                resume_skills.append(
                    skill
                )


        # ----------------------------------
        # Extract job skills
        # ----------------------------------

        required_skills = []

        for skill in skills:

            pattern = (
                r"\b"
                + re.escape(skill)
                + r"\b"
            )

            if re.search(
                pattern,
                job_lower
            ):

                required_skills.append(
                    skill
                )


        # ----------------------------------
        # Compare skills
        # ----------------------------------

        matching_skills = [
            skill
            for skill in required_skills
            if skill in resume_skills
        ]


        missing_skills = [
            skill
            for skill in required_skills
            if skill not in resume_skills
        ]


        # ----------------------------------
        # Match score
        # ----------------------------------

        if required_skills:

            score = (
                len(matching_skills)
                / len(required_skills)
            ) * 100

        else:

            score = 0


        # ----------------------------------
        # Display metrics
        # ----------------------------------

        st.divider()

        st.subheader(
            "📊 Resume Analysis"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Match Score",
                f"{score:.1f}%"
            )

        with col2:

            st.metric(
                "Matching Skills",
                len(matching_skills)
            )

        with col3:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )


        # ----------------------------------
        # Matching skills
        # ----------------------------------

        st.subheader(
            "✅ Matching Skills"
        )

        if matching_skills:

            st.success(
                ", ".join(
                    skill.title()
                    for skill in matching_skills
                )
            )

        else:

            st.info(
                "No matching skills found."
            )


        # ----------------------------------
        # Missing skills
        # ----------------------------------

        st.subheader(
            "❌ Missing Skills"
        )

        if missing_skills:

            st.error(
                ", ".join(
                    skill.title()
                    for skill in missing_skills
                )
            )

        else:

            st.success(
                "No major missing skills!"
            )


        # ----------------------------------
        # Resume skills
        # ----------------------------------

        st.subheader(
            "🧠 Skills Found in Resume"
        )

        if resume_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in resume_skills
                )
            )

        else:

            st.info(
                "No known skills detected."
            )


        # ----------------------------------
        # Recommendation
        # ----------------------------------

        st.subheader(
            "💡 Recommendation"
        )

        if score >= 80:

            st.success(
                "Excellent match! Your resume "
                "strongly matches this job."
            )

        elif score >= 60:

            st.warning(
                "Good match. Consider improving "
                "the missing skills."
            )

        elif score >= 40:

            st.warning(
                "Moderate match. You should "
                "strengthen several required skills."
            )

        else:

            st.error(
                "Low match. Consider building "
                "skills relevant to this job."
            )
